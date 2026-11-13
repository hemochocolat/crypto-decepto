from cryptography.fernet import Fernet
with open("key_file","rb") as key_file:
     customkey = key_file.read()
print (customkey)