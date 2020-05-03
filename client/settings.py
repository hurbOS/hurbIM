from cryptography.fernet import Fernet

global cipher
global user
global passw
global db1
global db2

key = Fernet.generate_key()
cipher = Fernet(key)
user = "UserName"
passw = "password"
db1 = "messages.db"
db2 = "contacts.db"

def init():
    global message_receiver
    message_receiver = ""
