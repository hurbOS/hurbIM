import sqlite3
import configure
from operator import itemgetter

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

    def get_records():
        db = sqlite3.connect(configure.dbfilename)
        c = db.cursor()
        c.execute('SELECT * from records')
        records = c.fetchall()
        c.close()
        return records

    def output_messages(user1,user2):
        db = sqlite3.connect(configure.dbfilename)
        c = db.cursor()
        c.execute('SELECT * from records WHERE sender=? AND reciever=?', (user1,user2))
        records = c.fetchall()
        c.execute('SELECT * from records WHERE sender=? AND reciever=?', (user2,user1))
        records2 = c.fetchall()
        c.close()
        merged = []
        for item in records:
            merged.append(item)
        for item in records2:
            merged.append(item)
        merged.sort(key=itemgetter(0))
        return merged
