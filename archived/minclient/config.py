from cryptography.fernet import Fernet

global cipher
global user
global passw
global connected
global message_receiver
global output

message_receiver = ""
key = Fernet.generate_key()
cipher = Fernet(key)
user = "UserName"
passw = "password"
connected = ""
output = ["",]
