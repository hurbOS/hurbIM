from picotui import *
from picotui.context import Context
from picotui.screen import Screen
from picotui.widgets import *
from picotui.defs import *
from cryption import *

with Context():
    d = Dialog(0,0)
    d.add(22, 40, WTextEntry(100,""))

    d.add(1, 1, WFrame(20, 40, "Messages"))
    d.add(2, 2, WListBox(18, 38, ["choice%d" % i for i in range(50)]))

    d.add(21, 2, WFrame(102,38,))
    z=open("Documents/Code/hurbIM/client/message.txt")
    file="Documents/Code/hurbIM/client/message.txt"
    key=load_key()
    decrypt(file,key)
    y = z.read()
    d.add(22, 3, WMultiEntry(100, 36, [y]))
    a = WButton(11,"Friends")
    b = WButton(8, "Quit")
    d.add(114, 1, b)
    d.add(102, 1, a)
    b.finish_dialog = ACTION_OK

    #d.redraw()
    result = d.loop()
