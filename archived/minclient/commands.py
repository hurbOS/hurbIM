import curses
import config
import time
import pickle

def msg_list(msg_window,num_rows,input_window):
    try:
        fd = open('messages.data', 'rb')
        dataset = pickle.load(fd)
        clearout()
        config.ouput.append(dataset)
        list_out(msg_window,num_rows,input_window)
    except:
        return

def clearout(msg_window,num_rows, input_window):
    config.output = ["",]
    list_out(msg_window,num_rows, input_window)

def usr_input(window, r, c, length, prompt):
    curses.echo()
    window.addstr(r, c, prompt)
    choice = window.getstr(r, c + 2, length)
    dec = choice.decode("utf-8")
    return dec

def list_out(msg_window, num_rows, input_window):
    outcount = 0
    for items in config.output:
        msg_window.addstr(outcount,2,config.output[outcount])
        while len(config.output) > num_rows -6:
            config.output.pop(1)
        msg_window.refresh()
        input_window.border(0)
        input_window.refresh()
        outcount+=1

def check_command(command, msg_window, num_rows, input_window):
    commandlist = [
    "",
    "Command (abbreviation) --arguments - description",
    "",
    "quit          (q) - Quits this application",
    "help          (h) - Displays this menu",
    "send          (s) - Enter messaging mode",
    " - exit       (e) - exit send mode",
    " - img     *  (i) - Send image",
    "recipient     (r) --Username - set message receiver",
    "contact    *  (c) --Username - Add a contact",
    "friend     *  (f) --Username - Add a friend",
    "block      *  (b) --Username - Block a user",
    "unblock    *  (u) --Username - Unblock a user",
    "delete     *  (d) --Username - Delete Contact",
    "",
    "*  - Not working yet",
    "",
    ]

    if command == "":
        return

    elif command == "help" or command == "h":
        count = 0
        config.output.append("["+time.ctime()+"] Help Menu:")
        for items in commandlist:
            config.output.append(commandlist[count])
            count+=1

    elif "recipient" in command or "r" in command:
        try:
            split = command.split("--")
            config.message_receiver = split[1]
            config.output.append("["+time.ctime()+"] Message recipient set to '"+config.message_receiver+"'.")
        except:
            config.output.append("["+time.ctime()+"] Something was wrong with your command, try again")

    elif command == "send" or command == "s":
        clearout(msg_window,num_rows, input_window)
        config.output.append("["+time.ctime()+"] Send mode")
        msg_list(msg_window,num_rows,input_window)
        while True:
            out = usr_input(input_window, 1, 2, 200, ":")
            input_window.clear()
            input_window.border(0)
            input_window.refresh()
            if out == "exit" or out == "e":
                config.output.append("["+time.ctime()+"] Command Mode")
                list_out(msg_window,num_rows,input_window)
                break
            elif out =="":
                1+1
    else:
        config.output.append("["+time.ctime()+"] Command '"+command+"' not recognised, please try another.")
    list_out(msg_window, num_rows, input_window)
