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

    def get_records():
        db = sqlite3.connect(configure.dbfilename)
        c = db.cursor()
        c.execute('SELECT * from records')
        records = c.fetchall()
        c.close()
        return records
