import tkinter as tk
from tkinter import filedialog
from PIL import Image
import random

def encrypt():
    plaintext = plaintext_entry.get()
    key = key_entry.get()

    # Generate OTP key
    otp_key = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(len(plaintext)))

    ciphertext = ""
    for i in range(len(plaintext)):
        char = chr((ord(plaintext[i]) + ord(otp_key[i]) + ord(key[i])) % 256)
        ciphertext += char

    save_path = filedialog.asksaveasfilename(defaultextension="basket1.jpg")
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size
    index = 0
    for row in range(height):
        for col in range(width):
            r, g, b = pixels[col, row]
            if index < len(ciphertext):
                pixels[col, row] = (r & 0xFE | (ord(ciphertext[index]) >> 7),
                                    g & 0xFE | ((ord(ciphertext[index]) >> 2) & 0x01),
                                    b & 0xFE | (ord(ciphertext[index]) & 0x03))
                index += 1

    img.save(save_path)
    result_label.config(text="Encryption successful!")

def decrypt():
    key = key_entry.get()

    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size
    ciphertext = ""
    for row in range(height):
        for col in range(width):
            r, g, b = pixels[col, row]
            char = chr(((r & 0x01) << 7) | ((g & 0x01) << 2) | (b & 0x03))
            ciphertext += char

    plaintext = ""
    for i in range(len(ciphertext)):
        char = chr((ord(ciphertext[i]) - ord(key[i])) % 256)
        plaintext += char

    result_label.config(text="Decryption successful!")
    plaintext_entry.delete(0, tk.END)
    plaintext_entry.insert(0, plaintext)

def select_image():
    global image_path
    image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg")])
    image_label.config(text="Selected image: " + image_path)

root = tk.Tk()
root.title("Steganography with OTP")

plaintext_label = tk.Label(root, text="Plaintext:")
plaintext_label.pack()

plaintext_entry = tk.Entry(root)
plaintext_entry.pack()

key_label = tk.Label(root, text="Key:")
key_label.pack()

key_entry = tk.Entry(root)
key_entry.pack()

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt)
encrypt_button.pack()

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt)
decrypt_button.pack()

select_image_button = tk.Button(root, text="Select Image", command=select_image)
select_image_button.pack()

image_label = tk.Label(root, text="Selected image: None")
image_label.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
