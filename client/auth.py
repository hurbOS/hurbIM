import settings
def authenticate(client_socket):
    wgsender = settings.user
    wgpass = settings.passw

    msg=bytes(wgsender+":"+wgpass,"utf8")
    client_socket.send(msg)
