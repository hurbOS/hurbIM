from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import datetime
import sqlite3
import configure

class MessageDatabase(object):
    def __init__(self):
        db = sqlite3.connect(configure.dbfilename)
        c = db.cursor()
        c.execute(
        "CREATE TABLE IF NOT EXISTS records\
            ( record_internal_id INTEGER PRIMARY KEY, \
              sender        TEXT, \
              reciever      TEXT, \
              contents      TEXT, \
              timestamp     TEXT  \
              )" \
            )
        db.commit()
        c.close()

    def add_record(sender = '', reciever='',contents='',timestamp=''):
        db = sqlite3.connect(configure.dbfilename)
        c = db.cursor()
        c.execute('INSERT INTO records(sender,reciever,contents,timestamp) \
                    VALUES(?,?,?,?)', (sender,reciever,contents,timestamp))
        db.commit()
        c.close()

    def get_record(message_reciever):
        db = sqlite3.connect(configure.dbfilename)
        c = db.cursor()
        c.execute('SELECT sender,contents,timestamp from records WHERE reciever=?', (message_reciever, ))
        records = c.fetchall()
        c.close()
        return records

def accept_incoming_connections():
    while True:
        client, client_address = SERVER.accept()
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()

def handle_client(client):
    while True:
        msg = client.recv(BUFSIZ)
        if not msg:
            break
        wgsender='UserName'
        wgreciever='User2'
        wgcontents=msg.decode("utf-8")
        wgtimestamp=str(datetime.datetime.now())
        #out = bytes(wgtimestamp + " - " +  wgsender + ": " + wgcontents, "utf8")
        #client.send(out)
        MessageDatabase.add_record(sender=wgsender,reciever=wgreciever,contents=wgcontents,timestamp=wgtimestamp)

clients = {}
addresses = {}

HOST = ''
PORT = 6901
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    MessageDatabase()
    SERVER.listen(5)
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
