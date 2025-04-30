#!/usr/bin/env python3
from datetime import datetime

# Step 1: Load Vigenère Table
with open("../pubrepiar64/3extvigniar64", "r") as f:
    table = [list(line.strip()) for line in f.readlines()]

# Step 2: Character order (same as encryption)
chars = (
    [chr(i) for i in range(48, 58)] +    # Numbers
    [chr(i) for i in range(97, 123)] +   # Lowercase
    [chr(i) for i in range(65, 91)] +    # Uppercase
    [chr(i) for i in range(32, 48)] +    # Specials before numbers
    [chr(i) for i in range(58, 65)] +    # Specials between numbers/uppercase
    [chr(i) for i in range(91, 97)] +    # Specials between uppercase/lowercase
    [chr(i) for i in range(123, 127)]    # Remaining specials
)

# Step 3: Load symmetric key
with open("../step6/6symmetrickeyiar64", "rb") as f:
    key = f.read().decode()

# Step 4: Load encrypted text
with open("../pubrepiar64/4sencryptedtextiar64", "r") as f:
    encrypted_text = f.read()

# Step 5: Decrypt using extended Vigenère logic
decrypted = []
key_index = 0

for c in encrypted_text:
    if c not in chars:
        decrypted.append(c)
        continue
    row_char = key[key_index % len(key)]
    row_index = chars.index(row_char)
    col_index = table[row_index].index(c)
    decrypted_char = chars[col_index]
    decrypted.append(decrypted_char)
    key_index += 1

plaintext = ''.join(decrypted)

# Step 6: Save plaintext
with open("8dplaintextiar64", "w") as f:
    f.write(plaintext)

# Step 7: Print timestamp and plaintext
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f" Timestamp: {timestamp}")
print(" Decrypted Message:\n")
print(plaintext)
