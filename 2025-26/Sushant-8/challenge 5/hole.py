holes = set("abdegopqr")

def bit(w):
    c = sum(ch in holes for ch in w)
    return "1" if c%2 else "0"

import re
data=open("words.txt").read()
seq=re.findall(r"\b[a-z]{4}\b", data)

bits="".join(bit(w) for w in seq)

out=""
for i in range(0,len(bits)-8,8):
    try:
        out+=chr(int(bits[i:i+8],2))
    except:
        break

print(out[:300])
print("SAIC index:", out.find("SAIC"))
