from cryption import *
from consoleGui import *
#key
key = load_key()
# file name
file = "/home/wilson/Documents/Code/hurbIM/client/message.txt"
# encrypt it
encrypt(file, key)
#gui
print(result)
