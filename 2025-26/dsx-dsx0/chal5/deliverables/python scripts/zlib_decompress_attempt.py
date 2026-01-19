# zlib_decompress_attempt.py
# Attempt to decompress decoded binary data using zlib

import zlib

data = open("stage2.bin", "rb").read()

try:
    decompressed = zlib.decompress(data)
    print("Decompression successful")
    print("Length:", len(decompressed))

    with open("final_output.bin", "wb") as f:
        f.write(decompressed)

    print(decompressed[:500].decode(errors="ignore"))

except zlib.error as e:
    print("Zlib decompression failed:", e)
