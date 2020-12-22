import data_center
import message

def act(database):
    if not data_center.in_databases(database):
        message.error_message(database, "dbd")
        return False

    data_center.remove_database(database)
    return True

def handle(command):
    if len(command) == 0:
        message.error_message("DB::NULL", "cmw")
        return False

    if len(command) == 1:
        return act(command[0])

    message.error_message(command[1], "cmw")
    return False
