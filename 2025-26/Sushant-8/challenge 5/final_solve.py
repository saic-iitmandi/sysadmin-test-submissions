with open('acrostic_full.txt', 'r') as f:
    acrostic = f.read().strip()

hex_key = '5e50ad2d7a56f4952318c234ad2d4ade9181e91ac6928da929d690a5a75a561581ef4ac286ade96a9a95a0cd1a42158caf28d2b4a1294bda1484234ad2b6bda11ad455adad1a12b0bd2f4a0a00b5210ada0e549529534ab6ad215ad812ad2e085a10ac09'
key_bytes = bytes.fromhex(hex_key)

print(f"Scanning {len(acrostic)} characters with a {len(key_bytes)} byte key...")

for i in range(len(acrostic) - len(key_bytes)):
    decoded = ""
    for j in range(len(key_bytes)):
        # XORing each acrostic char with the corresponding key byte
        decoded += chr(ord(acrostic[i + j]) ^ key_bytes[j])
    
    if "SAIC" in decoded:
        print(f"\n[!!!] FLAG FOUND at index {i}:")
        print(decoded)
        break
    if i % 10000 == 0:
        print(f"Progress: {i}/{len(acrostic)}", end='\r')
