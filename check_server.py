import requests
from collections import defaultdict

def get_server_info(url):
    """Check if a URL has a 'Server' header and return it if the response is 200."""
    try:
        response = requests.get(url, timeout=5, allow_redirects=True)
        if response.status_code == 200:
            return response.headers.get("Server", "Unknown")  # Return 'Unknown' if no Server header
    except requests.exceptions.RequestException:
        return None  # Return None if request fails
    return None

def format_url(url):
    """Ensure the URL starts with https://"""
    url = url.strip()
    if not url.startswith(("http://", "https://")):
        url = "https://" + url  # Default to HTTPS
    return url

def main():
    input_file = "urls.txt"

    try:
        with open(input_file, "r") as f:
            urls = [format_url(line) for line in f if line.strip()]  # Clean URLs

        server_dict = defaultdict(list)

        for url in urls:
            server = get_server_info(url)
            if server:  # Only add if server info is found
                server_dict[server].append(url)

        if server_dict:
            print("\nServer Information:")
            for server, url_list in server_dict.items():
                print(f"\n{server}:")
                print("\n".join(url_list))
        else:
            print("No servers detected for URLs with status 200.")

    except FileNotFoundError:
        print(f"Error: {input_file} not found.")

if __name__ == "__main__":
    main()
