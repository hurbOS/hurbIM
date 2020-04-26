from cryptography.fernet import Fernet

def init():
    global message_sender
    message_sender = ""

global cipher
global user
global passw
global welcome

key = Fernet.generate_key()
cipher = Fernet(key)
user = "UserName"
passw = "password"
