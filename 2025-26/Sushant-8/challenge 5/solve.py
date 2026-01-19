import re

# Load cleaned words
data = open("words.txt").read()
words = re.findall(r"\b[a-z]{4}\b", data)

# Keep only vocabulary words
vocab = set("coin gate path lake leaf star wave rain sand fire snow wall pool rock lamp book moon boat bird fork road tree seed wind roof door desk fish".split())

segment = [w for w in words if w in vocab]

def bit_from_word(w):
    total = 0
    for ch in w:
        total += format(ord(ch), "08b").count("1")
    return "1" if total % 2 == 1 else "0"

bits = "".join(bit_from_word(w) for w in segment)

out = ""
for i in range(0, len(bits)-8, 8):
    out += chr(int(bits[i:i+8], 2))

print(out[:300])
print("\n---- SEARCH ----")
i = out.find("SAIC")
print(out[i:i+120])
