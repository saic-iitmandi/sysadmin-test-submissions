data=open("payload.bin","rb").read()

# collect bits from each byte
bits="".join(str(b&1) for b in data)

def decode(bits, reverse=False, offset=0):
    out=""
    b=bits[offset:]
    if reverse:
        b=b[::-1]

    for i in range(0,len(b)-8,8):
        try:
            c=chr(int(b[i:i+8],2))
            if 32<=ord(c)<=126:
                out+=c
            else:
                out+="."
        except:
            break
    return out


# Try ALL realistic modes
for rev in [False, True]:
    for off in range(0,8):
        r=decode(bits, rev, off)
        if "SAIC" in r:
            i=r.index("SAIC")
            print("\nFOUND rev=",rev,"off=",off)
            print(r[i:i+120])
            exit()

print("No hit yet")
