vocab = set("coin gate path lake leaf star wave rain sand fire snow wall pool rock lamp book moon boat bird fork road tree seed wind roof door desk fish".split())

bits = []

prev = None
run = 0

with open("words.txt") as f:
    for token in f.read().split():
        if token not in vocab:
            continue

        if token == prev:
            run += 1
        else:
            if prev is not None:
                bits.append("1" if run % 2 == 1 else "0")
            prev = token
            run = 1

# last run
if prev:
    bits.append("1" if run % 2 == 1 else "0")

bits = "".join(bits)

print("Bits collected:", len(bits))

out = ""
for i in range(0, len(bits)-8, 8):
    try:
        out += chr(int(bits[i:i+8],2))
    except:
        break

print(out[:300])
print("SAIC index:", out.find("SAIC"))
