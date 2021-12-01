from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path
from os import listdir
from os.path import isfile, join
import time


class Encryptor:
    # generates a key
    def __init__(self, key):
        self.key = key

    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    # encrypts with generated key
    def encrypt(self, message, key, key_size=256):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)

    # encrypts given file
    def encrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            plaintext = fo.read()
        enc = self.encrypt(plaintext, self.key)
        with open(file_name + ".enc", 'wb') as fo:
            fo.write(enc)
        os.remove(file_name)

    # decrypts with key
    def decrypt(self, ciphertext, key):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")

    # decrypts selected file
    def decrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            ciphertext = fo.read()
        dec = self.decrypt(ciphertext, self.key)
        with open(file_name[:-4], 'wb') as fo:
            fo.write(dec)
        os.remove(file_name)

    # reads all files
    def getAllFiles(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dirs = []
        for dirName, subdirList, fileList in os.walk(dir_path):
            for fname in fileList:
                if (fname != 'script.py' and fname != 'data.txt.enc'):
                    dirs.append(dirName + "\\" + fname)
        return dirs

    # encrypts files one-by-one
    def encrypt_all_files(self):
        dirs = self.getAllFiles()
        for file_name in dirs:
            self.encrypt_file(file_name)

    # decrypts files one-by-one
    def decrypt_all_files(self):
        dirs = self.getAllFiles()
        for file_name in dirs:
            self.decrypt_file(file_name)


key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
enc = Encryptor(key)
clear = lambda: os.system('cls')

if os.path.isfile('passwordFile.txt.enc'):
    while True:
        password = str(input("Enter Your Password: "))
        enc.decrypt_file("passwordFile.txt.enc")
        p = ''
        with open("passwordFile.txt", "r") as f:
            p = f.readlines()
        if p[0] == password:
            enc.encrypt_file("passwordFile.txt")
            break

    while True:
        clear()
        choice = int(input(
            "1. Select '1' to Encrypt File.\n2. Select '2' to Decrypt File.\n3. Select '3' to Encrypt All Files in Directory.\n4. Select '4' to Decrypt All Files in Directory.\n5. Select '5' to Exit.\n"))
        clear()
        if choice == 1:
            enc.encrypt_file(str(input("Enter Name of File to Encrypt: ")))
        elif choice == 2:
            enc.decrypt_file(str(input("Enter Name of File to Decrypt: ")))
        elif choice == 3:
            enc.encrypt_all_files()
        elif choice == 4:
            enc.decrypt_all_files()
        elif choice == 5:
            exit()
        else:
            print("Please Select a Valid Option!")

else:
    while True:
        clear()
        password = str(input("Please Enter a Password that will be Used for Decryption: "))
        repassword = str(input("Please Confirm Password: "))
        if password == repassword:
            break
        else:
            print("Passwords Mismatched!")
    f = open("passwordFile.txt", "w+")
    f.write(password)
    f.close()
    enc.encrypt_file("passwordFile.txt")
    print("Please Restart the Program")
    time.sleep(15)


