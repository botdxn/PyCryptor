from cryptography.fernet import Fernet


def createkey():
    key = Fernet.generate_key()
    file = open('key.key', 'wb')
    file.write(key)
    file.close()
    print("Encrypt key file created.")

def openkey():
    try:
        file = open('key.key', 'r')
        key = file.read()
        return key
    except ValueError:
        print('Key file not found.')