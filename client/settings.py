from cryptography.fernet import Fernet

global cipher
global user
global passw
global welcome
global HOST
global PORT
global BUFSIZ
global ADDR

key = Fernet.generate_key()
cipher = Fernet(key)
user = "UserName"
passw = "password"

def init():
    global message_receiver
    message_receiver = ""
