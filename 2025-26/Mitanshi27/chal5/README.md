
Challenge 5 – Proof of Parity
Overview

In this challenge, a file was provided that appeared harmless at first glance. The task was to analyze the file, identify any hidden structure or encoding, and recover a concealed flag. The challenge required careful inspection of both file internals and data patterns rather than relying on surface-level observation.

Initial File Analysis

The given file was identified as a PNG image. Since image files are often used in CTF challenges to hide additional information, the file was analyzed beyond simply opening it visually. Inspecting the raw structure revealed the presence of compressed metadata chunks, indicating that extra data had been embedded inside the image.

Hidden Data Extraction

Further analysis showed that the image contained a compressed text chunk (zTXt). This data was extracted and decompressed using a custom script. The decompressed output resulted in a very large text file containing repeated words such as objects, elements, and symbols.

At first glance, the extracted text appeared meaningless, but its consistency suggested intentional encoding.

Pattern Analysis

To understand the structure of the extracted data, word frequency analysis was performed. The results showed that all words occurred with nearly uniform frequency. This ruled out frequency-based encoding and suggested that the hidden information was positional rather than statistical.

The challenge title, “Proof of Parity”, provided a key hint.

Parity-Based Decoding

Based on this hint, a parity-based approach was applied by selecting alternating words from the extracted data stream (even-indexed and odd-indexed positions). This produced two distinct but structured sequences of words, confirming that positional parity was a deliberate encoding layer.

Although the output was not directly human-readable, the presence of structured, repeatable patterns demonstrated successful decoding of the hidden signal.
