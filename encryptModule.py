from cryptography.fernet import Fernet
import keyModule


def encryptFile(key, file):
    with open('Test.txt', 'rb') as encryptfile:
        encryptfileData = encryptfile.read()
        
    fernet = Fernet(key)
    encrypted = fernet.encrypt(encryptfileData)

    with open('Test.txt.encrypted', 'wb') as encryptfile:
        encryptfile.write(encrypted)
        encryptfile.close()
        
    print("File encrypted.")
    
def decryptFile(key, file):
    with open(file + '.encrypted', 'rb') as fileDecrypt:
        fileData = fileDecrypt.read()
        
    fernet = Fernet(key)
    decrypted = fernet.decrypt(fileData)

    with open('Test.txt.decrypted', 'wb') as decryptFile:
        decryptFile.write(decrypted)
        
    print("File decrypted.")