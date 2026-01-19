# 🖼️ Challenge 5 – Hidden Data Extraction from PNG  
### Binary Forensics Investigation

## 📖 Scenario

A PNG image file `final.png` was provided.  
Although it appeared to be a normal image, the challenge required verifying whether **hidden embedded data** existed inside the file and recovering a secret flag.

In CTF-style forensic tasks, image files often carry concealed payloads inside binary structures or metadata.  
Therefore, the image was analyzed as a **binary data container**, not just as a visual file.

---

## 🎯 Objective

- Analyze the provided PNG image
- Detect hidden embedded data
- Extract and reconstruct the secret flag

Expected flag format: `SAIC{...}`

---

## 🧰 Tools Used

- Binary string extraction utilities  
- Pattern-based text filtering  
- Manual inspection of extracted outputs  

---

## 🔍 Stage 1 – Raw Binary String Extraction

The PNG file was processed to extract all printable character sequences from its binary data.

Result:
- Large volume of unreadable and random strings
- Expected outcome due to PNG compression format

Conclusion:
✔ Binary data successfully dumped  
➡️ Required structured filtering to locate meaningful payload

---

## 🔎 Stage 2 – Pattern-Based Filtering

Since CTF flags typically contain curly braces `{ }`, extracted text was filtered to identify brace-enclosed sequences.

Result:
- Many brace patterns found
- Majority contained random or unreadable characters
- Identified as compression artifacts (false positives)

Conclusion:
✔ Noise patterns detected  
➡️ Required isolation of readable structured payload

---

## 🧪 Stage 3 – Meaningful Payload Isolation

Among all detected brace patterns, one short and fully readable sequence stood out:

{93F_z}


All other patterns contained corrupted or non-readable symbols, confirming `{93F_z}` as the intentional hidden payload.

---

## 🏁 Stage 4 – Flag Reconstruction

Using the standard challenge flag format:

SAIC{{93F_z}


This successfully reconstructed the hidden flag embedded inside the PNG binary structure.

---

## 📊 Investigation Summary

| Phase | Method | Result |
|--------|---------|--------|
| Binary Extraction | Printable string dump | Raw data extracted |
| Pattern Filtering | Brace-based search | Many false positives |
| Manual Inspection | Readable token isolation | `{93F_z}` identified |
| Flag Construction | Prefix reconstruction | `SAIC{93F_z}` recovered |

---

## 🧠 Security Insight

This challenge demonstrates:

- Image files can store hidden readable data inside binary chunks
- Simple string extraction can reveal concealed payloads
- Pattern filtering helps separate real data from compression noise
- Manual validation is essential in forensic workflows

---

## 🏁 Conclusion

Through systematic binary forensic analysis:

- The PNG file was treated as a data container
- Hidden readable sequences were extracted
- Noise artifacts were filtered out
- A valid embedded payload was isolated
- The final flag was successfully reconstructed

This confirms the presence and successful extraction of hidden data from the image.

---

## 👤 Author

**Devansh Yadav**  
SAIC SysAdmin Challenge 5
