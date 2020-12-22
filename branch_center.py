import message
import new_command
import delete_command
import dbs_command
import change_command

def handle(command):
    if command[0] == "new":
        return new_command.handle(command[1:])
    elif command[0] == "delete":
        return delete_command.handle(command[1:])
    elif command[0] == "dbs":
        return dbs_command.handle(command[1:])
    elif command[0] == "change":
        return change_command.handle(command[1:])
    else:
        message.error_message(command[0], "cmd")
