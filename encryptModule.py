from cryptography.fernet import Fernet
import keyModule, json, os
from pathlib import Path

with open('config.json', 'r') as configFile:
        configData = json.load(configFile)

def encryptFile(key, file):
    with open(file, 'rb') as encryptfile:
        encryptfileData = encryptfile.read()
        
    fernet = Fernet(key)
    encrypted = fernet.encrypt(encryptfileData)

    with open(file + '.encrypted', 'wb') as encryptfile:
        encryptfile.write(encrypted)
        encryptfile.close()
        if configData['REMOVE_ENCRYPTED'] == 'True':
            os.remove(file)
            print(f"File {file} encrypted. Original file deleted.")
        else:
            print(f"File {file} encrypted.")
        
        print(f"Key used to encrypt: {repr(key)}")
    
def decryptFile(key, file):
    with open(file, 'rb') as fileDecrypt:
        fileData = fileDecrypt.read()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(fileData)
    
    with open(file, 'wb') as decryptFile:
        decryptFile.write(decrypted)
        decryptFile.close()
        if configData['REMOVE_DECRYPTED'] == 'True':
            if '.encrypted' in file:
                newfile = file.replace('.encrypted', '')
                os.rename(file, newfile)
            print(f"File {file} decrypted.")
        else:
            print(f"File {file} decrypted.")