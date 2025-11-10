# 🔐 Secure File Encryption Tool

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Encryption-AES%20256-green?logo=lock&logoColor=white" />
  <img src="https://img.shields.io/badge/GUI-Tkinter%20%26%20CustomTkinter-orange?logo=windowsterminal&logoColor=white" />
  <img src="https://img.shields.io/badge/Security-RSA%20Key%20Storage-red?logo=shield&logoColor=white" />
  <img src="https://img.shields.io/github/stars/Godakash007/SECURE-FILE-ENCRYPION-TOOL?style=social" />
</p>

---

## 🧠 Overview

**Secure File Encryption Tool** is a **Python-based desktop application** designed to safeguard confidential files using **AES-256 encryption**.  
It offers **RSA-protected key storage**, a **password strength checker**, and **automatic file deletion** after multiple failed decryption attempts — ensuring your data remains secure at all times.

The intuitive **Tkinter + CustomTkinter GUI** makes file encryption accessible to everyone — from cybersecurity students to privacy-conscious users.

---

## ✨ Features

✅ **AES-256 Encryption & Decryption** – Protects files using industry-grade encryption.  
✅ **Password Strength Checker** – Encourages strong, unpredictable passwords.  
✅ **RSA-Secured Key Storage** – Encrypts private keys for additional security.  
✅ **Auto File Deletion** – Deletes files after 3 failed decryption attempts to prevent brute-force attacks.  
✅ **Modern GUI** – Built with Tkinter and CustomTkinter for a clean and user-friendly interface.  

---

## 🛠️ Technologies Used

| Component | Technology |
|------------|-------------|
| Programming Language | Python |
| GUI Framework | Tkinter, CustomTkinter |
| Encryption | AES (via PyCryptodome) |
| Key Management | RSA |
| File Handling | Secure I/O mechanisms |

---

## 🚀 How to Use

1. **Clone the repository**
   ```bash
   git clone https://github.com/Godakash007/SECURE-FILE-ENCRYPION-TOOL.git
   cd SECURE-FILE-ENCRYPION-TOOL
   
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt

3. **Run the application**
   ```bash
   python main.py
4. **Encrypt or Decrypt Files**
    Select a file via the Browse button.
    Enter a strong password (strength indicator will guide you).
    Click Encrypt to secure your file.
    To decrypt, choose the encrypted file and enter the correct password.
