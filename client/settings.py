from cryptography.fernet import Fernet

global cipher
global user
global passw
global welcome

key = Fernet.generate_key()
cipher = Fernet(key)
user = "UserName"
passw = "password"

def init():
    global message_reciever
    message_reciever = ""
