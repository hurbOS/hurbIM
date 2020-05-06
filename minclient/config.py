from cryptography.fernet import Fernet

global cipher
global user
global passw

key = Fernet.generate_key()
cipher = Fernet(key)
user = "UserName"
passw = "password"

def init():
    global message_receiver
    message_receiver = ""
