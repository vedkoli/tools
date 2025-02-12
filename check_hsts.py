import requests

def check_hsts(url):
    try:
        response = requests.get(url, timeout=5, allow_redirects=True)
        if 'strict-transport-security' in response.headers:
            return True
        return False
    except requests.exceptions.RequestException:
        return None

def main():
    input_file = "urls.txt"
    output_file = "hsts_results.txt"

    try:
        with open(input_file, "r") as f:
            urls = [line.strip() for line in f if line.strip()]

        results = []
        for url in urls:
            if not url.startswith("http"):
                url = "https://" + url  # Default to HTTPS if not provided

            status = check_hsts(url)
            if status is True:
                results.append(f"{url} - HSTS Enabled")
            elif status is False:
                results.append(f"{url} - HSTS Not Enabled")
            else:
                results.append(f"{url} - Failed to Check")

        with open(output_file, "w") as f:
            f.write("\n".join(results))

        print(f"Check completed! Results saved in {output_file}")

    except FileNotFoundError:
        print(f"Error: {input_file} not found.")

if __name__ == "__main__":
    main()
