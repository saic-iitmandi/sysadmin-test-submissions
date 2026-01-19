a = [8186, 10208, 3632, 12587, 12311, 8428, 6333, 864, 6786, 12811, 5442, 7245, 103, 2626, 12811, 2766, 10208, 6786, 12811, 5442, 11474, 864, 12811, 1817, 7514, 7921, 2626, 1817, 12811, 6786, 7245, 12811, 7245, 6786, 864, 8477] # got in baked__goods.txt
n = 13081 #RSA factors
e = 19
p = 103 #factored n
q = 127
phi = (p - 1) * (q - 1) #euler totient
def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    return g, y1, x1 - (a // b) * y1
def modinv(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        raise Exception("No modular inverse")
    return x % m
d = modinv(e, phi)
m = [pow(c, d, n) for c in a]  # Decrypting RSA (found this in oven.py)
flag = bytes(m).decode()
print("flag: ", flag)
