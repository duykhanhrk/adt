import message
import new_command
import delete_command
import dbs_command
import ext_command
import node_command
import change_command
import help_command
import get_command
import view_command

def handle(command):
    if command[0] == "new":
        return new_command.handle(command[1:])
    elif command[0] == "delete":
        return delete_command.handle(command[1:])
    elif command[0] == "dbs":
        return dbs_command.handle(command[1:])
    elif command[0] == "get":
        return get_command.handle(command[1:])
    elif command[0] == "view":
        return view_command.handle(command[1:])
    elif command[0] == "ext":
        return ext_command.handle(command[1:])
    elif command[0] == "node":
        return node_command.handle(command[1:])
    elif command[0] == "change":
        return change_command.handle(command[1:])
    elif command[0] == "help":
        return help_command.handle(command[1:])
    elif command[0] == "exit":
        if len(command) > 1:
            message.error_message(command[1], "cmw")
            return False
        return True
    else:
        message.error_message(command[0], "cmd")
