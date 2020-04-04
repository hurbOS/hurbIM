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
    z=open("/home/wilson/Documents/Code/hurbIM/client/message.txt").readlines()
    x=open("/home/wilson/Documents/Code/hurbIM/client/welcome.txt").readlines()
    open_file=x
    file = "/home/wilson/Documents/Code/hurbIM/client/message.txt"
    key=load_key()
    num_lines = sum(1 for line in open_file) - 1
    d.add(22, 3, WListBox(100, 36, ["%s" % open_file[i] for i in range(num_lines)]))
    a = WButton(11,"Friends")
    b = WButton(8, "Quit")
    d.add(114, 1, b)
    d.add(102, 1, a)
    b.finish_dialog = ACTION_OK

    #d.redraw()
    result = d.loop()
