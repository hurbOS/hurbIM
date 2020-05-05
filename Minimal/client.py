from picotui.context import Context
from picotui.screen import Screen
from picotui.widgets import *
from picotui.defs import *
from picotui.dialogs import *
import os
from subprocess import *

with Context():
    term_w  = Popen('tput cols', shell=True, stdout=PIPE).communicate()
    term_h  = Popen('tput lines', shell=True, stdout=PIPE).communicate()
    width  = int(term_w[0])
    height = int(term_h[0])
    
    
    Screen.attr_color(C_WHITE, C_BLACK)
    Screen.cls()
    Screen.attr_reset()
    Screen.cursor("off")
    d = Dialog(0, 0, width, height)

    items = ["Chat 1", "Chat 2", "Chat 3", "Chat 4"]
    #i = WTextEntry(out1-6, "")
    #d.add(3, 42,i)
    # i.handle_edit_key(KEY_ENTER)
    #res = i.get()
    # items.append(res)
    d.add(2, 1, WFrame(width-4, len(items)+2, "Chats:"))
    d.add(3, 2, WListBox(width-6, len(items), items))
    d.redraw()
    res = d.loop()


print("Result:", res)
