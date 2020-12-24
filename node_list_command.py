import data_center
import message
import storage

def act(nodes):
    message.normal_message("{:4s} {}".format("STT", "Node"))
    stt = 0
    for node in nodes:
        stt += 1
        node_json = storage.load_node(node)
        message.normal_message("{:4d} {}".format(stt, "Id: " + node))
        message.normal_message("{:4s} {}".format("", "Name: " + node_json["name"]))

def handle(command):
    if len(command) == 0:
        act(storage.nodes())
        return True

    message.error_message(command[0], "cmw")
