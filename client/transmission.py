from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

def auth():
    break

def receive():
       while True:
           try:
               msg = client_socket.recv(BUFSIZ).decode("utf8")
               InputBox.update_message_list(msg)

           except OSError:
               break

def when_add_Message():
    try:
        if(self.value!=""):
            wgsender = settings.user
            wgreciever = settings.message_sender
            self.wgcontents  = self.value

            msg=bytes(self.wgcontents,"utf8")
            client_socket.send(msg)
            self.value=""
    except:
        self.value = ""

if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 6901

    BUFSIZ = 1024
    ADDR = (HOST, PORT)

    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(ADDR)

    receive_thread = Thread(target=receive)
    receive_thread.start()
