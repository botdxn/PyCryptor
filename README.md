# PyCryptor
Encrypting files with a hash key

# Overview
This script provides you with functions to encrypt and decrypt files and whole directories. As of today the key is hardcoded because key generation and opening seems to throw a 'token invalid' when trying to decrypt whole directory but works when decrypting a single file.

# Modules
I didn't yet clean the script up but the modules and functions are as follows:
# main.py:
- creates config.json where you can specify if you want to delete original files after encryption and decryption
- debugClean() - WIP - deletes files and simulates a clean directory for you to test encryption and decryption
- encryptDir() - encrypts files in directory specified in variable 'filesToEncrypt'
- decryptDir() - decrypts files in directory specified in variable 'filesToDecrypt'
# encryptModule.py
- encryptFile(key, file) - encrypts a specified file with a key and either deletes or keeps original files
- decryptFile(key, file) - decrypts a specified file with a key and either deletes or keeps encrypted files
# keyModule.py
- createkey() - creates a key file with fernet
- openkey() - reads a key file

# Roadmap
- add terminal user interface to call the functions, specify files, keys, directories
- add argv support to execute from cmd with parameters
- create more secure encryption rather than relying on Fernet
- add stealth mode
- add threading support
