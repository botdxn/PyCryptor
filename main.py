import keyModule, encryptModule, os, json, glob

dir = os.getcwd()
filesToEncrypt = os.listdir('mass')
filesToDecrypt = glob.glob(dir + '\mass\*.encrypted')


#creating json config file
config = {
    "REMOVE_ENCRYPTED": "True",
    "REMOVE_DECRYPTED": "True"
}
with open('config.json', 'w') as configFile:
    json.dump(config, configFile)
    configFile.close()

#checking if key file is present, else creating a key file
KEY = "5VPo7JrbIFzQDMDdsBfx8bPhQwALxTmepzOawL6CLJY="
    

def main():
    #encryptDir(filesToEncrypt)
    decryptDir(filesToDecrypt)

def encryptDir(filesToEncrypt):
    for file in filesToEncrypt:
        encryptModule.encryptFile(KEY, dir + '/mass/' + file)

def decryptDir(filesToDecrypt):
    for file in filesToDecrypt:
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
    #debugClean()