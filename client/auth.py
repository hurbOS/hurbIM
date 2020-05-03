import settings
from cryptography.fernet import Fernet

def authenticate(socket):
    wgsender = settings.user
    wgpass = settings.passw

    msg=bytes(wgsender+":"+wgpass,"utf8")
    socket.send(msg)

def encode(text):
    from settings import cipher
    encoded_text = cipher.encrypt(text)
    print(encoded_text)

def decode(text):
    from settings import cipher
    decoded_text = cipher.decrypt(text)
