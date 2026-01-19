# decode_stage1_base28_3symbols.py
# First decoding attempt: 3 base-28 symbols -> 1 byte

alphabet = [
    "bird","boat","book","coin","desk","door","fire","fish","fork","gate",
    "lake","lamp","leaf","moon","path","pool","rain","road","rock","roof",
    "sand","seed","snow","star","tree","wall","wave","wind"
]

word_to_value = {word: i for i, word in enumerate(alphabet)}

decoded_bytes = bytearray()

with open("words.txt", "r") as f:
    words = f.read().split()

payload = [w for w in words if w in word_to_value]

for i in range(0, len(payload) - 2, 3):
    value = (
        word_to_value[payload[i]] * 28 * 28 +
        word_to_value[payload[i + 1]] * 28 +
        word_to_value[payload[i + 2]]
    )
    decoded_bytes.append(value % 256)

print(decoded_bytes[:200])
print(decoded_bytes[:200].decode(errors="ignore"))
