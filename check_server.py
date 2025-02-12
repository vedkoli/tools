import requests
from collections import defaultdict

def get_server_info(url):
    """Check if a URL has a 'Server' header and return it if the response is 200 OK."""
    try:
        response = requests.get(url, timeout=5, allow_redirects=True)
        if response.status_code == 200:
            return response.headers.get("Server", "Unknown")  # If no 'Server' header, return 'Unknown'
    except requests.exceptions.RequestException:
        return None  # Return None if request fails
    return None

def format_urls(url):
    """Generate both HTTP and HTTPS versions of the URL."""
    url = url.strip().lstrip("http://").lstrip("https://")  # Remove existing scheme
    return [f"http://{url}", f"https://{url}"]

def main():
    input_file = "urls.txt"

    try:
        with open(input_file, "r") as f:
            urls = [line.strip() for line in f if line.strip()]  # Read and clean URLs

        server_dict = defaultdict(list)

        for url in urls:
            http_url, https_url = format_urls(url)

            # Check HTTPS first, then HTTP if HTTPS fails
            for test_url in [https_url, http_url]:
                server = get_server_info(test_url)
                if server:
                    server_dict[server].append(test_url)
                    break  # Stop after finding the first successful response

        if server_dict:
            print("\nServer Information (200 OK Responses Only):")
            for server, url_list in server_dict.items():
                print(f"\n{server}:")
                print("\n".join(url_list))
        else:
            print("No servers detected for URLs with status 200.")

    except FileNotFoundError:
        print(f"Error: {input_file} not found.")

if __name__ == "__main__":
    main()
