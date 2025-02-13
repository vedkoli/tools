import subprocess
import sys
from tqdm import tqdm  # Progress bar support

def check_clickjacking(url):
    try:
        # Fetch headers using curl
        cmd = f'curl -s -I -L {url}'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        headers = result.stdout.split("\n")
        response_code = "Unknown"
        x_frame_options = None

        for header in headers:
            if header.startswith("HTTP/"):
                response_code = header.split()[1]  # Extract HTTP status code
            if header.lower().startswith("x-frame-options"):
                x_frame_options = header.split(":", 1)[1].strip().lower()

        # Clickjacking vulnerability detected if no X-Frame-Options header
        is_vulnerable = x_frame_options is None and response_code == "200"

        return is_vulnerable, response_code
    except Exception as e:
        return False, "Error"

def main():
    # Get filename from command-line arguments or use default "url.txt"
    input_file = sys.argv[1] if len(sys.argv) > 1 else "url.txt"
    vulnerable_urls = []

    try:
        with open(input_file, "r") as file:
            urls = [line.strip() for line in file if line.strip()]

        print(f"Checking for Clickjacking in '{input_file}'...\n")
        for url in tqdm(urls, desc="Scanning", ncols=80, ascii=True, unit="url"):
            is_vulnerable, response_code = check_clickjacking(url)
            if is_vulnerable:
                vulnerable_urls.append(url)

        print("\nVulnerable URLs (Clickjacking detected with 200 OK):\n")
        for url in vulnerable_urls:
            print(url)

    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
    except Exception as e:
        print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    main()
