import socket
from IPy import IP

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def port_scan(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        print("[+] port " + str(port) + " is open")
    except:
        print("[+] port " + str(port) + " is close")

ipaddress = input("[+] Enter ip address : ")
converted_ip = check_ip(ipaddress)


for port in range(75,85):
    port_scan(converted_ip, port)

print(converted_ip)


