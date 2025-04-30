#!/usr/bin/env python3

from datetime import datetime
import rsa

# Load public key from DESTINATION (Step 2)
with open("../step2/2dpubkeybiniar64.bin", "rb") as f:
    pub_key = rsa.PublicKey.load_pkcs1(f.read(), format="DER")

# Symmetric key from Step 4 (e.g., SHAKESPEARE)
symmetric_key = "SHAKESPEARE".encode()

# Encrypt the key
encrypted_key = rsa.encrypt(symmetric_key, pub_key)

# Save encrypted symmetric key
with open("5keyencryptiar64", "wb") as f:
    f.write(encrypted_key)

# Print timestamp and confirmation
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("Timestamp:", timestamp)
print("Encrypted symmetric key saved as 5keyencryptiar64")
