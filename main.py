import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import customtkinter as ctk
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import hashlib
import json
import time
import shutil
import urllib.request

# Download and set background image
bg_image_path = "background_image.webp"
urllib.request.urlretrieve("https://media.istockphoto.com/id/1724789360/photo/digital-security-concept-and-cloud-computing-security.jpg?s=612x612&w=0&k=20&c=Fn_R9Vo2vGbJv_qxLvCE37JbEWD7RJq0Gzb_dbl1abE=", bg_image_path)

# Progress Bar Update Function
def update_progress(progress_bar, value):
    progress_bar.set(value)
    root.update_idletasks()

# Password Strength Checker
def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Too short"
    if not any(char.isdigit() for char in password):
        return "Weak: Add numbers"
    if not any(char.isupper() for char in password):
        return "Weak: Add uppercase letters"
    if not any(char in "!@#$%^&*()-_+=<>?/" for char in password):
        return "Weak: Add special characters"
    return "Strong"

# Secure Key Storage
def store_private_key(private_key, password):
    key_hash = hashlib.sha256(password.encode()).digest()
    encrypted_key = AES.new(key_hash, AES.MODE_EAX).encrypt(private_key.export_key())
    with open("private_key.enc", "wb") as file:
        file.write(encrypted_key)

def load_private_key(password):
    key_hash = hashlib.sha256(password.encode()).digest()
    try:
        with open("private_key.enc", "rb") as file:
            encrypted_key = file.read()
        private_key = AES.new(key_hash, AES.MODE_EAX).decrypt(encrypted_key)
        return RSA.import_key(private_key)
    except:
        return None

def encrypt_file(file_path, password, progress_bar):
    update_progress(progress_bar, 0.2)
    key = hashlib.sha256(password.encode()).digest()
    cipher = AES.new(key, AES.MODE_EAX)
    with open(file_path, 'rb') as f:
        data = f.read()
    ciphertext, tag = cipher.encrypt_and_digest(data)
    update_progress(progress_bar, 0.6)
    with open(file_path + ".enc", "wb") as f:
        f.write(cipher.nonce + tag + ciphertext)
    update_progress(progress_bar, 1.0)
    messagebox.showinfo("Success", "File encrypted successfully!")

def decrypt_file(file_path, password, progress_bar):
    key = hashlib.sha256(password.encode()).digest()
    with open(file_path, 'rb') as f:
        nonce, tag, ciphertext = f.read(16), f.read(16), f.read()
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    try:
        data = cipher.decrypt_and_verify(ciphertext, tag)
        original_filename = file_path.replace(".enc", "")
        with open(original_filename, "wb") as f:
            f.write(data)
        update_progress(progress_bar, 1.0)
        messagebox.showinfo("Success", "File decrypted successfully!")
    except:
        failed_attempts[file_path] = failed_attempts.get(file_path, 0) + 1
        if failed_attempts[file_path] >= 3:
            os.remove(file_path)
            messagebox.showerror("Security Alert", "File deleted after 3 failed attempts!")
        else:
            messagebox.showerror("Error", "Incorrect password!")

# GUI Setup
root = ctk.CTk()
root.title("Secure File Encryption Tool")
root.geometry("500x400")

# Load and display background image
bg_image = Image.open(bg_image_path)
bg_image = bg_image.resize((500, 400), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

file_path = tk.StringVar()
failed_attempts = {}

ctk.CTkLabel(root, text="Select File", bg_color="transparent", text_color="white", font=("Arial", 14)).pack(pady=5)
ctk.CTkEntry(root, textvariable=file_path, width=300).pack()
ctk.CTkButton(root, text="Browse", command=lambda: file_path.set(filedialog.askopenfilename())).pack(pady=5)

ctk.CTkLabel(root, text="Enter Password", bg_color="transparent", text_color="white", font=("Arial", 14)).pack(pady=5)
password_entry = ctk.CTkEntry(root, show="*")
password_entry.pack()

password_strength_label = ctk.CTkLabel(root, text="", bg_color="transparent", text_color="white")
password_strength_label.pack()

def update_strength():
    strength = check_password_strength(password_entry.get())
    password_strength_label.configure(text=strength)
password_entry.bind("<KeyRelease>", lambda e: update_strength())

progress_bar = ctk.CTkProgressBar(root)
progress_bar.pack(pady=10)

ctk.CTkButton(root, text="Encrypt", command=lambda: encrypt_file(file_path.get(), password_entry.get(), progress_bar)).pack(pady=5)
ctk.CTkButton(root, text="Decrypt", command=lambda: decrypt_file(file_path.get(), password_entry.get(), progress_bar)).pack(pady=5)

root.mainloop()
