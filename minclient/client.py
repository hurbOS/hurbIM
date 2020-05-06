import curses
import commands
import config
import auth
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
screen = curses.initscr()
#relative size to terminal
num_rows, num_cols = screen.getmaxyx()
#colours
curses.start_color()
curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

#get input
def usr_input(window, r, c, length):
    curses.echo()
    choice = window.getstr(r, c, length)
    dec = choice.decode("utf-8")
    return dec

#windows
def main_window():
    global chat_window
    global msg_window
    global ticker_window
    global input_window
    global status_window
    chat_window = curses.newwin(num_rows-1, int(num_cols/5), 1, 0)
    chat_window.border(0)
    msg_window = curses.newwin(int(num_rows-5), int(num_cols/5*4-1), 1, int(num_cols-num_cols/5*4))
    msg_window.border(0)
    input_window = curses.newwin(4, int(num_cols/5*4-1), num_rows-4, int(num_cols-num_cols/5*4))
    input_window.border(0)
    input_window.addstr(1, 2, ">")
    status_window = curses.newwin(1, num_cols+2, 0, 0)
    status_window.attron(curses.color_pair(3))
    statusbarstr  = " | HURBIM | Unread Messages: {} | Server Connectivity: {} | Type 'help' to list commands | Type 'quit' to exit |"
    status_window.addstr(0, 0, statusbarstr)
    status_window.addstr(0, len(statusbarstr), " " * (num_cols - len(statusbarstr) - 1))
    status_window.attroff(curses.color_pair(3))

#main sequence
try:
    main_window()
    status_window.refresh()
    msg_window.refresh()
    chat_window.refresh()
except:
    print("Your window is too small, try again with a larger window")
    curses.endwin()

#connection
HOST = '127.0.0.1'
PORT = 6901
BUFSIZ = 1024
ADDR = (HOST, PORT)
global client_socket
client_socket = socket(AF_INET, SOCK_STREAM)
#client_socket.connect(ADDR)
#auth.authenticate(client_socket)
#receive_thread = Thread(target=receive)
#receive_thread.start()

#input loop
while True:
    input_window.refresh()
    msginput = usr_input(input_window, 1, 4, 200)
    input_window.refresh()
    input_window.clear()
    commands.check_command(msginput, msg_window, num_rows)
    if msginput == "quit" or msginput == "q":
        curses.endwin()
        break
    main_window()
