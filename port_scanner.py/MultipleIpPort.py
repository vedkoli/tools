import socket
from IPy import IP

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def scan(ip):
    convert_ip = check_ip(ip)
    print("\n" + "[-_0 Scanning target]" + str(convert_ip))

    for port in range(75, 85):
        scan_port(convert_ip, port)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        print("[+] port " + str(port) + " is open")
    except:
        print("[+] port " + str(port) + " is close")



ipaddress = input("[+] Enter ip/s address : ( split multiple target with ,): ")
if "," in ipaddress:
    for ip in ipaddress.split(','):
        scan(ip.strip(' '))
else:
        scan(ipaddress)




