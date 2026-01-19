1. Initial Analysis (The Dead End)
I started by throwing standard image analysis tools at final.png.

StegSolve: I cycled through every bit-plane filter (Red, Green, Blue, Alpha). Results? Pure garbage noise.

Strings: Checked for hidden ASCII. Nothing useful.

Binwalk: Checked for hidden embedded files. Clean.

2. The Breakthrough: LSB Extraction
I switched to Linux and used zsteg, a more aggressive steganography tool for PNGs.

Command: zsteg -a final.png

The Hit: The tool flagged hidden data in the b1,rgb,lsb,xy channel.

The Artifact: P0xCB3Ee24c30718F2De29fccfB012f778363e1a06A96

3. Decoding the "Hash"
At first glance, this looked like some weird hash.

Analysis:

It started with 0x (Hexadecimal).

It was 42 characters long (ignoring the P).

The mix of uppercase and lowercase letters (Ee, De) was too specific to be random.

Realization: This is an Ethereum Address (which uses mixed-case checksums).

Cleanup: I stripped the prefix P (likely "Pointer" or "Public") and the trailing 96 (likely noise from the extraction).

Target Address: 0xCB3Ee24c30718F2De29fccfB012f778363e1a06A

4. Blockchain Forensics
Since the address was valid, I knew the flag wasn't in the image anymore—it was on the chain. I checked the Sepolia Testnet (standard for CTFs) on Etherscan.

The Discovery: The address wasn't a wallet; it was a Smart Contract.

The Origin: It was created 8 days ago by a specific transaction (0x04df3e5...).

The Paydirt: I inspected the Input Data of that creation transaction.

5. Recovering the Flag
The "Input Data" field contained the compiled bytecode for the contract.

Decoding: I switched the view to UTF-8 and scanned the messy text.

The Find: Buried at the end of the metadata was the flag in plain text.

Final Flag: SAIC{M4YB3_Y0U_4R3_TH3_83ST}