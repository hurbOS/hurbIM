import npyscreen

def guiFunc(*args):
    form = npyscreen.Form(name='hurbIM')
    form.edit()

def launchGui(*args):
    npyscreen.wrapper_basic(guiFunc)