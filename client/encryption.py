from cryptography.fernet import Fernet

def encode(text):
    from settings import cipher
    encoded_text = cipher.encrypt(text)
    print(encoded_text)

def decode(text):
    from settings import cipher
    decoded_text = cipher.decrypt(text)
