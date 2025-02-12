import requests

def check_clickjacking(url):
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers

        x_frame_options = headers.get("X-Frame-Options", "Missing")
        csp = headers.get("Content-Security-Policy", "Missing")

        if x_frame_options == "Missing" and csp == "Missing":
            result = "VULNERABLE (No X-Frame-Options & CSP)"
        elif x_frame_options in ["DENY", "SAMEORIGIN"] or "frame-ancestors" in csp:
            result = "NOT VULNERABLE (Proper Headers Found)"
        else:
            result = f"POTENTIALLY VULNERABLE (X-Frame-Options: {x_frame_options}, CSP: {csp})"

        print(f"[{url}] -> {result}")

    except requests.RequestException as e:
        print(f"[{url}] -> ERROR: {e}")

def main():
    input_file = "urls.txt"
    
    try:
        with open(input_file, "r") as file:
            urls = file.read().splitlines()

        for url in urls:
            if not url.startswith("http"):
                http_url = f"http://{url}"
                https_url = f"https://{url}"
                check_clickjacking(http_url)
                check_clickjacking(https_url)
            else:
                check_clickjacking(url)

    except FileNotFoundError:
        print(f"ERROR: {input_file} not found.")

if __name__ == "__main__":
    main()
