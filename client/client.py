import curses
from cryption import *
import npyscreen
import sqlite3

class InputBox(npyscreen.BoxTitle):
    _contained_widget = npyscreen.MultiLineEdit
class MessageBox(npyscreen.BoxTitle):
    _contained_widget = npyscreen.Pager

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

    def actionHighlighted(self, act_on_this, keypress):
        self.parent.parentApp.getForm('EDITRECORDFM').value =act_on_this[0]
        self.parent.parentApp.switchForm('EDITRECORDFM')

    def when_add_record(self, *args, **keywords):
        self.parent.parentApp.getForm('EDITRECORDFM').value = None
        self.parent.parentApp.switchForm('EDITRECORDFM')

    def when_delete_record(self, *args, **keywords):
        self.parent.parentApp.myDatabase.delete_record(self.values[self.cursor_line][0])
        self.parent.update_list()

#The actual form to display the record list will be a FormMutt subclass. We will alter the MAIN_WIDGET_CLASS class variable to use our RecordList widget, and make sure that the list of records is updated every time the form is presented to the user.

class RecordListDisplay(npyscreen.Form):
    def create(self):

        y, x = self.useable_space()
        self.ChatBox = self.add(RecordList, name="Chats", relx=2, max_width=x // 6, rely=1,
                                   max_height=0,values=[])
        self.MessageBox = self.add(MessageBox,name="Messages", rely=1, relx=(x // 5) + 1, max_height=-3, editable=True,
                                      custom_highlighting=True, highlighting_arr_color_data=[0],values=[])
        self.InputBox = self.add(InputBox, name="Input", relx=(x // 5) + 1, rely=-5,max_height=-3)

    def inputbox_submit(self, _input):
        self.InputBox.value = ""
        self.InputBox.display()
    def beforeEditing(self):
        self.update_list()

    def update_list(self):
        self.ChatBox.values = self.parentApp.myDatabase.list_all_records()
        self.ChatBox.display()
#The form to edit each record will be an example of an ActionForm. Records will only be altered when the user selects the ‘ok’ button. Before the form is presented to the user, the values of each of the individual widgets are updated to match the database record, or cleared if we are creating a new record.

class EditRecord(npyscreen.ActionForm):
    def create(self):
        self.value = None
        self.wgUserName   = self.add(npyscreen.TitleText, name = "User Name:",)
        self.wgUserTag = self.add(npyscreen.TitleText, name = "User Tag:")

    def beforeEditing(self):
        if self.value:
            record = self.parentApp.myDatabase.get_record(self.value)
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
            self.parentApp.myDatabase.update_record(self.record_id,
                                            user_name=self.wgUserName.value,
                                            user_tag = self.wgUserTag.value
                                            )
        else: # We are adding a new record.
            self.parentApp.myDatabase.add_record(user_name=self.wgUserName.value,
            user_tag = self.wgUserTag.value
            )
        self.parentApp.switchFormPrevious()

    def on_cancel(self):
        self.parentApp.switchFormPrevious()

#Finally, we need an application object that manages the two forms and the database:

class AddressBookApplication(npyscreen.NPSAppManaged):
    def onStart(self):
        self.myDatabase = AddressDatabase()
        self.addForm("MAIN", RecordListDisplay)
        self.addForm("EDITRECORDFM", EditRecord)

if __name__ == '__main__':
    myApp = AddressBookApplication()
    myApp.run()
