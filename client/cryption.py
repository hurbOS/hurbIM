from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("/home/wilson/Documents/Code/hurbIM/client/key.key","wb") as key_file:
        key_file.write(key)

def load_key():
    return open("/home/wilson/Documents/Code/hurbIM/client/key.key", "rb").read()

def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)
