# Challenge 4 - The Bakery’s Secret Recipe

## Challenge Description

As the administrator of SAIC’s public-facing server, you are responsible for auditing exposed files and services. During a routine inspection, you discover a directory belonging to a small internal bakery project.

The folder appears harmless at first glance, but may reveal sensitive information if investigated properly.

Your task is to analyze and recover the hidden flag.

### Objective

Investigate the provided folder.
Use forensics techniques to analyze the directory and extract the hidden flag.

## Detailed Process Description

Extracted and Opened the folder in WSL Ubuntu Environment

### Working Tree File Inspection

Commands:

```bash
cat README.md
cat menu.txt 
file ReadME.md
file menu.txt
```
Output:

```text

Cookie Bakery
Welcome to our bakery!
We make the best cookies in town!! Come have a look!
Hours: 9-5 PM

Today's Specials:
- Chocolate Chip
- Mystery Cookie

README.md: ASCII text

menu.txt: ASCII text
```
This Indicates that the files in working tree are clean with no hint or hidden information

### Repository Analysis

Commands:

```bash
git status
git log --all
```
Output:

```text
Author: = <=>
Date:   Fri Jan 9 07:57:24 2026 +0530

    update hours

commit 0c9b415b8bcf290a471df48b2dc255e1bb94f14d
Author: = <=>
Date:   Fri Jan 9 07:57:15 2026 +0530

    add menu

commit 9c89d2e4fffee48411b9fa62a30994ad1c69e05a
Author: = <=>
Date:   Fri Jan 9 07:45:08 2026 +0530

    the bakery is open
```

Commit history is clean, no suspicious commits

### Git Object Forensics

Command:

```bash
git fsck
```

Output:

```text
Checking object directories: 100% (256/256), done.
Checking objects: 100% (14/14), done.
dangling commit 63570471b6d86a7c63ddb2fc3dd5d55da624e1ea
dangling commit a3e00065651d7bb9a54c10a9157696e07903ebac
Verifying commits in commit graph: 100% (5/5), done.
```

This indicated the presence of dangling commits, which often retain deleted or rewritten data.
The data in the dangling commits can be revealed using

```bash
git show 63570471b6d86a7c63ddb2fc3dd5d55da624e1ea
git show a3e00065651d7bb9a54c10a9157696e07903ebac
```
Output:

```text
commit 63570471b6d86a7c63ddb2fc3dd5d55da624e1ea
Author: = <=>
Date:   Fri Jan 9 07:54:55 2026 +0530

    batch archive

diff --git a/baked_goods.txt b/baked_goods.txt
new file mode 100644
index 0000000..10432c2
--- /dev/null
+++ b/baked_goods.txt
@@ -0,0 +1 @@
+[8186, 10208, 3632, 12587, 12311, 8428, 6333, 864, 6786, 12811, 5442, 7245, 103, 2626, 12811, 2766, 10208, 6786, 12811, 5442, 11474, 864, 12811, 1817, 7514, 7921, 2626, 1817, 12811, 6786, 7245, 12811, 7245, 6786, 864, 8477]
diff --git a/oven.py b/oven.py
new file mode 100644
index 0000000..2111286
--- /dev/null
+++ b/oven.py
@@ -0,0 +1,5 @@
+#import ingredients
+n = p*q
+m = flag.encode()
+cypher = [pow(b, e, n) for b in m] #we like our cookies chunky
+#and the cookies are ready!!

commit a3e00065651d7bb9a54c10a9157696e07903ebac
Merge: 9c89d2e 47c8d89
Author: = <=>
Date:   Fri Jan 9 07:48:05 2026 +0530

    merge recipe parameters
```

this shows two files `baked_goods.txt` and `oven.py` along with 2 another hidden commits
`9c89d2e` and `47c8d89`

on revealing both `47c8d89` reveals values of n and e

Command:

```bash
git show 47c8d89
```

```text
our super special secret ingredients
n = 13081
e = 19
```

This Suggests that this is a RSA Key Encryption, this can be solved as explained below:

### RSA key Decryption

```text

n = 13081 is a product of 2 primes p and q, which can be solved to be
p = 127 and q = 103

further, euler's totient has to be solved for this:

Φ(n) = (p-1)(n-1)

Φ(n) = (126)(102)
Φ(n) = 12852

and also, we have a public key e = 19 which is co-prime with Φ(n) = 12852

```

this can be solved using a simple python program to automate decryption

```python
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
```
Output:

```text
SAIC{ev3n_l0g5_cAn_l13_tRu5t_n0_0n3}
```

## Conclusion:

Upon analyzing git objects, dangling or unreachable objects reveal the data encrypted using RSA key encryption along with .py script used for encryption and encryption keys

when decrypted, flag is obtained

Flag = SAIC{ev3n_l0g5_cAn_l13_tRu5t_n0_0n3}