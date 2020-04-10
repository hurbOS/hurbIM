import npyscreen
import sqlite3
import settings
from client import *

class AddressDatabase(object):
    def __init__(self, filename="contacts.db"):
        self.dbfilename = filename
        db = sqlite3.connect(self.dbfilename)
        c = db.cursor()
        c.execute(
        "CREATE TABLE IF NOT EXISTS records\
            ( record_internal_id INTEGER PRIMARY KEY, \
              user_name     TEXT, \
              user_tag      TEXT \
              )" \
            )
        db.commit()
        c.close()

    def add_record(self, user_name = '', user_tag=''):
        db = sqlite3.connect(self.dbfilename)
        c = db.cursor()
        c.execute('INSERT INTO records(user_name, user_tag) \
                    VALUES(?,?)', (user_name, user_tag))
        db.commit()
        c.close()

    def update_record(self, record_id, user_name = '', user_tag=''):
        db = sqlite3.connect(self.dbfilename)
        c = db.cursor()
        c.execute('UPDATE records set user_name=?, user_tag=? \
                    WHERE record_internal_id=?', (user_name, user_tag, \
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

    def user_get_record(self, record_id):
        db = sqlite3.connect(self.dbfilename)
        c = db.cursor()
        c.execute('SELECT user_name from records WHERE record_internal_id=?', (record_id,))
        records = c.fetchall()
        c.close()
        return records[0]

#The main screen of the application will be a list of names. When the user selects a name, we will want to edit it. We will subclass MultiLineAction, and override display value to change how each record is presented. We will also override the method actionHighlighted to switch to the edit form when required. Finally, we will add two new keypresses - one to add and one to delete records. Before switching to the EDITRECORDFM, we either set its value to None, if creating a new form, or else set its value to that of the record we wish to edit.

class RecordList(npyscreen.MultiLineAction):
    def __init__(self, *args, **keywords):
        super(RecordList, self).__init__(*args, **keywords)

        self.add_handlers({
            "^A": self.when_add_record,
            "^D": self.when_delete_record
        })

    def display_value(self, vl):
        return "%s, %s" % (vl[1], vl[2])

    def actionHighlighted(self, act_on_this, keypress, *args, **keywords):
        settings.message_sender = self.parent.parentApp.myDatabase2.user_get_record(self.values[self.cursor_line][0])[0]
        messages = self.parent.parentApp.myDatabase.get_record(settings.message_sender)
        self.parent.update_message_list(messages)

    def when_add_record(self, *args, **keywords):
        self.parent.parentApp.getForm('EDITRECORDFM').value = None
        self.parent.parentApp.switchForm('EDITRECORDFM')

    def when_delete_record(self, *args, **keywords):
        self.parent.parentApp.myDatabase2.delete_record(self.values[self.cursor_line][0])
        self.parent.update_list()

#The actual form to display the record list will be a FormMutt subclass. We will alter the MAIN_WIDGET_CLASS class variable to use our RecordList widget, and make sure that the list of records is updated every time the form is presented to the user.

class EditContact(npyscreen.ActionForm):
    def create(self):
        self.value = None
        self.wgUserName   = self.add(npyscreen.TitleText, name = "User Name:",)
        self.wgUserTag = self.add(npyscreen.TitleText, name = "User Tag:")

    def beforeEditing(self):
        if self.value:
            record = self.parentApp.myDatabase2.get_record(self.value)
            self.name = "Record id : %s" % record[0]
            self.record_id          = record[0]
            self.wgUserName.value   = record[1]
            self.wgUserTag.value = record[2]
        else:
            self.name = "New Record"
            self.record_id          = ''
            self.wgUserName.value   = ''
            self.wgUserTag.value = ''

    def on_ok(self):
        if self.record_id: # We are editing an existing record
            self.parentApp.myDatabase2.update_record(self.record_id,
                                            user_name=self.wgUserName.value,
                                            user_tag = self.wgUserTag.value
                                            )
        else: # We are adding a new record.
            self.parentApp.myDatabase2.add_record(user_name=self.wgUserName.value,
            user_tag = self.wgUserTag.value
            )
        self.parentApp.switchFormPrevious()

    def on_cancel(self):
        self.parentApp.switchFormPrevious()
