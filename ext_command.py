import message
import ext_list_command
import ext_add_command
import ext_delete_command

def handle(command):
    if len(command) == 0:
        message.error_message("DO:NULL", "cmw")
        return False
    elif command[0] == "list":
        return ext_list_command.handle(command[1:])
    elif command[0] == "add":
        return ext_add_command.handle(command[1:])
    elif command[0] == "delete":
        return ext_delete_command.handle(command[1:])
    else:
        message.error_message(command[0], "cmd")
        return False
