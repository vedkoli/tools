import socket
from IPy import IP

ipaddress = input("[+] enter ip address : ")
port = 80


try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Port 80 is open")
except:
        print("[-] Port 80  is close")
