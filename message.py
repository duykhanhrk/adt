ERROR = {
    "cmw": "This command wrong.",
    "cmd": "This command doesn't exist.",
    "dbe": "This database exists.",
    "dbd": "This database doesn't exist.",
    "nma": "This command doesn't accepted.",
    "fid": "This file doesn't exist.",
    "fic": "Couldn't load this file.",
    "drn": "No such directory.",
    "prn": "Couldn't find this property.",
    "ndn": "Couldn't find this node.",
    "nde": "This node already exists.",
    "dnn": "This name doesn't accepted.",
    "etn": "Couldn't find this ext.",
    "mpi": "Must be a positive integer",
    "sns": "This server is not supported",
    "cng": "Couldn't get data",
    "epd": "Error processing data"
}

STATUS = {
    "s": "SUCCESS",
    "e": "ERROR",
    "w": "WARNING"
}

MESSAGE_TRAY = []

# Echo
def normal_message(message_content):
    print(message_content)

def progress_message(status_code, message_content):
    print("{:10s}{}".format("[" + STATUS[status_code] + "]", message_content))

def error_message(error_obj, error_code):
    print(error_obj + ": " + ERROR[error_code])

def help_message(command_name, arguments, description):
    print("{:10s}{}\n{:10s}{}".format(command_name, arguments, "", description))

# Message tray
def add_message(message):
    MESSAGE_TRAY.append(message)

def can_show_messages():
    if len(MESSAGE_TRAY) == 0:
        return False

    return True

def show_messages():
    global MESSAGE_TRAY
    for message in MESSAGE_TRAY:     
        if (message["type"] == "error_message"):
            error_message(message["error_obj"], message["error_code"])
        elif (message["type"] == "progress_message"):
            progress_message(message["status_code"], message["message_content"])
        elif (message["type"] == "normal_message"):
            normal_message(message["message_content"])
        elif (message["type"] == "help_message"):
            help_message(message["command_name", "arguments", "description"])    
    MESSAGE_TRAY = []
