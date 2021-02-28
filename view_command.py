import data_center
import message

def view_role(data, end_with = "\n", after_print = None, before_print = None):
    if type(data) == list:
        # before print
        if before_print != None:
            print(before_print, end=end_with)

        # print
        for item in data:
            if type(item) == dict:
                print("")
                view_role(item)
                print("")
            elif type(item) == list:
                view_role(item, before_print="\n", after_print="\b\b ", end_with="")
                print("")
            else:
                view_role(item, end_with=", ")

        # after print
        if after_print != None:
            print(after_print, end=end_with)
    elif type(data) == dict:
        for key in data.keys():
            print(key, end = ": ")
            if type(data[key]) == list:
                view_role(data[key], after_print="\b\b ")
            else:
                view_role(data[key])
    else:
        print(data, end=end_with)

def act(db_id):
    db = data_center.get_database(db_id)
    view_role(db)

def handle(command):
    if len(command) == 0:
        message.error_message("DB::NULL", "cmw")
        return False

    if len(command) == 1:
        if not data_center.in_databases(command[0]):
            message.error_message(command[0], 'dbd')
            return  False
        return act(command[0])

    message.error_message(command[1], "cmw")
    return False