import data_center
import message
import storage

def act(exts):
    message.normal_message("{:4s} {}".format("STT", "Ext"))
    stt = 0
    for ext in exts:
        stt += 1
        ext_json = storage.load_ext(ext)
        message.normal_message("{:4d} {}".format(stt, "Id: " + ext))
        message.normal_message("{:4s} {}".format("", "Name: " + ext_json["name"]))
        message.normal_message("{:4s} {}".format("", "Version: " + ext_json["version"]))
        message.normal_message("{:4s} {}".format("", "Server: " + ext_json["server"]))
        message.normal_message("{:4s} {}".format("", "Detail: " + ext_json["detail"]))

def handle(command):
    if len(command) == 0:
        act(storage.exts())
        return True

    message.error_message(command[0], "cmw")
    return False
