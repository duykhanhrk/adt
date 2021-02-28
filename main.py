import storage
import message
import data_center
import branch_center
import sys

def prepare_data():
    if not storage.does_file_exist("config.json"):
        message.error_message("config.json", "fid")
        return False

    if not data_center.load_config():
        message.error_message("config.json", "fic")
        return False

    if not data_center.in_config("exts_folder"):
        message.error_message("config.json::exts_folder", "prn")
        return False

    if not data_center.in_config("nodes_folder"):
        message.error_message("config.json::nodes_folder", "prn")
        return False

    if not data_center.in_config("current_node"):
        message.error_message("config.json::current_node", "prn")
        return False

    if not storage.does_directory_exist(data_center.get_exts_folder()):
        message.error_message(data_center.get_exts_folder(), "drn")
        return False

    if not storage.does_directory_exist(data_center.get_nodes_folder()):
        message.error_message(data_center.get_nodes_folder(), "drn")
        return False

    if not storage.does_node_exist(data_center.get_current_node()):
        message.error_message(data_center.get_current_node(), "ndn")
        return False

    if not data_center.load_node():
        message.error_message(data_center.get_current_node(), "fic")
        return False

    return True

def main():
    if not prepare_data():
        return 1

    sys.argv.pop(0)
    if len(sys.argv) > 0:
        while len(sys.argv) > 0:
            branch_center.handle(sys.argv.pop(0).split(" "))
        return 1

    while True:
        command = input("#> ")
        if command == "exit":
            return 0

        if command == "":
            continue

        branch_center.handle(command.split(" "))

        if message.can_show_messages():
            message.show_messages()

if __name__ == "__main__":
    main()