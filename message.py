ERROR = {
    "cmw": "This command wrong."
    "cmd": "This command doesn't exist.",
    "dbe": "This database exists.",
    "dbd": "This database doesn't exist.",
    "nma": "This command doesn't accepted."
}

STATUS = {
    "s": "SUCCESS",
    "e": "ERROR",
    "w": "WARNING"
}

def message(message_content):
    print(message_content)

def progress_message(status_code, message_content):
    print("{:10s}{}".format("[" + STATUS[status_code] + "]", message_content))

def error_message(error_obj, error_code):
    print(error_obj + ": " + message_content)