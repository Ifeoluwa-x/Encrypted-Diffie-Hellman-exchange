#!/usr/bin/env python3
from datetime import datetime

# Step 1: Load Vigenère matrix from file
with open("../step3/3extvigniar64", "r") as f:
    table = [list(line.strip()) for line in f.readlines()]

# Step 2: Define character set in the same custom order used in Step 3
chars = (
    [chr(i) for i in range(48, 58)] +    # Numbers (0-9)
    [chr(i) for i in range(97, 123)] +   # Lowercase (a-z)
    [chr(i) for i in range(65, 91)] +    # Uppercase (A-Z)
    [chr(i) for i in range(32, 48)] +    # Specials before numbers
    [chr(i) for i in range(58, 65)] +    # Specials between numbers and uppercase
    [chr(i) for i in range(91, 97)] +    # Specials between uppercase and lowercase
    [chr(i) for i in range(123, 127)]    # Remaining specials
)

# Step 3: Load plaintext
with open("originaltext1", "r") as f:
    plaintext = f.read()

# Step 4: Prompt for key
key = input("Enter the symmetric key: ").upper()

# Step 5: Encrypt using extended Vigenère cipher
encrypted = []
key_index = 0
for char in plaintext:
    if char not in chars:
        encrypted.append(char)
        continue
    row = chars.index(key[key_index % len(key)])
    col = chars.index(char)
    encrypted_char = table[row][col]
    encrypted.append(encrypted_char)
    key_index += 1

ciphertext = ''.join(encrypted)

# Step 6: Save encrypted text
with open("4sencryptedtextiar64", "w") as f:
    f.write(ciphertext)

# Step 7: Show and timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"\n Timestamp: {timestamp}")
print(" Encrypted Output:\n")
print(ciphertext)

