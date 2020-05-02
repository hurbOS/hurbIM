import settings
def authenticate(socket):
    wgsender = settings.user
    wgpass = settings.passw

    msg=bytes(wgsender+":"+wgpass,"utf8")
    socket.send(msg)
