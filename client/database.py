import sqlite3

class MessageDatabase(object):
    def __init__(self,filename="messages.db"):
        self.dbfilename = filename
        db = sqlite3.connect(self.dbfilename)
        c = db.cursor()
        c.execute(
        "CREATE TABLE IF NOT EXISTS records\
            ( record_internal_id INTEGER PRIMARY KEY, \
              sender        TEXT, \
              reciever      TEXT, \
              contents      TEXT, \
              timestamp     TEXT \
              )" \
            )
        db.commit()
        c.close()

    def add_record(self, sender = '', reciever='',contents='',timestamp=''):
        db = sqlite3.connect(self.dbfilename)
        c = db.cursor()
        c.execute('INSERT INTO records(sender,reciever,contents,timestamp) \
                    VALUES(?,?,?,?)', (sender,reciever,contents,timestamp))
        db.commit()
        c.close()

    def get_record(self, message_reciever):
        db = sqlite3.connect(self.dbfilename)
        c = db.cursor()
        c.execute('SELECT sender,timestamp,contents from records WHERE reciever=?', (message_reciever, ))
        records = c.fetchall()
        c.close()
        return records

    def delete_records(self):
        db = sqlite3.connect(self.dbfilename)
        c = db.cursor()
        c.execute('DELETE * FROM records')
        db.commit()
        c.close()
