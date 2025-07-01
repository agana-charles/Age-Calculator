import nmap
import socket


def scan_network(network_range):
    scanner = nmap.PortScanner()
    scanner.scan(hosts=network_range, arguments='-p 22,80,443 --open -sV')
    
    report = []

    for host in scanner.all_hosts():
        host_data = {
            'ip': host,
            'open_ports': []
        }
        for proto in scanner[host].all_protocols():
            ports = scanner[host][proto].keys()
            for port in ports:
                service = scanner[host][proto][port]
                host_data['open_ports'].append({
                    'port': port,
                    'name': service['name'],
                    'product': service.get('product', 'N/A'),
                    'version': service.get('version', 'N/A')
                })
        report.append(host_data)
    
    return report

def save_report(report, filename="network_report.txt"):
    with open(filename, 'w') as f:
        for device in report:
            f.write(f"IP: {device['ip']}\n")
            for port in device['open_ports']:
                f.write(f"  Port {port['port']} ({port['name']}): {port['product']} {port['version']}\n")
            f.write("\n")

if __name__ == "__main__":
    network = "192.168.1.0/24"  # Adjust to your network
    print("Scanning network...")
    results = scan_network(network)
    print("Scan complete. Saving report...")
    save_report(results)
    print("Report saved as 'network_report.txt'")