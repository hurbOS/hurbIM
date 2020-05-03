from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import configure
import time
import messagedb
import userdb

def accept_incoming_connections():
    while True:
        client, client_address = SERVER.accept()
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()

def handle_client(client):
    try:
        authmsg = client.recv(BUFSIZ)
        dec = authmsg.decode("utf-8")
        if(dec!=""):
            splitter = dec.split(':')
            if(userdb.UserDatabase.get_record(splitter[0])==[]):
                client.close()
            else:
                if(userdb.UserDatabase.get_precord(splitter[1])==[]):
                    client.close()
                else:
                    print("connected")
                    while True:
                            msg = client.recv(BUFSIZ)
                            if not msg:
                                break
                            msgsplitter=msg.decode("utf-8").split(':')
                            messagedb.MessageDatabase.add_record(sender=msgsplitter[0],receiver=msgsplitter[1],contents=msgsplitter[2],timestamp=time.ctime())
                            sendable = messagedb.MessageDatabase.output_messages(msgsplitter[0],msgsplitter[1])
                            for item in sendable:
                                client.send(item)
    except:
        print("client side error")

clients = {}
addresses = {}

HOST = ''
PORT = 6901
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    messagedb.MessageDatabase()
    userdb.UserDatabase()
    SERVER.listen(5)
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
