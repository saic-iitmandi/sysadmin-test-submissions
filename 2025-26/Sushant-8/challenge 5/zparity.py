data=open("payload.zlib","rb").read()

# Use MSB parity of each byte
bits="".join(str(b&1) for b in data)


out=""
for i in range(0,len(bits)-8,8):
    out+=chr(int(bits[i:i+8],2))

print(out[:300])
print("SAIC index:", out.find("SAIC"))