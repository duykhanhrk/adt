import data_center
import json
import os
import platform
import random
import shutil

SEPARATE = "\\"

if platform.system() == "Linux":
    SEPARATE = "/"

def current_path():
    return os.path.dirname(os.path.realpath(__file__))

def does_path_exist(path):
    return os.path.exists(os.path.join(current_path(), path))

def does_file_exist(file_path):
    return os.path.isfile(os.path.join(current_path(), file_path))

def does_directory_exist(directory_path):
    return os.path.isdir(os.path.join(current_path(), directory_path))

def load(file_path):
    file_path = os.path.join(current_path(), file_path)

    with open(file_path) as json_file:
        return json.load(json_file)

def save(file_path, data):
    file_path = os.path.join(current_path(), file_path)

    with open(file_path, "w") as outfile:
        json.dump(data, outfile)

def copy(from_file_path, to_file_path):
    shutil.copyfile(from_file_path, to_file_path)

def delete(file_path):
    os.remove(file_path)

def make_string_id():
    chrs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
    str_id = ""
    for i in range(8):
        str_id += chrs[random.randint(0, 62)]

    return str_id

# ext and node
def does_ext_exist(ext_id):
    return does_file_exist(data_center.get_exts_folder() + SEPARATE + ext_id + ".ext_json")

def does_node_exist(node_id):
    return does_file_exist(data_center.get_nodes_folder() + SEPARATE + node_id + ".node_json")

def load_ext(ext_id):
    return load(data_center.get_exts_folder() + SEPARATE + ext_id + ".ext_json")

def save_ext(ext_id, data):
    save(data_center.get_exts_folder() + SEPARATE + ext_id + ".ext_json", data)

def add_ext(file_path):
    ext_id = make_string_id()
    while does_ext_exist(ext_id):
        ext_id = make_string_id()

    copy(file_path, data_center.get_exts_folder() + SEPARATE + ext_id + ".ext_json")

def delete_ext(ext_id):
    delete(data_center.get_exts_folder() + SEPARATE + ext_id + ".ext_json")

def load_node(node_id):
    return load(data_center.get_nodes_folder() + SEPARATE + node_id + ".node_json")

def save_node(node_id, data):
    save(data_center.get_nodes_folder() + SEPARATE + node_id + ".node_json", data)

def delete_node(node_id):
    delete(data_center.get_nodes_folder() + SEPARATE + node_id + ".node_json")

def is_true_ext_id(ext_id):
    chrs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
    for c in ext_id:
        if not c in chrs:
            return False
    return True

def exts():
    ext_jsons = []
    for _file in os.listdir(os.path.join(current_path(), data_center.get_exts_folder())):
        if _file.endswith(".ext_json"):
            if is_true_ext_id(_file[0:-9]):
                ext_jsons.append(_file[0:-9])
    return ext_jsons

def is_true_node_id(node_id):
    chrs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
    for c in node_id:
        if not c in chrs:
            return False
    return True

def nodes():
    node_jsons = []
    for _file in os.listdir(os.path.join(current_path(), data_center.get_nodes_folder())):
        if _file.endswith(".node_json"):
            if is_true_node_id(_file[0:-10]):
                node_jsons.append(_file[0:-10])
    return node_jsons
