import data_center
import message
import storage

def act(file_path):
    if not storage.does_file_exist(file_path):
        message.error_message(file_path, "fid")
        return False

    storage.add_ext(file_path)
    return True

def handle(command):
    if len(command) == 0:
        message.error_message("EXT FILE::NULL", "cmw")
        return False

    if len(command) == 1:
        return act(command[0])

    message.error_message(command[1], "cmw")
    return False
