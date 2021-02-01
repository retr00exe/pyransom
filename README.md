# Pyransom

![Pyransom](https://res.cloudinary.com/retr00exe/image/upload/v1612194312/Screenshot_2021-02-01_224342_kgqurv.png)

This ransomware script implement [AES](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) and [RSA](<https://en.wikipedia.org/wiki/RSA_(cryptosystem)>) cryptosystem to encrypt file. Target folder will encrypted using fernet cryptosystem based on 128-bit **AES**. The fernet key also encrypted using **RSA** cryptosystem based on PKCS1-OAEP standard.

## How To Use

1. Generate RSA key by run `gen_rsa.py`. After that you will get a pair public and private key in PEM format.
2. Run `main.py` to start ransomware script.
3. After the welcome message show up you need to input the target directory you want to attack. The default directory is `C:/Users/<USERNAME>/Desktop`.

## Warning

Make sure you run this script on virtual machine. Don't delete your `private.pem` key or your file will be encrypted forever. This program is for educational purpose and help CS/CE students understand how cryptography works in real world scenario.

## Bug

- `PermissionError: [Errno 13] Permission denied:` (To prevent this bug run `cmd` as administrator)

**PS** : This tool is only for testing and academic purposes and can only be used where strict consent has been given. Do not use it for illegal purposes! Code licensed by MIT with no warranty.
