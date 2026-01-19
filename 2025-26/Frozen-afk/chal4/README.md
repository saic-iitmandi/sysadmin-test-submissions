# Challenge 4

**January 18, 2026**

---

## 1. Executive Summary

The target environment contained a hidden version control directory (.git). The objective was to
identify sensitive logic hidden in the development history and decrypt the protected flag.

Since I am new to Git forensics and cryptography, I relied on searching for specific error messages
and code patterns to guide my investigation. This process led me to discover hidden commits and
eventually identify a mathematical vulnerability in the recovered script.

---

## 2. Phase 1: Git Forensics (The Hunt)

### 2.1 Identifying the “Missing” History

The Logic: I listed the files and saw nothing interesting, but I noticed a .git folder. I searched online
to check if the presence of this folder meant there were other files hidden in the directory. The search
results confirmed that a .git folder contains the entire history of the project, meaning files could be
hidden or deleted.

Research Query: “how to access hidden files in .git folder”

Action: After realizing the data was likely there but hidden, I searched for the specific commands
to access it. The results recommended using git fsck, which checks the database for orphaned objects.

git fsck --lost -found

Discovery: This command recovered several "dangling blobs." By inspecting them one by one, I
found a deleted Python script named oven.py.

---

### 2.2 Digging into Metadata (.env)

The Logic: The script I found referenced variables that weren’t defined in the code. I suspected
they might be hidden in configuration files or other commits. I checked the logs to see if anything was
missed.

Research Query: “git log show file changes status”

Action: I ran git log –stat and saw a commit titled “merge recipe parameters” . This
seemed suspicious because "parameters" usually implies configuration data.

Recovery: I checked the content of that specific commit and found a hidden .env file containing
the variables n and e.

---

## 3. Phase 2: Cryptographic Analysis (The Pattern)

### 3.1 Recognizing the RSA Pattern

The Logic: Inside oven.py, there was a line of code: pow(b, e, n). I had never seen this used for
encryption before, so I searched for what this function does in a security context.

Research Query: “python pow(b,e,n) encryption algorithm”

Conclusion: The search results explained that this specific mathematical operation is the core of
the **RSA Algorithm**.

• I learned that n and e are the "Public Keys" (which matched the variables I found in the .env
file).

• The list of numbers in baked_goods.txt was the encrypted message.

• To decrypt it, I learned I needed a "Private Key" (d), which requires factoring n.

---

### 3.2 Vulnerability Assessment (Weak Encryption)

The Logic: I read that RSA is usually very secure because n is a huge number. However, the n I
found (13081) looked very small compared to the examples online.

Research Query: “how to crack RSA with small n”

Analysis: The search results confirmed that if n is small, you don’t need supercomputers to crack
it—you just need to find its prime factors.

Conclusion: This confirmed the vulnerability: the key was too small to be secure.

---

## 4. Phase 3: Exploitation & Decryption

To decrypt the message, I followed a tutorial on how to calculate the private key (d) once you have
the factors of n.

### 4.1 Factoring the Modulus

Command:

factor 13081

Result: 13081: 103 127

Derivation: This gave me the two prime numbers p = 103 and q = 127.

---

### 4.2 Private Key Calculation

I used an online calculator (and verified with Python) to perform the standard RSA math:

• Euler’s Totient (ϕ): Calculated as (p− 1)(q − 1) = 102× 126 = 12852.

• Private Exponent (d): Calculated as the modular inverse of e (mod ϕ).

---

### 4.3 Final Decryption

I generated the Python decoding script from ChatGPT using the formula m = cd (mod n) and the
list of encrypted numbers. I ran that script, which converted the numbers back into text.

---

## 5. Conclusion

Flag Recovered:

SAIC{ev3n_l0g5_cAn_l13_tRu5t_n0_0n3}

---

## Table of Contents

- Executive Summary
- Phase 1: Git Forensics (The Hunt)
- Identifying the “Missing” History
- Digging into Metadata (.env)
- Phase 2: Cryptographic Analysis (The Pattern)
- Recognizing the RSA Pattern
- Vulnerability Assessment (Weak Encryption)
- Phase 3: Exploitation & Decryption
- Factoring the Modulus
- Private Key Calculation
- Final Decryption
- Conclusion
