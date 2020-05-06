import curses
import config

output = ["",]
def check_command(command, msg_window, num_rows):
    outcount = 0
    commandlist = [
    "",
    "Command (abbreviation) --arguments - description",
    "",
    "quit          (q) - Quits this application",
    "help          (h) - Displays this menu",
    "send       *  (s) - Enter messaging mode",
    "recipient     (r) --Username - set message receiver",
    "contact    *  (c) --Username - Add a contact",
    "friend     *  (f) --Username - Add a friend",
    "block      *  (b) --Username - Block a user",
    "unblock    *  (u) --Username - Unblock a user",
    "delete     *  (d) --Username - Delete Contact",
    "",
    "*  - Not working yet",
    ]
    if command == "":
        return

    elif command == "help" or command == "h":
        count = 0
        for items in commandlist:
            output.append(commandlist[count])
            count+=1

    elif "recipient" in command or "r" in command:
        try:
            split = command.split("--")
            config.message_receiver = split[1]
            output.append("Message recipient set to '"+config.message_receiver+"'.")
        except:
            output.append("Something was wrong with your command, try again")

    else:
        output.append("Command '"+command+"' not recognised, please try another.")

    for items in output:
        msg_window.addstr(outcount,2,output[outcount])
        while len(output) > num_rows -6:
            output.pop(1)
        msg_window.refresh()
        outcount+=1
