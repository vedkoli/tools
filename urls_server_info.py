import subprocess

def get_response_code(url):
    try:
        # Execute curl command to fetch response code
        cmd = f'curl -s -o /dev/null -w "%{{http_code}}" -L {url}'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        return result.stdout.strip()
    except Exception as e:
        return "Error"

def main():
    input_file = "url.txt"
    
    try:
        with open(input_file, "r") as file:
            urls = [line.strip() for line in file if line.strip()]
        
        for url in urls:
            response_code = get_response_code(url)
            if response_code == "200":  # Only show URLs with a 200 response code
                print(url)

    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
    except Exception as e:
        print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    main()
