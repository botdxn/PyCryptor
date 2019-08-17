import keyModule, encryptModule, os, json, glob, sys, getopt

#dir = os.getcwd()
#filesToEncrypt = os.listdir('mass')
#filesToDecrypt = glob.glob(dir + '\mass\*.encrypted')


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
        print('elo')

def encryptDir(filesToEncrypt):
    for file in filesToEncrypt:
        encryptModule.encryptFile(KEY, arg + file)

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
        try:
                opts, args = getopt.getopt(sys.argv[1:], 'o:v', ['encdir=', 'decdir=', 'encfile=', 'decfile='])
        except getopt.GetoptError as error:
                print(error)
                sys.exit(2)
        
        for opt, arg in opts:
                if opt == '--encdir':
                        encryptDir(os.listdir(arg))
                        
                elif opt == '--decdir':
                        decryptDir(glob.glob(arg+'*.encrypted'))
                
                elif opt =='--encfile':
                        encryptModule.encryptFile(KEY, arg)
                        
                elif opt == '--decfile':     
                        encryptModule.decryptFile(KEY, arg)