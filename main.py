from cryptography.fernet import Fernet
key = Fernet.generate_key()
f=Fernet(key)
with open("key_file","wb") as key_file:
    key_file.write(key)
token = f.encrypt(b"A very secret messengo")
print(token)
decryption = f.decrypt(token)
print(decryption)
