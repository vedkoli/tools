import requests

def check_hsts_header(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            hsts_header = response.headers.get('Strict-Transport-Security')
            if hsts_header:
                return True, hsts_header
            else:
                return False, None
        else:
            return None, None
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None, None

def main():
    # Take input URLs separated by commas
    urls_input = input("Enter URLs separated by commas: ")
    urls = [url.strip() for url in urls_input.split(',')]

    for url in urls:
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url

        has_hsts, hsts_header = check_hsts_header(url)
        if has_hsts is None:
            print(f"{url} did not return a 200 OK response.")
        elif has_hsts:
            print(f"{url} has HSTS header set: {hsts_header}")
        else:
            print(f"{url} does not have HSTS header set.")

if __name__ == "__main__":
    main()