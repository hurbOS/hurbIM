from cryptography.fernet import Fernet

def init():
    global message_sender
    message_sender = ""

global cipher
key = Fernet.generate_key()
cipher = Fernet(key)
