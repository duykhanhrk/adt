import data_center
import message
import storage

def act(node_id):

    data_center.save_node(node_id)
    return True

def handle(command):
    if len(command) == 0:
        return act(data_center.get_current_node())

    if len(command) == 1:
        # Check if this node id is correct.
        if not storage.is_true_node_id(command[0]):
            message.error_message(command[1], "dnn")
            return False

        # Check that the node id already exists.
        if storage.does_node_exist(command[0]):
            message.error_message(command[0], "nde")
            return False

        return act(command[0])
                

    message.error_message(command[1], "cmw")
    return False
