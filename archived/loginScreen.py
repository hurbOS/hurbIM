
from picotui.context import Context
from picotui.screen import Screen
from picotui.widgets import *
from picotui.defs import *
from picotui.dialogs import *
import os
from subprocess import *

with Context():
    # Terminal width & height 
    term_w  = Popen('tput cols', shell=True, stdout=PIPE, ).communicate()
    term_h = Popen('tput lines', shell=True, stdout=PIPE, ).communicate()
    
    # Size variables
    width = int(term_w[0])
    height = int(term_h[0])

    mid_x = width / 2
    mid_y = height / 2
    
    # Set screen shit
    Screen.attr_color(C_WHITE, C_BLACK)
    Screen.cls()
    Screen.attr_reset()
    Screen.enable_mouse()

    # Base 
    d = Dialog(0, 0, width, height)
    frame = WFrame(width-2, height-2, "Login Screen:")
    d.add(1, 1, frame)

    # Title
    with open("Minimal/title.txt", "r") as f:
        title = f.readlines()
    
    name_w = len(title[0])
    name_h = len(title)-1   
    # name = WListBox(name_w, name_h, title)
    pos_x = int((frame.w / 2)-(name_w/2))
    pos_y = int((frame.h / 2)-(name_h/2) - 3)
    
    for i in range(len(title)):
        d.add(pos_x,pos_y+i, title[i])

    # Text Input
    username = WTextEntry(32, " ")
    password = WTextEntry(32, " ")
    d.add(mid_x-15, 12, "Username:")
    d.add(mid_x-15, 14, "Password:")
    d.add(mid_x-4, 12, username)
    d.add(mid_x-4, 14, password)

    # Button
    """ Got lazy so I gave up"""

    # items = ["One", "Two", "Three", "Four"]
    # i = WTextEntry(width-6, "")
    # d.add(3, 42,i)
    # i.handle_edit_key(KEY_ENTER)
    # res = i.get()
    # items.append(res)
    
    d.redraw()
    res = d.loop()

print("Result:", res)