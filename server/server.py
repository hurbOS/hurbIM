import socket
from _thread import *
import threading

# Basic Vars
print_lock = threading.Lock()
HOST = '127.0.0.1'
PORT = 6900

#Create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
#Start listening
sock.listen(5)
print("Server is listening")

def threadFunc(c):
    while True:
        data = c.recv(1024)
        if not data:
            print_lock.release()
            break
        c.send(data)

#While loop to keep alive
while True:
    c, addr = sock.accept()
    print_lock.acquire()
    print("Connected")
    start_new_thread(threadFunc(c))
sock.close()