# zlib_header_scan.py
# Scan a binary file for possible zlib headers

data = open("stage2.bin", "rb").read()

zlib_headers = [
    b'\x78\x01',
    b'\x78\x9c',
    b'\x78\xda'
]

for i in range(0, 200):
    if data[i:i+2] in zlib_headers:
        print("Possible zlib header at offset", i, data[i:i+2])
