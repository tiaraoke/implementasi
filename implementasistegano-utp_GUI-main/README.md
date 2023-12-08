#implementasi_Stegano-utp-dengan-tampilan GUI

Implementasi Stegano dan OTP (One Time Path) dengan tampilan GUI ini merupakan salah satu untuk memenuhi tugas Mata Kuliah Kriptografi

langkah pertama: kita harus siapkan tools
 1. Visual Studio Code
 2. install Stegano, tk, dan pillow di cmd!

    Contoh : ![pillow](https://github.com/fauzifarhansyah/implementasistegano-utp_GUI/assets/127401431/a0f1ca13-6ad3-469a-b639-8e3cb91289b6)
             ![tk](https://github.com/fauzifarhansyah/implementasistegano-utp_GUI/assets/127401431/4ef28ca1-0b45-4c1d-bf08-f48b3eca3ff4)
             ![stegano](https://github.com/fauzifarhansyah/implementasistegano-utp_GUI/assets/127401431/802cef94-3322-4aa4-855b-a67b8935f001)

#langkah kedua: adalah lakukan source code seperti file steganografi.py

'''python
import tkinter as tk
from tkinter import filedialog
from PIL import Image
import random

def encrypt():
    plaintext = plaintext_entry.get()
    key = key_entry.get()

    /// Generate OTP key
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
'''


lalu jalankan source code kemudian akan muncul tampilan GUI

![1](https://github.com/fauzifarhansyah/implementasistegano-utp_GUI/assets/127401431/70773724-5490-4468-8103-6007958bc271)

 langkah ketiga: isilah plainteks dan key, dan pilih gambar dengan select image

![2](https://github.com/fauzifarhansyah/implementasistegano-utp_GUI/assets/127401431/10dabad9-ce7f-43e7-b5c8-8daff64177c2)

langkah keempat: lakukan encrypt dan descript sehingga akan muncul pilihan save image seperti diatas ini:
lalu simpan image dengan nama sesuai keinginan, contoh seperti di gambar diatas: "basket1 & basket2"
 

![3](https://github.com/fauzifarhansyah/implementasistegano-utp_GUI/assets/127401431/d345c217-5536-496b-ad17-3ff0c8fdd292)
#selanjutnya silakan periksa apakah sudah sukses melakukan encript seperti tulisan dibagian bawah gambar.

#Terima Kasih 

