from cryptography.fernet import Fernet
import keyModule


def encryptFile(key):
    with open('Test.txt', 'rb') as file:
        fileData = file.read()
        
    fernet = Fernet(key)
    encrypted = fernet.encrypt(fileData)

    with open('Test.txt.encrypted', 'wb') as encryptFile:
        encryptFile.write(encrypted)
        
    print("File encrypted.")
    
def decryptFile(key):
    with open('Test.txt.encrypted', 'rb') as file:
        fileData = file.read()
        
    fernet = Fernet(key)
    encrypted = fernet.decrypt(fileData)

    with open('Test.txt.decrypted', 'wb') as encryptFile:
        encryptFile.write(encrypted)
        
    print("File decrypted.")