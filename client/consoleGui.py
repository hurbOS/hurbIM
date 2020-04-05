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

class MessageView(Frame):
    def __init__(self, screen):
        super(MessageView, self).__init__(screen,
                                       screen.height -2,
                                       screen.width -4,
                                       hover_focus=True,
                                       can_scroll=True,
                                       title="HurbIM")
        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(Button("Quit", self._quit))
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
