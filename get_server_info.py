import subprocess
import sys
from collections import defaultdict
from tqdm import tqdm  # Import tqdm for progress bar

def get_server_info_and_response(url):
    try:
        # Execute curl command to fetch server header and response code
        cmd = f'curl -s -I -L {url}'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        # Parse headers to extract Server and Response Code
        headers = result.stdout.split("\n")
        server_info = "Unknown"
        response_code = "Unknown"

        for header in headers:
            if header.lower().startswith("server:"):
                server_info = header.split(":", 1)[1].strip()
            if header.startswith("HTTP/"):
                response_code = header.split()[1]

        return server_info, response_code
    except Exception as e:
        return "Error", "N/A"

def main():
    # Get filename from command-line arguments or use default "url.txt"
    input_file = sys.argv[1] if len(sys.argv) > 1 else "url.txt"
    server_dict = defaultdict(list)  # Dictionary to store URLs grouped by server info

    try:
        with open(input_file, "r") as file:
            urls = [line.strip() for line in file if line.strip()]

        print(f"Processing URLs from '{input_file}'...\n")
        for url in tqdm(urls, desc="Checking", ncols=80, ascii=True, unit="url"):
            server_info, response_code = get_server_info_and_response(url)
            if response_code == "200":  # Only store URLs with a 200 response code
                server_dict[server_info].append(url)

        print("\n")  # Ensure a new line after progress bar completion

        # Print the grouped output
        for server, url_list in server_dict.items():
            print(f"{server} 200")
            for url in url_list:
                print(url)
            print()  # Blank line for readability

    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
    except Exception as e:
        print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    main()
