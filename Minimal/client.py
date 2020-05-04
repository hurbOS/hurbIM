from picotui.context import Context
from picotui.screen import Screen
from picotui.widgets import *
from picotui.defs import *
from picotui.dialogs import *
import os
import subprocess

with Context():
    width=subprocess.Popen('tput cols', shell=True, stdout=subprocess.PIPE, )
    height=subprocess.Popen('tput lines', shell=True, stdout=subprocess.PIPE, )
    out1=int(width.communicate()[0])
    out2 = int(height.communicate()[0])
    Screen.attr_color(C_WHITE, C_BLUE)
    Screen.cls()
    Screen.attr_reset()
    d = Dialog(0, 0, out1, out2)

    items = []
    #i = WTextEntry(out1-6, "")
    #d.add(3, 42,i)
    #i.handle_edit_key(KEY_ENTER)
    #res = i.get()
    #items.append(res)
    d.add(2, 1, WFrame(out1-4, out2-10, "Chats:"))
    d.add(3, 2, WListBox(out1-6, out2-12, items))
    d.redraw()
    res = d.loop()


print("Result:", res)
