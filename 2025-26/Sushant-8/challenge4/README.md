# Challenge 4 – The Bakery’s Secret Recipe

## FLAG  
`SAIC{ev3n_l0g5_cAn_l13_tRu5t_n0_0n3}`  

hehe, i am very happy to find this flag because i felt like giving up at one time because i couldn't find the RSA parameters

---

## now here goes the story

downloaded the repo, got a folder then opened it in a terminal using

```bash
ls -la
```

only 2 normal files were available (i know such a childish attempt but still)

then i checked for hidden references because there was no flag available normally, that got me to explore the opportunity in git internals:

```bash
cat .git/info/refs
```

there i got 3 additional refs:

```
a3e00065651d7bb9a54c10a9157696e07903ebac  refs/archive/merged  
9c89d2e4fffee48411b9fa62a30994ad1c69e05a  refs/heads/main  
63570471b6d86a7c63ddb2fc3dd5d55da624e1ea  refs/tags/archive-tag
```

they were not part of the normal history, so it was certain that i had inspect them, then i used:

```bash
git ls-tree -r <commit-hash>
git cat-file -p <blob-hash>
```

read the `.env` file (because .env file is the place where developers keep secrests such as passwords, here we found it so it ought to be exploited)

```bash
git cat-file -p 9005f7170a1a0f3afdc784a07f8d360c635d1f55
```

```
our super special secret ingredients
n = 13081
e = 19
Updated: Jan 2026
```

now it was certain that flag was encrypted using RSA and the keys are to be found in git history

Another hidden commit (`63570471b6d86a7c63ddb2fc3dd5d55da624e1ea`) contained:

- baked_goods.txt – a list of numbers  
- oven.py – the encryption code  

i used:

```bash
git ls-tree -r 63570471b6d86a7c63ddb2fc3dd5d55da624e1ea
```

i opened them using `git cat-file -p`

### baked_goods.txt gave me a cypher text:

```
[8186, 10208, 3632, 12587, 12311, 8428, 6333, 864, 6786, 12811, 5442,
7245, 103, 2626, 12811, 2766, 10208, 6786, 12811, 5442, 11474, 864,
12811, 1817, 7514, 7921, 2626, 1817, 12811, 6786, 7245, 12811, 7245,
6786, 864, 8477]
```

### oven.py gave me this:

```python
#import ingredients
n = p*q
m = flag.encode()
cypher = [pow(b, e, n) for b in m] #we like our cookies chunky
#and the cookies are ready!!
```

by now it was clear that i am very close to solution and each character of the flag was encrypted using RSA formula  
`c = m^e mod n`

---

## so now i followed the standard RSA decryption steps

- Factorized n → 103 × 127  
- Computed φ(n)  
- Found private key d = e⁻¹ mod φ(n)  
- Decrypted each number using pow(c, d, n)

---

## i exactly used this python session

```python
>>> def find_d(e, n):
...     p, q = 103, 127
...     phi = (p - 1) * (q - 1)
...     # This finds the modular inverse
...     return pow(e, -1, phi)
...
>>> n = 13081
>>> e = 19
>>> d = find_d(e, n)

>>> cipher = [8186, 10208, 3632, 12587, 12311, 8428, 6333, 864, 6786, 12811,
... 5442, 7245, 103, 2626, 12811, 2766, 10208, 6786, 12811, 5442, 11474,
... 864, 12811, 1817, 7514, 7921, 2626, 1817, 12811, 6786, 7245, 12811,
... 7245, 6786, 864, 8477]

>>> flag = "".join([chr(pow(c, d, n)) for c in cipher])
>>> print(flag)
SAIC{ev3n_l0g5_cAn_l13_tRu5t_n0_0n3}
```

and hence i got the flag

---

## Challenges Faced

there were many challenges such as:

- i was toying around `git grep "SAIC"` but it returned nothing  
- i also didn't knew it was a RSA problem until i used LLMs  
- my first decryption attempt also produced some flag in ancient language which were completely wrong

