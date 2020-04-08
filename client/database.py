import curses
import npyscreen
import sqlite3
import datetime

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
        c.execute('SELECT sender,timestamp,contents from records WHERE reciever=?', (record_id, ))
        records = c.fetchall()
        c.close()
        return records[0]
################################################################################
class MessageRecordList(npyscreen.MultiLineAction):
    def __init__(self, *args, **keywords):
        super(MessageRecordList, self).__init__(*args, **keywords)
        self.add_handlers({
            "^A": self.when_add_record,
        })
        _contained_widget = npyscreen.MultiLineAction

    def when_add_record(self, *args, **keywords):
        self.parent.parentApp.getForm('EDITMESSAGE').value = None
        self.parent.parentApp.switchForm('EDITMESSAGE')

################################################################################
class EditMessage(npyscreen.ActionForm):
    def create(self):
        global wgsender
        global wgtimestamp
        self.value = None
        wgsender = "UserName"
        self.wgreciever = self.add(npyscreen.TitleText, name = "Recipient:")
        self.wgcontents   = self.add(npyscreen.MultiLineEdit, name = "Contents:",)
        wgtimestamp = datetime.datetime.now()

    def beforeEditing(self):
        if self.value:
            record = self.parentApp.myDatabase.get_record(self.value)
            self.name = "Record id : %s" % record[0]
            self.record_id          = record[0]
            wgsender  = record[1]
            self.wgreciever.value = record[2]
            self.wgcontents.value   = record[3]
            wgtimestamp = record[4]

        else:
            self.name = "New Record"
            self.record_id          = ''
            wgsender = ''
            self.wgreciever.value = ''
            self.wgcontents.value = ''
            wgtimestamp = ''


    def on_ok(self):
        if self.record_id: # We are editing an existing record
            self.parentApp.update_record(self.record_id,
                                            sender=wgsender,
                                            reciever = self.wgreciever.value,
                                            contents = self.wgcontents.value,
                                            timestamp = wgtimestamp,
                                            )
        else: # We are adding a new record.
            self.parentApp.myDatabase.add_record(
            sender = wgsender,
            reciever = self.wgreciever.value,
            contents = self.wgcontents.value,
            timestamp = wgtimestamp,
            )
        self.parentApp.switchFormPrevious()

    def on_cancel(self):
        self.parentApp.switchFormPrevious()
