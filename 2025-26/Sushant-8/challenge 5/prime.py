import re, math

data=open("words.txt").read()
seq=re.findall(r"\b[a-z]{4}\b", data)

vocab=set("coin gate path lake leaf star wave rain sand fire snow wall pool rock lamp book moon boat bird fork road tree seed wind roof door desk fish".split())
seq=[w for w in seq if w in vocab]

def is_prime(n):
    if n<2: return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0: return False
    return True

out=""
for i,w in enumerate(seq,1):
    if is_prime(i):
        out+=w[0]

print(out[:300])
print("SAIC index:", out.find("SAIC"))

