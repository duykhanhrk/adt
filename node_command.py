import message
import node_list_command
import node_save_command
import node_delete_command

def handle(command):
    if len(command) == 0:
        message.error_message("DO:NULL", "cmw")
        return False
    elif command[0] == "list":
        return node_list_command.handle(command[1:])
    elif command[0] == "save":
        return node_save_command.handle(command[1:])
    elif command[0] == "delete":
        return node_delete_command.handle(command[1:])
    else:
        message.error_message(message[0], "cmd")
        return False
