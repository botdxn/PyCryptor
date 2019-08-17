import keyModule, encryptModule

KEY = keyModule.openkey()

def main():
    keyModule.createkey()
    encryptModule.encryptFile(KEY)
    encryptModule.decryptFile(KEY)

if __name__ == '__main__':
    main()