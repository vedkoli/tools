import subprocess

def get_server_info(url):
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
        return f"Error: {e}", "N/A"

def main():
    input_file = "url.txt"
    
    try:
        with open(input_file, "r") as file:
            urls = [line.strip() for line in file if line.strip()]
        
        for url in urls:
            server_info, response_code = get_server_info(url)
            print(f"{url} - {server_info} - {response_code}")

    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
    except Exception as e:
        print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    main()
