Objective:
The objective of this challenge was to analyze an image file suspected of containing hidden information and attempt to extract and decode the concealed data using systematic inspection and reverse-engineering techniques.

Tools Used:
1. Operating System: Ubuntu Linux
2. exiftool – for extracting image metadata
3. pngcheck – for validating PNG structure and identifying chunk types
4. GNU coreutils (grep, sort, uniq, awk, wc, tr) – for large-scale text processing and statistical analysis
5. Python 3 – for scripting custom decoding and decompression logic
6. zlib (Python standard library) – for decompression attempts

Methodology and Attempts:

1. Initial File Validation
The image was first validated using the `file` utility and `pngcheck -v`. This confirmed the file to be a valid PNG image with standard IHDR, IDAT, and IEND chunks. Importantly, a very large `zTXt` chunk with the keyword “Description” was identified, indicating compressed textual metadata embedded within the PNG.

2. Metadata Extraction
Using `exiftool`, the contents of the `Description` field were extracted. The extracted data consisted of an extremely large sequence of English words (millions of tokens), suggesting that the data was not intended to be human-readable but rather encoded.

The metadata was saved to a separate file (`words.txt`) to allow structured analysis without terminal overflow.

3. Vocabulary and Structural Analysis
Statistical analysis of the extracted words revealed:
- Approximately 8.9 million total word tokens.
- 843 unique words overall.
- A subset of words appeared in the format `word..word`, occurring only ~3000 times.
- The overwhelming majority of tokens were single words.

This strongly suggested that:
- Single words formed the main encoded data stream.
- The `word..word` pairs were auxiliary data, possibly defining mappings, ordering, or metadata.

4. Frequency Analysis
A frequency count of single words showed a clear separation:
- A small group of 28 words appeared with very high and nearly uniform frequency (~214k occurrences each).
- Remaining words appeared far less frequently and were interpreted as padding, noise, or structural markers.

The 28 high-frequency words were isolated and treated as the true encoding alphabet:
bird, boat, book, coin, desk, door, fire, fish, fork, gate,
lake, lamp, leaf, moon, path, pool, rain, road, rock, roof,
sand, seed, snow, star, tree, wall, wave, wind

5. Hypothesis: Base-N Word Encoding
Based on the uniform distribution and fixed vocabulary size, it was hypothesized that:
- Each of the 28 words represents a digit in a base-28 number system.
- The overall word stream encodes binary data via positional base-28 values.

6. Decoding Attempts (Python)
A custom Python script was written to:
- Filter out non-payload words.
- Map the 28 core words to numeric values.
- Convert sequences of words into byte values.

Initial attempts grouped 3 base-28 symbols per byte (with modulo reduction). This produced high-entropy binary output but did not cleanly decompress.

7. Evidence of Secondary Compression
Despite decode failure, partial byte inspection showed patterns consistent with compressed binary data. Notably, byte sequences resembling zlib headers (e.g., `0x78 0x9c`) appeared during early decoding attempts, suggesting that the word stream decoded into another compressed layer.

8. Decompression Attempts
The decoded binary output was saved to a file (`stage2.bin`) and tested using Python’s zlib decompression routines. Decompression failed with an “incorrect header check” error, indicating either:
- Misalignment of the compressed stream,
- Incorrect symbol grouping, or
- An additional wrapper/header preceding the compressed data.

Header scanning for standard zlib signatures did not yield a valid offset before time constraints expired.

Conclusion and Current State:
The challenge was not fully solved within the allotted time. However, the investigation conclusively established that:
- The image hides data within a PNG `zTXt` metadata chunk.
- The metadata contains a large-scale word-encoded payload.
- The payload uses a fixed 28-word alphabet with uniform frequency, strongly indicating base-28 encoding.
- The decoded output appears to contain a secondary compressed (zlib-like) data layer.
- Remaining work would involve refining symbol grouping and alignment to correctly extract and decompress the final payload.
