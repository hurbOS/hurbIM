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
              receiver      TEXT, \
              contents      TEXT, \
              timestamp     TEXT  \
              )" \
            )
        db.commit()
        c.close()

    def add_record(sender = '', receiver='',contents='',timestamp=''):
        db = sqlite3.connect(configure.dbfilename)
        c = db.cursor()
        c.execute('INSERT INTO records(sender,receiver,contents,timestamp) \
                    VALUES(?,?,?,?)', (sender,receiver,contents,timestamp))
        db.commit()
        c.close()

    def output_messages(user1,user2):
        db = sqlite3.connect(configure.dbfilename)
        c = db.cursor()
        c.execute('SELECT sender,receiver,contents from records WHERE sender=? AND receiver=?', (user2,user1))
        records = c.fetchall()
        c.close()
        merged=[]
        for item in records:
            stringy = str(item)
            merged.append(bytes(stringy, "utf8"))
        return merged
