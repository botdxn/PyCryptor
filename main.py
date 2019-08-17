import keyModule, encryptModule, os, json, glob, sys, getopt

#creating json config file
config = {
    "REMOVE_ENCRYPTED": "True",
    "REMOVE_DECRYPTED": "True"
}
#loading json config file
with open('config.json', 'w') as configFile:
    json.dump(config, configFile)
    configFile.close()

#checking if key file is present, else creating a key file
if os.path.isfile('key.key') == True:
    KEY = keyModule.openkey()
    print('Key file found.')
elif os.path.isfile('/key.key') == False:
    print('Key file not found. Creating new key.')
    keyModule.createkey()
    KEY = keyModule.openkey()

def encryptDir(KEY, filesToEncrypt):
    for file in filesToEncrypt:
        encryptModule.encryptFile(KEY, arg + file)

def decryptDir(KEY, filesToDecrypt):
    for file in filesToDecrypt:
        encryptModule.decryptFile(KEY, file)

if __name__ == '__main__':
        try:
                opts, args = getopt.getopt(sys.argv[1:], 'o:v', ['encdir=', 'decdir=', 'encfile=', 'decfile=', 'key==', 'dirkey==', 'help=='])
        except getopt.GetoptError as error:
                print(error)
                sys.exit(2)
        
        for opt, arg in opts:
                if opt == '--encdir':
                        files = [ f for f in os.listdir(arg) if os.path.isfile(os.path.join(arg,f)) ]
                        encryptDir(KEY, files)
                        
                elif opt == '--decdir':
                        decryptDir(KEY, glob.glob(arg+'*.encrypted'))
                
                elif opt =='--encfile':
                        encryptModule.encryptFile(KEY, arg)
                        
                elif opt == '--decfile':     
                        encryptModule.decryptFile(KEY, arg)
                        
                elif opt == '--key':
                        KEY = bytes(arg)
                        
                elif opt == '--dirkey':
                        try:
                                file = open(arg, 'rb')
                                KEY = file.read()
                        except ValueError:
                                print('Key file not found.')
                                
                # elif opt or arg == '--help':
                #         print("List of available parameters:")
                #         print("--help returns list of available parameters")
                #         print("--encfile <path to file> encodes a file and returns the key used to encode")
                #         print("--decfile <path to file + \".encrypted\"> decodes a file if either the key file is present in current dir, or if the key is specified via --key or if the key path is specified via --keydir")
                #         print("--encdir <path to directory> encodes all files inside the specified directory and returns the key")
                #         print("--decdir <path to directory> decodes all *.encrypted files inside specified directory if either the key file is present in current dir, or if the key is specified via --key or if the key path is specified via --keydir")