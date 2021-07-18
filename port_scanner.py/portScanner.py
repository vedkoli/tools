import socket
from IPy import IP

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def scan(target, s, e):
    converted_ip = check_ip(target)
    print("\n" + "[-+-] Scanning target :" + converted_ip)
    for port in range(int(s), int(e)):
        port_scan(converted_ip , port)

def get_banner(sock):
    return sock.recv(1024)


def port_scan(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print("[+] port " + str(port) + " is open     " + str(banner))
        except:

            print("[+] port " + str(port) + " is open")
    except:
            pass
        #print("[+] port " + str(port) + " is close")


target = input("[+] Enter target address (if more than one , separate win ,): ")
start_port = input("[+]Enter staring port number : ")
end_port = input("[+]Enter ending port number : ")

if "," in target:
    for ip in target.split(","):
        scan(ip.strip(" "),start_port, end_port)
else:
    scan(target, start_port, end_port)




