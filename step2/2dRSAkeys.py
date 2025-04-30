#!/usr/bin/env python3
from datetime import datetime
import rsa

# Generate timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Generate RSA key pair
(pubkey, privkey) = rsa.newkeys(2048)

# Define pubrep path (relative to script location)
PUBREP_PATH = "../pubrepiar64/2dpubkeybiniar64.bin"

# Save keys in binary format
with open("2dpvkeybiniar64.bin", "wb") as f:
    f.write(privkey.save_pkcs1('DER'))

with open("2dpubkeybiniar64.bin", "wb") as f:
    f.write(pubkey.save_pkcs1('DER'))

# Save keys in ASCII format
with open("2dpvkeyasciar64.asc", "w") as f:
    f.write(privkey.save_pkcs1().decode())

with open("2dpubkeyasciar64.asc", "w") as f:
    f.write(pubkey.save_pkcs1().decode())

# Save public key to pubrep directory
try:
    with open(PUBREP_PATH, "wb") as f:
        f.write(pubkey.save_pkcs1('DER'))
except IOError:
    print(f"Error: Could not save public key to {PUBREP_PATH}")
    print("Please ensure the pubrepiar64 directory exists")

# Print results
print("Timestamp:", timestamp)
print("\nPrivate Key (ASCII):")
print(privkey.save_pkcs1().decode())
print("\nPublic Key (ASCII):")
print(pubkey.save_pkcs1().decode())
