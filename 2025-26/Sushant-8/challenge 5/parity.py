f=open("final.png","rb").read()
bits="".join(str(b&1) for b in f)

def decode(parity,pos):
    out=[]
    for i in range(0,len(bits)-8,8):
        b=bits[i:i+8]

        if parity=="odd" and b.count("1")%2!=1: continue
        if parity=="even" and b.count("1")%2!=0: continue

        c=b[1:] if pos=="first" else b[:-1]

        try:
            ch=chr(int(c,2))
            if 32<=ord(ch)<=126:
                out.append(ch)
            else:
                out.append(".")
        except:
            pass
    return "".join(out)

for p in ["odd","even"]:
    for pos in ["first","last"]:
        r=decode(p,pos)
        if "SAIC" in r:
            print("\nFOUND with:",p,pos)
            i=r.index("SAIC")
            print(r[i:i+120])
