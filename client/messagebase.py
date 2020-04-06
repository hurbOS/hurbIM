import curses
import npyscreen
import sqlite3

class MessageDatabase(object):
    def __init__(self, filename="messages.db"):
        self.dbfilename = filename
        db = sqlite3.connect(self.dbfilename)
        c = db.cursor()
        c.execute(
        "CREATE TABLE IF NOT EXISTS records\
            ( record_internal_id INTEGER PRIMARY KEY, \
              message_sender  TEXT, \
              message_reciever TEXT, \
              message_contents TEXT, \
              message_timestamp TEXT \
              )" \
            )
        db.commit()
        c.close()

    def add_record(self, message_sender = '', message_reciever='',message_contents='',message_timestamp=''):
        db = sqlite3.connect(self.dbfilename)
        c = db.cursor()
        c.execute('INSERT INTO records(message_sender,message_reciever,message_contents,message_timestamp) \
                    VALUES(?,?,?,?)', (message_sender,message_reciever,message_contents,message_timestamp))
        db.commit()
        c.close()

    def update_record(self, record_id, message_sender = '', message_reciever='',message_contents='',message_timestamp=''):
        db = sqlite3.connect(self.dbfilename)
        c = db.cursor()
        c.execute('UPDATE records set message_sender=?, message_reciever=?,message_contents=?,message_timestamp=? \
                    WHERE record_internal_id=?', (message_sender,message_reciever,message_contents,message_timestamp, \
                                                        record_id))
        db.commit()
        c.close()

    def delete_record(self, record_id):
        db = sqlite3.connect(self.dbfilename)
        c = db.cursor()
        c.execute('DELETE FROM records where record_internal_id=?', (record_id,))
        db.commit()
        c.close()

    def list_all_records(self, ):
        db = sqlite3.connect(self.dbfilename)
        c = db.cursor()
        c.execute('SELECT * from records')
        records = c.fetchall()
        c.close()
        return records

    def get_record(self, record_id):
        db = sqlite3.connect(self.dbfilename)
        c = db.cursor()
        c.execute('SELECT * from records WHERE record_internal_id=?', (record_id,))
        records = c.fetchall()
        c.close()
        return records[0]

class MessageRecordList(npyscreen.MultiLineAction):
    def __init__(self, *args, **keywords):
        super(MessageRecordList, self).__init__(*args, **keywords)
        self.add_handlers({
            "^D": self.when_delete_record
        })

    def display_value(self, vl):
        return "%s" % (vl[3])

    def when_delete_record(self, *args, **keywords):
        self.parent.parentApp.myDatabase.delete_record(self.values[self.cursor_line][0])
        self.parent.update_list()

def SendMessage(wgmessage_sender,wgmessage_reciever,wgmessage_contents,wgmessage_timestamp):
    parentApp.myDatabase.add_record(message_sender=wgmessage_sender.value,
    message_reciever = wgmessage_reciever.value,
    message_contents = wgmessage_contents.value,
    message_timestamp = wgmessage_timestamp.value
    )
