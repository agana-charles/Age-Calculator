import nmap
import sys

COMMON_PORTS = '22,80,443'

def scan_targets(targets):
    nm = nmap.PortScanner()
    all_results = {}

    for target in targets:
        print(f"Scanning {target} for common ports...")
        nm.scan(target, COMMON_PORTS, arguments='-sV')
        for host in nm.all_hosts():
            all_results.setdefault(host, [])
            for proto in nm[host].all_protocols():
                for port in nm[host][proto].keys():
                    port_info = nm[host][proto][port]
                    state = port_info['state']
                    service = port_info['name']
                    version = port_info.get('version', '')
                    product = port_info.get('product', '')
                    extrainfo = port_info.get('extrainfo', '')
                    banner = f"{product} {version} {extrainfo}".strip()
                    all_results[host].append({
                        'port': port,
                        'state': state,
                        'service': service,
                        'banner': banner
                    })
    return all_results

def scan_ssh_on_network(network):
    nm = nmap.PortScanner()
    print(f"Scanning {network} for devices with open SSH ports...")
    nm.scan(network, '22', arguments='-sV')
    ssh_devices = []
    for host in nm.all_hosts():
        if 'tcp' in nm[host] and 22 in nm[host]['tcp']:
            port_info = nm[host]['tcp'][22]
            if port_info['state'] == 'open':
                product = port_info.get('product', '')
                version = port_info.get('version', '')
                extrainfo = port_info.get('extrainfo', '')
                banner = f"{product} {version} {extrainfo}".strip()
                ssh_devices.append({
                    'ip': host,
                    'banner': banner
                })
    return ssh_devices

def generate_report(scan_results, ssh_results, filename="scan_report.txt"):
    with open(filename, "w") as f:
        f.write("=== General Port Scan Results ===\n\n")
        for ip, ports in scan_results.items():
            f.write(f"IP: {ip}\n")
            if ports:
                for port_info in ports:
                    f.write(f"  Port {port_info['port']} ({port_info['service']}) is {port_info['state']}\n")
                    if port_info['banner']:
                        f.write(f"    Banner: {port_info['banner']}\n")
                        if any(keyword in port_info['banner'].lower() for keyword in ["apache/2.2", "openssl 0.", "ssh-1."]):
                            f.write(f"    Potential outdated software detected!\n")
            else:
                f.write("  No common ports open.\n")
            f.write("\n")

        f.write("=== Devices with Open SSH Ports ===\n\n")
        if ssh_results:
            for device in ssh_results:
                f.write(f"IP: {device['ip']}\n")
                f.write(f"  SSH Banner: {device['banner']}\n\n")
        else:
            f.write("No devices with open SSH ports found.\n")

    print(f"Report saved to {filename}")

def main():
    if len(sys.argv) < 3:
        print("Usage: python nmap_advanced_scan.py <ip1> <ip2> ... <network_range>")
        print("Example: python nmap_advanced_scan.py 192.168.1.1 192.168.1.2 192.168.1.0/24")
        sys.exit(1)

    targets = sys.argv[1:-1]
    network = sys.argv[-1]

    # Scan common ports on given IPs or ranges
    scan_results = scan_targets(targets)

    # Scan network for devices with open SSH ports
    ssh_results = scan_ssh_on_network(network)

    # Generate combined report
    generate_report(scan_results, ssh_results)

if __name__ == "__main__":
    main()