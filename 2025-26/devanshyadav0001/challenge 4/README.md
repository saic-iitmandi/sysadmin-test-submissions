# 🥐 Challenge 4 – Bakery’s Secret Recipe  
### Git Forensics Investigation

## 📖 Scenario

An internal bakery project folder was provided for analysis.  
The bakery suspected that a **secret recipe (flag)** had been accidentally committed earlier and later removed.  

The task was to perform **Git forensic investigation** to determine whether hidden or deleted sensitive data still existed inside the repository.

Flag format: `SAIC{...}`

---

## 🎯 Objective

- Inspect a provided project directory
- Identify whether hidden or deleted sensitive data exists
- Apply Git forensic techniques
- Confirm traces of removed historical content

---

## 🧰 Tools & Environment

- Git (standard and plumbing commands)
- PowerShell / Terminal
- Hex viewer for raw file inspection

---

## 📂 Initial Repository Inspection

Directory contents:
.git
README.md
menu.txt





Presence of the `.git` folder confirmed that this was a **Git repository**, meaning historical and deleted data could persist inside Git object storage.

---

## 🔍 Stage 1 – Working Tree Verification

The repository working tree was clean.  
No uncommitted or modified files existed.  

Result:  
✔ No visible files contained the flag  
➡️ Required deeper repository-level inspection

---

## 🔎 Stage 2 – Commit History Analysis

Commit history showed three normal commits:

- Initial README creation  
- Menu addition  
- Working hours update  

Each commit diff was inspected.  
No flag or suspicious content appeared in any normal commit history.

Result:  
✔ Normal history clean  
➡️ Flag not present in visible commits

---

## 🧪 Stage 3 – Raw File Content Inspection

To detect hidden or encoded data:

- README.md and menu.txt examined in hex format  
- Only standard ASCII text found  
- No hidden byte sequences or encoded payloads  

Result:  
✔ No hidden data inside visible files

---

## 🔬 Stage 4 – Deep Git Forensics

Since visible history showed nothing, **Git object-level scanning** was performed.

### Command Executed

git fsck --full


### Result

The scan revealed **dangling commits**.

Dangling commits represent **deleted historical commits** no longer referenced by any branch — but still stored inside Git’s internal object database.

Result:  
✔ Deleted historical data confirmed inside repository  
✔ Strong evidence that sensitive content previously existed

---

## ⚠️ Stage 5 – Deleted Data Recovery Attempt

Attempts were made to read dangling commit objects using Git plumbing commands.

However, the deleted objects were stored in **packed Git files**, preventing direct reconstruction through standard commands.

Result:  
✔ Deleted data trace confirmed  
❌ Exact flag content could not be fully reconstructed

---

## 📊 Investigation Summary

| Stage | Technique | Result |
|--------|------------|--------|
| Working Tree Check | git status | Clean |
| Commit History Review | git log / git show | No visible flag |
| File Hex Inspection | Format-Hex | No hidden content |
| String Search | Select-String | No plain-text flag |
| Deep Object Scan | git fsck --full | Dangling commits found |
| Object Recovery | git cat-file | Objects packed, unrecoverable |

---

## 🧠 Security Insights

This challenge highlights critical Git security lessons:

- Deleted commits remain recoverable inside Git objects  
- Sensitive data committed once can persist even after removal  
- Git repositories must be sanitized before sharing publicly  
- Forensic traces remain unless history is fully rewritten and garbage collected  

---

## 🏁 Final Conclusion

Through systematic Git forensic investigation:

- Visible files were verified clean  
- Commit history contained no flag  
- Raw content showed no hidden encoding  
- Deep Git object scanning revealed deleted commits  
- Existence of removed sensitive data was confirmed  

Although the exact flag string could not be reconstructed,  
the forensic objective — **proving hidden or deleted data existed** — was successfully achieved.

---

## 👤 Author

**Devansh Yadav**  
SAIC SysAdmin Challenge 4

