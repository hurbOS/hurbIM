import npyscreen
import settings
import curses
import time
import database

class InputBox(npyscreen.MultiLineEdit):
    def __init__(self, *args, **keywords):
        super(InputBox, self).__init__(*args, **keywords)
        self.add_handlers({
            curses.ascii.NL: self.when_add_Message,
        })
    def when_add_Message(self, *args, **keywords):
        #try:
            if(self.value!=""):
                wgsender = settings.user
                wgreceiver = settings.message_receiver
                self.wgcontents  = self.value
                msg=bytes(wgsender+":"+wgreceiver+":"+self.wgcontents,"utf8")
                self.parent.sendmsg(msg)
                database.MessageDatabase.add_record(sender=wgsender,receiver=wgreceiver,contents=self.wgcontents,timestamp=time.ctime())
                self.value=""
                messages = database.MessageDatabase.get_record(settings.message_receiver)
                self.parent.update_message_list(messages)
        #except:
        #    self.value = ""

class BoxTitle(npyscreen.BoxTitle):
     _contained_widget = InputBox


class RecordList(npyscreen.MultiLineAction):
    def __init__(self, *args, **keywords):
        super(RecordList, self).__init__(*args, **keywords)
        self.add_handlers({
            "^A": self.when_add_record,
        })
    def display_value(self, vl):
        return "%s" % (vl[1])
    def actionHighlighted(self, act_on_this, keypress, *args, **keywords):
        settings.message_receiver = self.parent.parentApp.myDatabase2.user_get_record(self.values[self.cursor_line][0])[0]
        messages = database.MessageDatabase.get_record(settings.message_receiver)
        self.parent.update_message_list(messages)

    def when_add_record(self, *args, **keywords):
        self.parent.parentApp.getForm('EDITRECORDFM').value = None
        self.parent.parentApp.switchForm('EDITRECORDFM')

class BoxTitle2(npyscreen.BoxTitle):
     _contained_widget = RecordList

class MessageList(npyscreen.MultiLineAction):
    def __init__(self, *args, **keywords):
        super(MessageList, self).__init__(*args, **keywords)

class BoxTitle3(npyscreen.BoxTitle):
     _contained_widget = MessageList

class EditContact(npyscreen.ActionForm):
    def create(self):
        self.value = None
        self.wgUserName   = self.add(npyscreen.TitleText, name = "User Name:",)

    def beforeEditing(self):
        self.name = 'New Contact'
        self.record_id          = ''
        self.wgUserName.value   = ''

    def on_ok(self):
         # We are adding a new record.
        self.parentApp.myDatabase2.add_record(user_name=self.wgUserName.value)
        self.parentApp.switchFormPrevious()

    def on_cancel(self):
        self.parentApp.switchFormPrevious()
