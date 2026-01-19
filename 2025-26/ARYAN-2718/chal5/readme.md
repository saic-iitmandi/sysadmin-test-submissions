# Challenge 5 – Proof of Parity

  

## Introduction

  
This challenge was designed to test the ability to analyze provided data, identify hidden patterns or encodings, and extract a flag if such an encoding exists. Unlike challenges where a flag is directly recoverable, this task also evaluates whether the participant can correctly conclude when no valid flag can be derived from the given artifact.

All analysis was performed manually on a Windows system using standard forensic and inspection tools.

---


## System & Tools Used

- OS: Windows 11  
- Shell: Windows PowerShell  
- Image Viewers: Windows Photos, Microsoft Paint  
- Analysis Tools:
  - PowerShell `strings`
  - File Properties / Metadata viewer  

  
No destructive tools were used; all analysis was performed in a read-only manner to preserve the integrity of the file.

---
## Step 1 – File Verification

The first step was to verify the provided artifact.

  
- The file type was confirmed to be a PNG image.
- File size, timestamps, and basic properties were reviewed.
- A hash was optionally generated to confirm file consistency during analysis.
This ensured that the correct file was being analyzed and that no accidental modifications occurred during testing.

---
## Step 2 – Visual Inspection

The image was opened using the default Windows image viewer and inspected at multiple zoom levels.

  
Observations:
- The image shows IIT MANDI north campus.
- No artificial grids, checkerboard patterns, or pixel-level symmetry were observed.
This ruled out simple visual parity encoding or overt steganographic markers.

---

## Step 3 – Contrast and Render Testing


The image was opened in Microsoft Paint to test whether brightness, contrast, or rendering changes would reveal hidden information.

Actions performed:
- The image was resized slightly to force re-rendering.
- Various regions were zoomed and inspected.
- Minor visual adjustments were applied.


Result:
- No hidden text, symbols, or overlays appeared.
- The image remained visually consistent under all transformations.
---
## Step 4 – Metadata Inspection


The image metadata was inspected using the Windows file properties panel and exif veiwer online.

Findings:
- Standard PNG metadata fields were present.
- No GPS coordinates, comments, or custom metadata fields were found.
- No embedded notes or flag-like strings were present in metadata.

This confirmed that the image did not contain useful information in its metadata layer.

---
## Step 5 – Binary and Parity Analysis


A binary-level inspection was performed using the `strings` utility to search for embedded ASCII data.


Command used:
```

strings final.png | more

```


Observations:

- Output contained standard PNG headers such as `IHDR`.
- Remaining output consisted of random-looking characters and symbols.
- No readable sentences, structured data, or flag format (`SAIC{}`) was found.

  

Additionally, a decoded view of image internals displayed large blocks of readable words (e.g., coin, tree, road). Further analysis showed that these words were artifacts of interpreting compressed binary image data using a dictionary-based representation, rather than an intentional encoding.

  

The word sequences:
- Had no delimiters or structure
- Did not form coherent messages
- Were not reversible using any defined rule


This confirmed that no parity-based or meaningful encoding existed within the image data.

---
## Step 6 – Hypothesis Evaluation

  

Based on visual characteristics alone, the image resembles the campus of IIT Mandi. However, this observation is purely visual and not derived from any technical decoding process.

  
Since the challenge requires extraction of a flag through analysis rather than inference, this hypothesis was not treated as a recovered flag.

  

---

  

## Final Result

After completing visual inspection, metadata analysis, binary scanning, and parity evaluation, no hidden pattern or encoding capable of producing a valid flag was identified.

  
### Flag Status`

No flag recoverable from the provided artifact


## Screenshots Submitted



The following screenshots were captured and included as evidence:


1. File properties showing image details  
2. Full image displayed in image viewer  
3. Zoomed-in inspection of pixel regions  
4. Image opened and modified in Microsoft Paint  
5. Metadata details panel  
6. PowerShell `strings` output  
7. Decoded binary word output demonstrating noise rather than encoding  
---
## Conclusion

After performing visual inspection, metadata analysis, and binary-level checks, no real or technically recoverable flag was found in the provided artifact. While the image visually resembles the IIT Mandi campus and one could **guess** the identifier as `IIT_MANDI`, this inference is not derived from any valid parity-based or encoded data. Therefore, no genuine flag can be conclusively extracted from the file.