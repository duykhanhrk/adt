import message

def handle(command):
    if command[0] == "new":
        pass
    else:
        message.error_message(command[0], "cmd")