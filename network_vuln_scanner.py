import nmap
import sys
import ipaddress
from datetime import datetime

# Define ports of interest
PORTS = '22,80,443'

# Output file
OUTPUT_FILE = 'vuln_scan_report.txt'


def scan_ip(ip):
    scanner = nmap.PortScanner()
    print(f"[*] Scanning {ip}...")

    try:
        scanner.scan(
            hosts=ip,
            ports=PORTS,
            arguments='--script=banner -T4'
        )
    except Exception as e:
        print(f"[!] Error scanning {ip}: {e}")
        return ""

    report_lines = []
    if ip not in scanner.all_hosts():
        return ""

    report_lines.append(f"\nHost: {ip}")
    report_lines.append(f"State: {scanner[ip].state()}")

    if 'tcp' in scanner[ip]:
        for port in sorted(scanner[ip]['tcp']):
            port_data = scanner[ip]['tcp'][port]
            report_lines.append(f"\n  Port {port} ({port_data.get('name', 'unknown')}):")
            report_lines.append(f"    State   : {port_data.get('state', '')}")
            report_lines.append(f"    Product : {port_data.get('product', '')}")
            report_lines.append(f"    Version : {port_data.get('version', '')}")
            if 'script' in port_data:
                for script, output in port_data['script'].items():
                    report_lines.append(f"    [{script}]: {output.strip()}")

    return '\n'.join(report_lines)


def main():
    if len(sys.argv) != 2:
        print("Usage: python network_vuln_scanner.py <CIDR|IP|ips.txt>")
        return

    target_input = sys.argv[1]
    targets = []

    try:
        if target_input.endswith(".txt"):
            with open(target_input, 'r') as f:
                targets = [line.strip() for line in f if line.strip()]
        elif '/' in target_input:
            net = ipaddress.IPv4Network(target_input, strict=False)
            targets = [str(ip) for ip in net.hosts()]
        else:
            targets = [target_input]
    except Exception as e:
        print(f"[!] Error parsing input: {e}")
        return

    with open(OUTPUT_FILE, 'w') as f:
        f.write(f"Nmap Vulnerability Scan Report\nGenerated: {datetime.now()}\n")
        f.write("="*60 + "\n")

        for ip in targets:
            result = scan_ip(ip)
            if result:
                f.write(result)
                f.write("\n" + "-"*60 + "\n")

    print(f"\n[+] Scan complete. Results saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
