import ssl
import socket
from urllib.parse import urlparse

def check_tls_version(url, tls_version):
    try:
        # Parse the URL to get the hostname and port
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname
        port = parsed_url.port or 443  # Default to port 443 if not specified

        # Create a socket and wrap it with SSL context
        context = ssl.SSLContext(tls_version)
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # If the connection is successful, the TLS version is enabled
                return True
    except (ssl.SSLError, socket.error) as e:
        # If an error occurs, the TLS version is not enabled
        return False

def check_urls_for_tls(file_path):
    with open(file_path, 'r') as file:
        urls = file.read().splitlines()

    tls_10_enabled = []
    tls_11_enabled = []

    for url in urls:
        if check_tls_version(url, ssl.PROTOCOL_TLSv1):
            tls_10_enabled.append(url)
        if check_tls_version(url, ssl.PROTOCOL_TLSv1_1):
            tls_11_enabled.append(url)

    print("URLs with TLS 1.0 enabled:")
    for url in tls_10_enabled:
        print(url)

    print("\nURLs with TLS 1.1 enabled:")
    for url in tls_11_enabled:
        print(url)

if __name__ == "__main__":
    # Replace 'urls.txt' with the path to your text file containing URLs
    check_urls_for_tls('urls.txt')
