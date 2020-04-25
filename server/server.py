from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import curses
import datetime
import sqlite3
import sys

global dbfilename
dbfilename = "messages.db"

class MessageDatabase(object):
    def __init__(self):
        db = sqlite3.connect(dbfilename)
        c = db.cursor()
        c.execute(
        "CREATE TABLE IF NOT EXISTS records\
            ( record_internal_id INTEGER PRIMARY KEY, \
              sender        TEXT, \
              reciever      TEXT, \
              contents      TEXT \
              )" \
            )
        db.commit()
        c.close()

    def add_record(sender = '', reciever='',contents=''):
        db = sqlite3.connect(dbfilename)
        c = db.cursor()
        c.execute('INSERT INTO records(sender,reciever,contents,timestamp) \
                    VALUES(?,?,?)', (sender,reciever,contents))
        db.commit()
        c.close()

    def get_record(self, message_reciever):
        db = sqlite3.connect(dbfilename)
        c = db.cursor()
        c.execute('SELECT sender,contents from records WHERE reciever=?', (message_reciever, ))
        records = c.fetchall()
        c.close()
        return records

def accept_incoming_connections():
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):
    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            client.send(msg)
            wgsender = "UserName"
            wgreciever = "User2"
            wgcontents = msg.decode("utf-8")
            print(wgsender,wgreciever,wgcontents)
            myDatabase.add_record(
            sender = wgsender,
            reciever = wgreciever,
            contents = wgcontents,
            )
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            break

clients = {}
addresses = {}

HOST = ''
PORT = 6900
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    myDatabase = MessageDatabase()
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
