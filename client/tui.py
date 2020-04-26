import npyscreen
import settings
import curses
################################################################################
class RecordList(npyscreen.MultiLineAction):
    def __init__(self, *args, **keywords):
        super(RecordList, self).__init__(*args, **keywords)
        self.add_handlers({
            "^A": self.when_add_record,
            "^D": self.when_delete_record
        })
    def display_value(self, vl):
        return "%s" % (vl[1])
    def actionHighlighted(self, act_on_this, keypress, *args, **keywords):
        settings.message_sender = self.parent.parentApp.myDatabase2.user_get_record(self.values[self.cursor_line][0])[0]
        #messages = self.parent.parentApp.myDatabase.get_record(settings.message_sender)
        self.parent.update_message_list("")

    def when_add_record(self, *args, **keywords):
        self.parent.parentApp.getForm('EDITRECORDFM').value = None
        self.parent.parentApp.switchForm('EDITRECORDFM')

    def when_delete_record(self, *args, **keywords):
        self.parent.parentApp.myDatabase2.delete_record(self.values[self.cursor_line][0])
        self.parent.update_list()

class BoxTitle2(npyscreen.BoxTitle):
     _contained_widget = RecordList
################################################################################
class MessageList(npyscreen.MultiLineAction):
    def __init__(self, *args, **keywords):
        super(MessageList, self).__init__(*args, **keywords)
    #def display_value(self, vl):
    #    return "%s %s %s" % (vl[1],vl[])
class BoxTitle3(npyscreen.BoxTitle):
     _contained_widget = MessageList
###############################################################################
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
################################################################################
