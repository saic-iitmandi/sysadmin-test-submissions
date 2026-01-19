from PIL import Image
import numpy as np

img = Image.open("final.png").convert("RGB")
pixels = np.array(img)

bits = []

for pixel in pixels.reshape(-1, 3):
    r, g, b = pixel
    bits.append(str((r + g + b) % 2))

flag = ""
for i in range(0, len(bits), 8):
    byte = bits[i:i+8]
    if len(byte) < 8:
        break
    value = int("".join(byte), 2)
    if 32 <= value <= 126:
        flag += chr(value)

print(flag)
