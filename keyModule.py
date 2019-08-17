from cryptography.fernet import Fernet
import os

def createkey():
    key = Fernet.generate_key()
    file = open('key.key', 'wb')
    file.write(key)
    file.close()
    print(f"Encrypt key file created at {os.getcwd()}")
    return key

def openkey():
    try:
        file = open('key.key', 'rb')
        key = file.read()
        print(f"Encrypt key file opened at {os.getcwd()}")
        return key
    except ValueError:
        print('Key file not found.')