import nmap
from vulners import Vulners

# Initialize Vulners API
vulners_api = Vulners(api_key="YOUR_API_KEY_HERE")  # Replace with your real API key from vulners.com

def check_vulnerabilities(product, version):
    try:
        results = vulners_api.softwareVulnerabilities(product, version)
        cves = [item['id'] for item in results['data']['search']]
        return cves
    except Exception as e:
        return [f"Error checking CVEs: {e}"]

def scan_network(network_range):
    scanner = nmap.PortScanner()
    print(f"Scanning network: {network_range}")
    scanner.scan(hosts=network_range, arguments='-p 22,80,443 --open -sV')

    report = []

    for host in scanner.all_hosts():
        print(f"Scanning host: {host}")
        host_data = {
            'ip': host,
            'open_ports': []
        }

        for proto in scanner[host].all_protocols():
            ports = scanner[host][proto].keys()
            for port in ports:
                service = scanner[host][proto][port]
                product = service.get('product', '')
                version = service.get('version', '')

                cves = check_vulnerabilities(product, version) if product and version else []

                host_data['open_ports'].append({
                    'port': port,
                    'name': service['name'],
                    'product': product,
                    'version': version,
                    'vulnerabilities': cves
                })

        report.append(host_data)

    return report

def save_report(report, filename='network_report.txt'):
    with open(filename, 'w') as f:
        for device in report:
            f.write(f"IP: {device['ip']}\n")
            for port in device['open_ports']:
                f.write(f"  Port {port['port']} ({port['name']}): {port['product']} {port['version']}\n")
                if port['vulnerabilities']:
                    for cve in port['vulnerabilities']:
                        f.write(f"    - Vulnerability: {cve}\n")
            f.write("\n")

    print(f"\nReport saved to {filename}")

if __name__ == "__main__":
    network = "192.168.1.0/24"  # Replace with your network
    results = scan_network(network)
    save_report(results)