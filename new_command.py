import data_center
import message

def act(database, options):
    if not options["--r"] and data_center.in_databases(database):
        message.error_message(database, "dbe")
        return False

    if not data_center.is_true_database_name(database):
        message.error_message(database, "dnn")
        return False

    data_center.append_database(database, [])
    return True

def handle(command):
    options = {"--r": False}
    if "--r" in command:
        options["--r"] == True
        command.remove("--r")

    if len(command) == 0:
        message.error_message("DB::NULL", "cmw")
        return False

    if len(command) == 1:
        return act(command[0], options)

    message.error_message(command[1], "cmw")
