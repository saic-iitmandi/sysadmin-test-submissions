# Challenge 5

**January 18, 2026**

---

## 1. Executive Summary

The target artifact was a PNG image file named final.png. Initial checks for hidden files or metadata
yielded no results. The objective was to uncover hidden data embedded within the image itself.

Since I am not an expert in image forensics, I relied on automated tools found via Google. When the
primary tool crashed, I had to research specific error messages to find a workaround, which eventually
led me to manually extract and decode the flag.

---

## 2. Phase 1: Structural Analysis (The Dead End)

### 2.1 Metadata & Embedded Files

The Logic: I had an image file but no idea where the flag was. I searched for the most common ways
flags are hidden in images for beginners. The results suggested checking for metadata or hidden files
appended to the end.

Research Query: “how to check hidden files inside png or jpg”

Action: I ran the recommended tools exiftool (for metadata) and binwalk (for hidden files).

exiftool final.png
binwalk -e final.png

Observation:

• exiftool showed standard info but no hidden text.

• binwalk showed “Zlib compressed data,” but my research indicated this is just a normal part of
the PNG file format, not a hidden file.

Conclusion: The flag wasn’t attached to the file; it was likely hidden inside the pixel data.

---

## 3. Phase 2: The Tool Failure (The Crash)

### 3.1 Automated Analysis with zsteg

The Logic: Since the file structure was clean, I searched for "steganography tools linux". The most
popular result was zsteg, which is supposed to automatically find hidden data.

Research Query: “best tools for png lsb steganography”

Action: I installed and ran the tool.

zsteg -a final.png

The Obstacle: The tool started printing weird binary code and then suddenly crashed with a
SystemStackError: stack level too deep.

The Pivot: I didn’t know what this error meant, so I copied the error message into Google. The
results suggested that the tool was running out of memory while trying to scan everything at once.
The forums suggested extracting specific "bit planes" manually instead of letting the tool guess.

---

## 4. Phase 3: Manual Extraction (The Workaround)

### 4.1 Carving the Bit Planes

The Logic: Following the advice I found online, I tried to extract the data from the "Red" color
channel specifically, hoping the flag was there.

Action: I used the command found in the documentation to extract just the Red LSB plane.

zsteg -E "b1,r,lsb ,xy" final.png > red_plane.bin

---

### 4.2 Hexadecimal Analysis

The Logic: I tried to read the file using cat, but it was a mess of weird symbols. I searched for how
to look at the raw code of a binary file.

Research Query: “how to view raw hex of a binary file linux”

Action: The search recommended using xxd or hexdump.

head -c 64 red_plane.bin | xxd

Discovery: The hex dump revealed a pattern. Amidst the zeros, I saw readable characters like V,
F, R, etc.

00000000: 0042 3216 5646 5216 5230 4627 4776 ... .B2.VFR.R0F’Gv

Pattern Recognition: I didn’t recognize the string immediately, but it looked like a code. I put
the visible characters into a search engine/decoder, and it looked very similar to Base64 (which I had
seen in previous challenges), just cluttered with extra bytes.

---

## 5. Phase 4: Decoding & Solution

### 5.1 Reconstructing the Payload

The Logic: The raw data had "garbage" characters mixed with the text. I manually copied the
readable letters to form a clean string.

---

### 5.2 Final Decode

I took the cleaned-up string and passed it to a Base64 decoder.

echo "U0FJQ3tmbDRnXzFzX2gzcmV9" | base64 -d

---

## 6. Conclusion

Flag Recovered:

SAIC{fl4g_1s_h3re}

By manually extracting the data when the automated tool crashed, and by identifying the Base64
pattern in the raw file, I was able to recover the flag.

---

## Table of Contents

- Executive Summary
- Phase 1: Structural Analysis (The Dead End)
- Metadata & Embedded Files
- Phase 2: The Tool Failure (The Crash)
- Automated Analysis with zsteg
- Phase 3: Manual Extraction (The Workaround)
- Carving the Bit Planes
- Hexadecimal Analysis
- Phase 4: Decoding & Solution
- Reconstructing the Payload
- Final Decode
- Conclusion
