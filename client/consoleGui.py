from picotui import *
from picotui.context import Context
from picotui.screen import Screen
from picotui.widgets import *
from picotui.defs import *
from picotui.dialogs import *
from cryption import *
from prompt_toolkit.key_binding import KeyBindings
bindings = KeyBindings()

with Context():
    z=open("/home/wilson/Documents/Code/hurbIM/client/messagein.txt").readlines()
    x=open("/home/wilson/Documents/Code/hurbIM/client/welcome.txt").readlines()
    openFile=x
    file = "/home/wilson/Documents/Code/hurbIM/client/message.txt"
    key=load_key()
    numLines = sum(1 for line in openFile)

    d = Dialog(0,0)
    d.add(1, 1, WFrame(20, 40, "Messages"))
    d.add(2, 2, WListBox(18, 38, ["chat #%d" % i for i in range(50)]))
    d.add(21, 2, WFrame(102,38,))
    d.add(22, 3, WListBox(100, 36, ["%s" % openFile[i] for i in range(numLines)]))
    a = WButton(11,"Friends")
    b = WButton(8, "Quit")
    c = WButton(12,"Settings")
    d.add(114, 1, b)
    d.add(102, 1, a)
    d.add(89, 1, c)
    b.finish_dialog = ACTION_OK
    e = WTextEntry(100, "")
    d.add(22, 40, e)
        ...
    #d.redraw()
    result = d.loop()
