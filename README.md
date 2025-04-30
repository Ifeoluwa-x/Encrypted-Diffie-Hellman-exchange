# 🔐 Scripting For Cybersecurity

This project simulates a secure message transmission between two virtual machines — **Ubuntu (SOURCE)** and **Kali Linux (DESTINATION)** — using hybrid cryptographic techniques. It demonstrates both asymmetric encryption (RSA) and symmetric encryption (Vigenère), along with bash-based file exchange and timestamped terminal validations.

---

## 📘 Project Description

This simulation reflects the principles of secure communication across untrusted networks. The project involves:
- Generating RSA key pairs
- Building an extended ASCII Vigenère table
- Encrypting text using a symmetric key
- Securing that key with RSA
- Transferring encrypted components via bash
- Decrypting the message on the destination
- Post-processing the decrypted text per specified formatting rules

Screenshots are taken throughout the process with timestamps to verify execution sequence and correctness.

---

## 📂 Project Structure

```plaintext
finaliar64/
├── kalitreeiar64.png
├── ubuntutreeiar64.png
├── step1/
│   ├── 1sRSAkeys.py
│   ├── 1spvkeyasciar64.asc
│   ├── 1spubkeyasciar64.asc
│   └── 1sRSAkeysiar64.png
├── step2/
│   ├── 2dRSAkeys.py
│   ├── 2dpvkeyasciar64.asc
│   ├── 2dpubkeyasciar64.asc
│   └── 2dRSAkeysiar64.png
├── step3/
│   ├── 3vigniereiar64.py
│   └── 3extVigniereiar64.html
├── step4/
│   ├── 4symencryptiar64.py
│   ├── 4sencryptedtextiar64
│   └── 4sencryptedtextiar64.png
├── step5/
│   ├── 5keyencryptioniar64.py
│   └── 5exchangeiar64.png
├── step6/
│   ├── 6keydecryptioniar64.py
│   └── 6keydecryptioniar64.png
├── step7/
│   └── 7encfiletraniar64.png
├── step8/
│   ├── 8ddecryptioniar64.py
│   └── 8finaldecryptioniar64.png
├── step9/
│   ├── 9finalcodeiar64.py
│   └── 9absolutefinaliar64.jpg

```

---

## 🔄 Step-by-Step Workflow

### 🧩 Step 1: RSA Key Generation (Ubuntu - SOURCE)
- **Script:** `step1/1sRSAkeys.py`
- **Screenshot:** `step1/1sRSAkeysiar64.png`
- **Description:** Generates RSA key pair; saves keys in binary and ASCII; prints and screenshots with timestamp.

---

### 🧩 Step 2: RSA Key Generation (Kali - DESTINATION)
- **Script:** `step2/2dRSAkeys.py`
- **Screenshot:** `step2/2dRSAkeysiar64.png`
- **Description:** Same as Step 1 but done in Kali.

---

### 🧩 Step 3: Extended Vigenère Table Generation
- **Script:** `step3/3vigniereiar64.py`
- **Output:** `step3/3extVigniereiar64.html`
- **Description:** Generates 94x94 ASCII-based Vigenère table; HTML output with timestamp.

---

### 🧩 Step 4: Symmetric Encryption Using Vigenère (Ubuntu)
- **Script:** `step4/4symencryptiar64.py`
- **Output:** `step4/4sencryptedtextiar64`
- **Screenshot:** `step4/4sencryptedtextiar64.png`
- **Description:** Encrypts original text using the Vigenère table and key `SHAKESPEARE`.

---

### 🧩 Step 5: Symmetric Key Encryption and Transfer
- **Script:** `step5/5keyencryptioniar64.py`
- **Screenshot:** `step5/5exchangeiar64.png`
- **Description:** Encrypts the symmetric key with the Kali public RSA key; transfers key + Vigenère table via Bash.

---

### 🧩 Step 6: Decrypt Symmetric Key (Kali)
- **Script:** `step6/6keydecryptioniar64.py`
- **Output:** `6symmetrickeyiar64`
- **Screenshot:** `step6/6keydecryptioniar64.png`
- **Description:** Uses private RSA key to decrypt symmetric key.

---

### 🧩 Step 7: Encrypted Text Transfer (Ubuntu ➡️ Kali)
- **Screenshot:** `step7/7encfiletraniar64.png`
- **Description:** Transfers encrypted text file to DESTINATION with Bash and timestamped log.

---

### 🧩 Step 8: Decryption of Text Using Symmetric Key (Kali)
- **Script:** `step8/8ddecryptioniar64.py`
- **Output:** `8dplaintextiar64`
- **Screenshot:** `step8/8finaldecryptioniar64.png`
- **Description:** Decrypts text using recovered symmetric key and imported Vigenère table.

---

### 🧩 Step 9: Final Text Processing (Kali)
- **Script:** `step9/9finalcodeiar64.py`
- **Output:** `9absolutefinaliar64`
- **Screenshot:** `step9/9absolutefinaliar64.jpg`
- **Description:** Converts text: punctuation → ASCII in `{}`, lowercases every character except first in line.

---

## 📸 Screenshot Summary

| Step | Screenshot File | Description |
|------|------------------|-------------|
| 1 | `step1/1sRSAkeysiar64.png` | RSA key generation on Ubuntu |
| 2 | `step2/2dRSAkeysiar64.png` | RSA key generation on Kali |
| 4 | `step4/4sencryptedtextiar64.png` | Encrypted text output |
| 5 | `step5/5exchangeiar64.png` | Bash file exchange log |
| 6 | `step6/6keydecryptioniar64.png` | RSA key decryption |
| 7 | `step7/7encfiletraniar64.png` | Encrypted text file transfer |
| 8 | `step8/8finaldecryptioniar64.png` | Final decrypted plaintext |
| 9 | `step9/9absolutefinaliar64.jpg` | Final text transformation |

---

## 🎓 What I Learned

Working on this project gave me a deeper, hands-on understanding of several critical concepts in cybersecurity and system administration, including:

- 🔐 **Public-Key Cryptography (RSA):**  
  I learned how RSA encryption and decryption work, including generating and managing public/private key pairs in both binary and ASCII formats.

- 🧠 **Symmetric Encryption (Vigenère Cipher):**  
  I implemented an extended Vigenère cipher table that includes all printable ASCII characters, gaining insight into substitution ciphers and symmetric encryption mechanics.

- 📂 **Hybrid Encryption Model:**  
  I combined RSA and Vigenère to simulate real-world hybrid cryptographic systems, where a symmetric key is exchanged securely using public-key cryptography.

- 🧑‍💻 **Python Scripting:**  
  I wrote Python scripts to automate cryptographic processes, generate HTML outputs, read/write binary and text files, and apply formatting transformations to decrypted content.

- 💻 **Linux Command Line & Bash Scripting:**  
  I used Bash commands for inter-VM file transfers, managed folder structures, and executed scripts via terminal with timestamped logs.

- 🧾 **System Organization & Documentation:**  
  I followed strict file-naming conventions, structured my project directories correctly, and learned the importance of reproducibility and timestamped screenshots for validation.

- 🔍 **Attention to Detail Under Exam Constraints:**  
  I practiced working under exam-like restrictions, where internet use was limited, and every detail—naming, file structure, and execution order—was critical to success.

---


