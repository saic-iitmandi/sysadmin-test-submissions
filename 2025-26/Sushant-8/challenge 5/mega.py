import re, string

data = open("words.txt").read()
words = re.findall(r"\b[a-z]{4}\b", data)

vocab = set("coin gate path lake leaf star wave rain sand fire snow wall pool rock lamp book moon boat bird fork road tree seed wind roof door desk fish".split())
seq = [w for w in words if w in vocab]

print("Using words:", len(seq))

vowels="aeiou"
holes=set("abdegopqr")
left=set("qwertasdfgzxcvb")   # keyboard left side

def scrabble(w):
    score=0
    table={"a":1,"e":1,"i":1,"o":1,"u":1,"l":1,"n":1,"s":1,"t":1,"r":1,
           "d":2,"g":2,"b":3,"c":3,"m":3,"p":3,"f":4,"h":4,"v":4,"w":4,"y":4,
           "k":5,"j":8,"x":8,"q":10,"z":10}
    for c in w: score+=table[c]
    return score

def ascii1(w): return sum(ord(c) for c in w)
def alpha(w):  return sum(ord(c)-96 for c in w)
def vowel(w):  return sum(c in vowels for c in w)
def hole(w):   return sum(c in holes for c in w)
def leftk(w):  return sum(c in left for c in w)

modes={
 "ascii-sum":ascii1,
 "alpha-sum":alpha,
 "vowel":vowel,
 "hole":hole,
 "scrabble":scrabble,
 "keyboard":leftk,
}

def try_decode(bits,name):
    out=""
    for i in range(0,len(bits)-8,8):
        try:
            c=chr(int(bits[i:i+8],2))
            out+=c if 32<=ord(c)<=126 else "."
        except:
            break

    if "SAIC" in out:
        i=out.index("SAIC")
        print("\n>>> FOUND with",name)
        print(out[i:i+120])
        return True
    return False


# ----- BRUTE -----
for name,f in modes.items():
    bits="".join("1" if f(w)%2 else "0" for w in seq)
    if try_decode(bits,name):
        exit()

# also try position based
bits="".join("1" if i%2 else "0" for i,_ in enumerate(seq))
try_decode(bits,"position-parity")

print("No hit yet")
