import re

data = open("words.txt").read()
words = re.findall(r"\b[a-z]{4}\b", data)

# Known vocabulary filter
vocab = set("coin gate path lake leaf star wave rain sand fire snow wall pool rock lamp book moon boat bird fork road tree seed wind roof door desk fish".split())

seq = [w for w in words if w in vocab]

print("Total valid words:", len(seq))


def try_bits(bits, name):
    out=""
    for i in range(0,len(bits)-8,8):
        try:
            c=chr(int(bits[i:i+8],2))
            if 32<=ord(c)<=126:
                out+=c
            else:
                out+="."
        except:
            break

    if "SAIC" in out:
        i=out.index("SAIC")
        print("\n=== FOUND with",name,"===")
        print(out[i:i+120])
        return True
    return False


# --- MODEL 1: vowel parity ---
v="aeiou"
bits="".join("1" if sum(c in v for c in w)%2 else "0" for w in seq)
try_bits(bits,"vowel parity")

# --- MODEL 2: ascii bit parity ---
def ascii_parity(w):
    t=0
    for ch in w:
        t+=format(ord(ch),"08b").count("1")
    return "1" if t%2 else "0"

bits="".join(ascii_parity(w) for w in seq)
try_bits(bits,"ascii parity")

# --- MODEL 3: alphabet sum parity ---
bits="".join("1" if sum(ord(c)-96 for c in w)%2 else "0" for w in seq)
try_bits(bits,"alpha-sum parity")

# --- MODEL 4: first-letter parity ---
bits="".join("1" if (ord(w[0])-96)%2 else "0" for w in seq)
try_bits(bits,"first-letter parity")

print("\nDone brute tests.")
