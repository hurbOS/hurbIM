import sys
from asciimatics.effects import *
from asciimatics.event import *
from asciimatics.exceptions import *
from asciimatics.particles import *
from asciimatics.paths import *
from asciimatics.renderers import *
from asciimatics.scene import *
from asciimatics.screen import *
from asciimatics.sprites import *
from asciimatics.utilities import *
from asciimatics.version import *
from asciimatics.widgets import *

x = open("/home/wilson/Documents/Code/hurbIM/client/welcome.txt","r").readlines()
y = open("/home/wilson/Documents/Code/hurbIM/client/messagein.txt","r").readlines()
z = open("/home/wilson/Documents/Code/hurbIM/client/messageout.txt", "w")
openFile = x
numLines = sum(1 for line in openFile)

class MessageView(Frame):
    def __init__(self, screen):
        super(MessageView, self).__init__(screen,
                                       screen.height //3 *2,
                                       screen.width //3 *2,
                                       hover_focus=True,
                                       can_scroll=False,
                                       title="HurbIM")
        #self.set_theme("monochrome")
        self._list_view = ListBox(height = 17,name="Conversations",add_scroll_bar=True,options=[("option 1", 1), ("option 2", 2)])
        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(self._list_view)
        layout.add_widget(Divider())
        layout2 = Layout([1,1,1])
        self.add_layout(layout2)
        layout2.add_widget(Button("Settings", self._quit),0)
        #layout2.add_widget(Button("Friends", self._quit),1)
        layout2.add_widget(Button("Quit", self._quit),2)
        self.fix()
    @staticmethod
    def _quit():
        raise StopApplication("User pressed quit")

def demo(screen, scene):
    scenes = [
        Scene([MessageView(screen)], -1, name="Main"),
        #Scene([ContactView(screen, contacts)], -1, name="Edit Contact")
    ]

    screen.play(scenes, stop_on_resize=True, start_scene=scene, allow_int=True)

last_scene = None
while True:
    try:
        Screen.wrapper(demo, catch_interrupt=True, arguments=[last_scene])
        sys.exit(0)
    except ResizeScreenError as e:
        last_scene = e.scene
