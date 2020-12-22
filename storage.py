import data_center
import json
import os
import platform

SAPERATE = "\\"

if platform.system() == "Linux":
    SAPERATE = "/"

def current_path():
    return os.path.dirname(os.path.realpath(__file__))

def does_path_exist(path):
    return os.path.exists(os.path.join(current_path(), path))

def does_file_exist(file_path):
    return os.path.isfile(os.path.join(current_path(), file_path))

def does_directory_exist(directory_path):
    return os.path.isdir(os.path.join(current_path(), directory_path))

def does_ext_exist(ext_id):
    return does_file_exist(data_center.get_exts_folder() + SAPERATE + ext_id + ".json")

def does_node_exist(node_id):
    return does_file_exist(data_center.get_nodes_folder() + SAPERATE + node_id + ".json")

def load(file_path):
    file_path = os.path.join(current_path(), file_path)

    with open(file_path) as json_file:
        return json.load(json_file)

def save(file_path, data):
    file_path = os.path.join(current_path(), file_path)

    with open(file_path, "w") as outfile:
        json.dump(data, outfile)

def load_ext(ext_id):
    return load(data_center.get_exts_folder() + SAPERATE + ext_id + ".json")

def save_ext(ext_id, data):
    save(data_center.get_exts_folder() + SAPERATE + ext_id + ".json", data)

def load_node(node_id):
    return load(data_center.get_nodes_folder() + SAPERATE + node_id + ".json")

def save_node(node_id, data):
    save(data_center.get_nodes_folder() + SAPERATE + node_id + ".json", data)