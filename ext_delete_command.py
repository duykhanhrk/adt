import data_center
import message
import storage

def act(ext_id):
    if not storage.does_ext_exist(ext_id):
        message.error_message(ext_id, "etn")
        return False

    storage.delete_ext(ext_id)
    return True

def handle(command):
    if len(command) == 0:
        message.error_message("EXT ID::NULL", "cmw")
        return False

    if len(command) == 1:
        return act(command[0])

    message.error_message(command[1], "cmw")
    return False
