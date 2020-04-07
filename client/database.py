import curses
import npyscreen
import sqlite3
import datetime

class MessageDatabase(object):
    def __init__(self, filename="messages.db"):
        self.dbfilename = filename
        db = sqlite3.connect(self.dbfilename)
        c = db.cursor()
        c.execute(
        "CREATE TABLE IF NOT EXISTS records\
            ( record_internal_id INTEGER PRIMARY KEY, \
              sender        TEXT, \
              reciever      TEXT, \
              contents      TEXT, \
              timestamp     TEXT, \
              sender_tag    TEXT, \
              reciever_tag  TEXT  \
              )" \
            )
        db.commit()
        c.close()

    def add_record(self, sender = '', reciever='',contents='',timestamp='',sender_tag='',reciever_tag=''):
        db = sqlite3.connect(self.dbfilename)
        c = db.cursor()
        c.execute('INSERT INTO records(sender,reciever,contents,timestamp,sender_tag,reciever_tag) \
                    VALUES(?,?,?,?,?,?)', (sender,reciever,contents,timestamp,sender_tag,reciever_tag))
        db.commit()
        c.close()

    def update_record(self, record_id, sender = '', reciever='',contents='',timestamp='',sender_tag='',reciever_tag=''):
        db = sqlite3.connect(self.dbfilename)
        c = db.cursor()
        c.execute('UPDATE records set sender=?, reciever=?,contents=?,timestamp=?,sender_tag=?,reciever_tag=?\
                    WHERE record_internal_id=?', (sender,reciever,contents,timestamp,sender_tag,reciever_tag, \
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

    def get_user_record(self):
        db = sqlite3.connect(self.dbfilename)
        c = db.cursor()
        c.execute('SELECT * from records WHERE sender=wilson')
        records = c.fetchall()
        c.close()
        return records[0]

    def get_record(self, record_id):
        db = sqlite3.connect(self.dbfilename)
        c = db.cursor()
        c.execute('SELECT * from records WHERE record_internal_id=?', (record_id,))
        records = c.fetchall()
        c.close()
        return records[0]
################################################################################
class MessageRecordList(npyscreen.MultiLineAction):
    def __init__(self, *args, **keywords):
        super(MessageRecordList, self).__init__(*args, **keywords)
        _contained_widget = npyscreen.MultiLineAction

    def display_value(self, vl):
        return "%s %s %s" % (vl[4],vl[1],vl[3])


    def when_add_record(self, *args, **keywords):
        self.parent.parentApp.getForm('EDITMESSAGE').value = None
        self.parent.parentApp.switchForm('EDITMESSAGE')

    def when_delete_record(self, *args, **keywords):
        self.parent.parentApp.myDatabase.delete_record(self.values[self.cursor_line][0])
        self.parent.update_list()
################################################################################
class RecordList(npyscreen.MultiLineAction):
    def __init__(self, *args, **keywords):
        super(RecordList, self).__init__(*args, **keywords)
        self.add_handlers({
            "^A": self.when_add_record,
            "^D": self.when_delete_record
        })

    def display_value(self, vl):
        return "%s, %s" % (vl[1], vl[2])

    def actionHighlighted(self, act_on_this, keypress):
        record = parent.parentApp.myDatabase.get_record(self.value)
        update_list()

    def when_add_record(self, *args, **keywords):
        self.parent.parentApp.getForm('EDITMESSAGE').value = None
        self.parent.parentApp.switchForm('EDITMESSAGE')

    def when_delete_record(self, *args, **keywords):
        self.parent.parentApp.myDatabase.delete_record(self.values[self.cursor_line][0])
        self.parent.update_list()
################################################################################
class EditMessage(npyscreen.ActionForm):
    def create(self):
        global wgsender
        global wgtimestamp
        global wgsender_tag
        self.value = None
        wgsender = "UserName"
        self.wgreciever = self.add(npyscreen.TitleText, name = "Recipient:")
        self.wgreciever_tag = self.add(npyscreen.TitleText, name = "Tag")
        self.wgcontents   = self.add(npyscreen.MultiLineEdit, name = "Contents:",)
        wgtimestamp = datetime.datetime.now()
        wgsender_tag = "0822"

    def beforeEditing(self):
        if self.value:
            record = self.parentApp.myDatabase.get_record(self.value)
            self.name = "Record id : %s" % record[0]
            self.record_id          = record[0]
            wgsender  = record[1]
            self.wgreciever.value = record[2]
            self.wgcontents.value   = record[3]
            wgtimestamp = record[4]
            self.wgreciever_tag = record[5]
            wgsender_tag = record[6]
        else:
            self.name = "New Record"
            self.record_id          = ''
            wgsender = ''
            self.wgreciever.value = ''
            self.wgcontents.value = ''
            wgtimestamp = ''
            self.wgreciever_tag = ''
            wgsender_tag = ''

    def on_ok(self):
        if self.record_id: # We are editing an existing record
            self.parentApp.update_record(self.record_id,
                                            sender=wgsender,
                                            reciever = self.wgreciever.value,
                                            contents = self.wgcontents.value,
                                            timestamp = wgtimestamp,
                                            sender_tag = wgsender_tag,
                                            reciever_tag = self.wgreciever_tag
                                            )
        else: # We are adding a new record.
            self.parentApp.myDatabase.add_record(
            sender = wgsender,
            reciever = self.wgreciever.value,
            contents = self.wgcontents.value,
            timestamp = wgtimestamp,
            sender_tag = wgsender_tag,
            reciever_tag = self.wgreciever_tag
            )
        self.parentApp.switchFormPrevious()

    def on_cancel(self):
        self.parentApp.switchFormPrevious()
