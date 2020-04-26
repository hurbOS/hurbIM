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
    authmsg = client.recv(BUFSIZ)
    dec = authmsg.decode("utf-8")
    if(dec!=""):
        splitter = dec.split(':')
        if(userdb.UserDatabase.get_record(splitter[0])==[]):
            print("Uh Oh!")
        else:
            if(userdb.UserDatabase.get_precord(splitter[1])==[]):
                print("Uh Oh Again!")
    while True:
        msg = client.recv(BUFSIZ)
        if not msg:
            break
        wgsender='UserName'
        wgreciever='User2'
        wgcontents=msg.decode("utf-8")
        wgtimestamp=str(time.ctime())
        #out = bytes(wgtimestamp + " - " +  wgsender + ": " + wgcontents, "utf8")
        #client.send(bytes("hey hey","utf8"))
        messagedb.MessageDatabase.add_record(sender=wgsender,reciever=wgreciever,contents=wgcontents,timestamp=wgtimestamp)
        print(messagedb.MessageDatabase.get_records())

clients = {}
addresses = {}

HOST = ''
PORT = 6900
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
