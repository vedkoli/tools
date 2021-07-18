import socket
from IPy import IP

def real_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)


ipaddress = input("[+] Enter ip or domain : ")



print(real_ip(ipaddress))