def solve_index_parity():
    with open('clean_words.txt', 'r') as f:
        words = [line.strip() for line in f if line.strip()]

    # We check the parity of the index for EACH column (1-4)
    # e.g., 'a' is 1 (Odd), 'b' is 2 (Even)
    for col in range(4):
        bits = "".join(['1' if (ord(w[col].lower()) - 96) % 2 != 0 else '0' for w in words])
        
        for bit_len in [7, 8]:
            for shift in range(8):
                stream = bits[shift:]
                decoded = ""
                for i in range(0, len(stream), bit_len):
                    chunk = stream[i:i+bit_len]
                    if len(chunk) == bit_len:
                        val = int(chunk, 2)
                        decoded += chr(val % 128) if 31 < (val % 128) < 127 else "."
                
                if "SAIC" in decoded.upper():
                    print(f"🚩 FLAG FOUND IN COLUMN {col+1}!")
                    print(f"Result: {decoded}")
                    return

    # If that fails, try the SUM of the word's indices
    bits_sum = "".join(['1' if sum(ord(c)-96 for c in w) % 2 != 0 else '0' for w in words])
    # ... check bits_sum with the same bit_len/shift loops ...
    print("Checking Word-Index Sum Parity...")
    for bit_len in [7, 8]:
        for shift in range(8):
            stream = bits_sum[shift:]
            decoded = "".join(chr(int(stream[i:i+bit_len], 2)%128) for i in range(0, len(stream)-bit_len, bit_len))
            if "SAIC" in decoded.upper():
                print(f"🚩 FLAG FOUND IN INDEX SUM!")
                print(decoded)
                return

solve_index_parity()