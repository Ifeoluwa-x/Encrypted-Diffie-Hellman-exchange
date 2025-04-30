#!/usr/bin/env python3
from datetime import datetime
import rsa

def decrypt_key():
    # Generate timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        # Load private key
        with open("../step2/2dpvkeyasciar64.asc", "r") as f:
            priv_key = rsa.PrivateKey.load_pkcs1(f.read().encode())

        # Load encrypted key
        with open("../pubrepiar64/5keyencryptiar64", "rb") as f:
            encrypted_key = f.read()

        # Decrypt key
        decrypted_key = rsa.decrypt(encrypted_key, priv_key)

        # Save decrypted key
        with open("6symmetrickeyiar64", "wb") as f:
            f.write(decrypted_key)

        print("Timestamp:", timestamp)
        print("Decrypted symmetric key:", decrypted_key.decode())

    except FileNotFoundError as e:
        print(f"Error: {str(e)}")
        print("Please ensure both files exist:")
        print("- ../step2/2dpvkeyasciar64.asc")
        print("- ../pubrepiar64/5keyencryptiar64")
    except Exception as e:
        print(f"Decryption failed: {str(e)}")

if __name__ == "__main__":
    decrypt_key()
