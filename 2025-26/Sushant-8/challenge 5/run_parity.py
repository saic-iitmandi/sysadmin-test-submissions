import re

data=open("words.txt").read()
seq=re.findall(r"\b[a-z]{4}\b", data)

# keep only vocab-like words (optional)
vocab=set("coin gate path lake leaf star wave rain sand fire snow wall pool rock lamp book moon boat bird fork road tree seed wind roof door desk fish".split())
seq=[w for w in seq if w in vocab]

# --- RUN PARITY ---
bits=""
i=0
while i<len(seq):
    j=i
    while j<len(seq) and seq[j]==seq[i]:
        j+=1
    run=j-i

    bits += "1" if run%2==1 else "0"
    i=j

print("Total bits:",len(bits))

out=""
for k in range(0,len(bits)-8,8):
    try:
        out+=chr(int(bits[k:k+8],2))
    except:
        break

print(out[:300])
print("SAIC index:",out.find("SAIC"))
