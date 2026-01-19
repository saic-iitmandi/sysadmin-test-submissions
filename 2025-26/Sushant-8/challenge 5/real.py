data=open("payload.bin","rb").read()

bits="".join(str(b&1) for b in data)

out=""
for i in range(0,len(bits)-8,8):
    out+=chr(int(bits[i:i+8],2))

print(out[:400])
print("SAIC index:",out.find("SAIC"))
