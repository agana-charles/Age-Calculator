import requests
from bs4 import BeautifulSoup
import urllib.parse

# Payloads to test vulnerabilities
sql_payloads = ["' OR '1'='1", '" OR "1"="1', "';--"]
xss_payloads = ["<script>alert(1)</script>", "<img src=x onerror=alert(1)>"]

def get_forms(url):
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    return soup.find_all("form")

def get_form_details(form):
    details = {}
    action = form.attrs.get("action")
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

def is_vulnerable(response, payload_type="sql"):
    errors = {
        "sql": ["you have an error in your sql syntax", "warning: mysql", "unclosed quotation mark", "quoted string not properly terminated"],
        "xss": ["<script>alert(1)</script>", "<img src=x onerror=alert(1)>"]
    }
    for error in errors[payload_type]:
        if error.lower() in response.text.lower():
            return True
    return False

def submit_form(form_details, url, payload, payload_type="sql"):
    target_url = urllib.parse.urljoin(url, form_details["action"])
    data = {}
    for input_field in form_details["inputs"]:
        if input_field["type"] == "text" or input_field["type"] == "search":
            data[input_field["name"]] = payload
        elif input_field["name"]:
            data[input_field["name"]] = "test"

    if form_details["method"] == "post":
        res = requests.post(target_url, data=data)
    else:
        res = requests.get(target_url, params=data)

    return is_vulnerable(res, payload_type)

def scan_url(url):
    forms = get_forms(url)
    print(f"[+] Detected {len(forms)} form(s) on {url}")
    report = []

    for i, form in enumerate(forms):
        form_details = get_form_details(form)

        for payload in sql_payloads:
            if submit_form(form_details, url, payload, "sql"):
                report.append(f"[!] SQL Injection vulnerability detected in form #{i + 1} at {url} using payload: {payload}")
                break

        for payload in xss_payloads:
            if submit_form(form_details, url, payload, "xss"):
                report.append(f"[!] XSS vulnerability detected in form #{i + 1} at {url} using payload: {payload}")
                break

    return report

def save_report(results, filename="web_vulnerability_report.txt"):
    with open(filename, "w") as f:
        for line in results:
            f.write(line + "\n")
    print(f"\n[+] Report saved to {filename}")

if __name__ == "__main__":
    target = input("Enter URL to scan (e.g., http://testphp.vulnweb.com): ")
    findings = scan_url(target)
    if findings:
        for f in findings:
            print(f)
    else:
        print("[-] No vulnerabilities found.")
    save_report(findings)