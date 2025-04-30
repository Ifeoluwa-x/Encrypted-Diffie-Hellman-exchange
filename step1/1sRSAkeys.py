#!/usr/bin/env python3  

from datetime import datetime
import rsa

# Generate timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Generate RSA key pair
(pubkey, privkey) = rsa.newkeys(2048)

# Define paths
PUBREP_PATH = "../pubrepiar64/"  # Fixed relative path

# Save keys in binary format
with open("1spvkeybiniar64.bin", "wb") as f:
    f.write(privkey.save_pkcs1('DER'))

with open("1spubkeybiniar64.bin", "wb") as f:
    f.write(pubkey.save_pkcs1('DER'))

# Save keys in ASCII format
with open("1spvkeyasciar64.asc", "w") as f:
    f.write(privkey.save_pkcs1().decode())

with open("1spubkeyasciar64.asc", "w") as f:
    f.write(pubkey.save_pkcs1().decode())

# Save public key to pubrep directory (will fail if directory doesn't exist)
try:
    with open(PUBREP_PATH + "1spubkeybiniar64.bin", "wb") as f:
        f.write(pubkey.save_pkcs1('DER'))
except Exception as e:
    print(f"Error saving to pubrep directory: {str(e)}")
    print(f"Please ensure {PUBREP_PATH} exists")

# Print timestamp and ASCII keys
print("Timestamp:", timestamp)
print("\nPrivate Key (ASCII):")
print(privkey.save_pkcs1().decode())
print("\nPublic Key (ASCII):")
print(pubkey.save_pkcs1().decode())
