import socket

def check_ports(target, ports):
    print(f"[+] Checking ports on target: {target}")
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.5)
                result = sock.connect_ex((target, port))
                if result == 0:
                    print(f"[✓] Port {port} is open")
                else:
                    print(f"[-] Port {port} is closed")
        except Exception as e:
            print(f"[!] Error checking port {port}: {e}")

if __name__ == "__main__":
    target_host = input("Enter the target IP address or domain: ").strip()
    port_input = input("Enter ports separated by commas (e.g., 22,80,443): ").strip()

    if not target_host or not port_input:
        print("[!] You must enter both the target and port list.")
    else:
        try:
            ports = [int(p.strip()) for p in port_input.split(",") if p.strip().isdigit()]
            if not ports:
                print("[!] No valid ports detected.")
            else:
                check_ports(target_host, ports)
        except Exception as e:
            print(f"[!] Error processing ports: {e}")
