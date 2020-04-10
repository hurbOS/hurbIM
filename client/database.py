import curses
import npyscreen
import sqlite3
import datetime
################################################################################
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

    def update_record(self, record_id, sender = '', reciever='',contents='',timestamp=''):
        db = sqlite3.connect(self.dbfilename)
        c = db.cursor()
        c.execute('UPDATE records set sender=?, reciever=?,contents=?,timestamp=?\
                    WHERE record_internal_id=?', (sender,reciever,contents,timestamp, \
                                                        record_id))
        db.commit()
        c.close()

    def get_record(self, message_reciever):
        db = sqlite3.connect(self.dbfilename)
        c = db.cursor()
        c.execute('SELECT sender,timestamp,contents from records WHERE reciever=?', (message_reciever, ))
        records = c.fetchall()
        c.close()
        return records
################################################################################
class MessageRecordList(npyscreen.MultiLineAction):
    def __init__(self, *args, **keywords):
        super(MessageRecordList, self).__init__(*args, **keywords)
################################################################################
