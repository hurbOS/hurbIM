from picotui.context import Context
from picotui.screen import Screen
from picotui.widgets import *


def handle_click(w):
    with open('/home/wilson/Documents/Code/hurbIM/client/messageout.txt', 'w') as f:
        f.write(e.t)


with Context():

    d = Dialog(5, 5, 50, 12)

    d.add(1, 1, "Entry:")

    e = WTextEntry(100, "Text")
    d.add(10, 1, e)

    b = WButton(10, "Click")
    d.add(10, 10, b)
    b.on("click", handle_click)

    res = d.loop()
