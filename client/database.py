import sqlite3
import settings

class MessageDatabase(object):
    def __init__(self):
        db = sqlite3.connect(settings.db1)
        c = db.cursor()
        c.execute(
        "CREATE TABLE IF NOT EXISTS records\
            ( record_internal_id INTEGER PRIMARY KEY, \
              sender        TEXT, \
              receiver      TEXT, \
              contents      TEXT, \
              timestamp     TEXT \
              )" \
            )
        db.commit()
        c.close()

    def add_record(sender = '', receiver='',contents='',timestamp=''):
        db = sqlite3.connect(settings.db1)
        c = db.cursor()
        c.execute('INSERT INTO records(sender,receiver,contents,timestamp) \
                    VALUES(?,?,?,?)', (sender,receiver,contents,timestamp))
        db.commit()
        c.close()

    def get_record(message_receiver):
        db = sqlite3.connect(settings.db1)
        c = db.cursor()
        c.execute('SELECT timestamp,sender,contents from records WHERE receiver=?', (message_receiver, ))
        records = c.fetchall()
        c.close()
        return records

    def delete_records(self):
        db = sqlite3.connect(settings.db1)
        c = db.cursor()
        c.execute('DELETE * FROM records')
        db.commit()
        c.close()
