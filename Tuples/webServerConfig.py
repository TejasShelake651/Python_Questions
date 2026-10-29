# Web Server Configuration using Tuples and Lists

server_ip = (192, 168, 1, 1)
allowed_ips = ["192.168.1.2", "192.168.1.3"]

def update_allowed(ip):
    allowed_ips.append(ip)
    print(f"Added IP {ip} to allowed list.")

def display_config():
    print("Server IP (Tuple - Immutable):", server_ip)
    print("Allowed IPs (List - Mutable):", allowed_ips)

if __name__ == "__main__":
    display_config()
    update_allowed("192.168.1.100")
    display_config()
