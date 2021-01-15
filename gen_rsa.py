from Crypto.PublicKey import RSA

rsa_key = RSA.generate(2048)

private_key = rsa_key.export_key()
with open('private.pem', 'wb') as f:
    f.write(private_key)

public_key = rsa_key.publickey().export_key()
with open('public.pem', 'wb') as f:
    f.write(public_key)
