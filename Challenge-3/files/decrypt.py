#decrypt.py

cypher = [8186, 10208, 3632, 12587, 12311, 8428, 6333, 864, 6786, 12811, 5442, 7245, 103, 2626, 12811, 2766, 10208, 6786, 12811, 5442, 11474, 864, 12811, 1817, 7514, 7921, 2626, 1817, 12811, 6786, 7245, 12811, 7245, 6786, 864, 8477]

n = 13081
e = 19


# m = flag.encode()
# cypher = [pow(b, e, n) for b in m]    this can be reversed in the following way:

# 19·d ≡ 1 (mod 12852)     d can be founded by solving the modular inverse of e mod φ(n) to be d ≡ 4735
d = 4735

flag = bytes([pow(c, d, n) for c in cypher])

flag = flag.decode()
print(flag)