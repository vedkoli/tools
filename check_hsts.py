import requests

def check_hsts(url):
    """Check if a URL has the HSTS header enabled."""
    try:
        response = requests.get(url, timeout=5, allow_redirects=True)
        return 'strict-transport-security' in response.headers
    except requests.exceptions.RequestException:
        return None  # Return None if request fails

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

        hsts_enabled = []
        hsts_disabled = []
        failed_urls = []

        for url in urls:
            status = check_hsts(url)
            if status is True:
                hsts_enabled.append(url)
            elif status is False:
                hsts_disabled.append(url)
            else:
                failed_urls.append(url)

        print("\nHSTS Enabled URLs:")
        print(hsts_enabled if hsts_enabled else "None")

        print("\nHSTS Not Enabled URLs:")
        print(hsts_disabled if hsts_disabled else "None")

        print("\nFailed to Check:")
        print(failed_urls if failed_urls else "None")

    except FileNotFoundError:
        print(f"Error: {input_file} not found.")

if __name__ == "__main__":
    main()
