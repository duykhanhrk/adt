import data_center
import message

def view_role(data, end_with = "\n"):
    if type(data) == list:
        for item in data:
            if type(item) == dict or type(item) == list:
                print("")
                view_role(item)
                print("")
            else:
                view_role(item, end_with=", ")
    elif type(data) == dict:
        for key in data.keys():
            print(key, end = ": ")
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