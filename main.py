import keyModule, encryptModule, os

file = ('Test.txt')

if os.path.isfile('./key.key') == True:
    KEY = keyModule.openkey()
    print('Key file found.')
else:
    print('Key file not found. Creating new key.')
    keyModule.createkey()
    KEY = keyModule.openkey()
    

def main():
    encryptModule.encryptFile(KEY, file)
    encryptModule.decryptFile(KEY, file)

def debugClean():
    os.remove('key.key')
    print('DEBUG: Keys removed.')
    os.remove(file + '.encrypted')
    print('DEBUG: Encrypted files removed.')
    os.remove(file + '.decrypted')
    print('DEBUG: Decrypted files removed.')
    
if __name__ == '__main__':
    main()
    debugClean()