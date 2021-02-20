import data_center
import message
import storage

def act(node_id):
    if not storage.does_node_exist(node_id):
        message.error_message(node_id, "ndn")
        return False

    storage.delete_node(node_id)
    return True

def handle(command):
    if len(command) == 0:
        message.error_message("NODE ID::NULL", "cmw")
        return False

    if len(command) == 1:
        return act(command[0])

    message.error_message(command[1], "cmw")
    return False
