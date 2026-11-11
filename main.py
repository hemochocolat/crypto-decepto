from cryptography.fernet import Fernet
key = Fernet.generate_key()
f=Fernet(key)
token = f.encrypt(b"A very secret messengo")
print(token)
decryption = f.decrypt(token)
print(decryption)