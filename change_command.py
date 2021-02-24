import data_center
import message

default_options = {
    "method": "--g"
}

def act(database, from_database, options):
    if not data_center.in_databases(database):
        message.error_message(database, "dbd")
        return False

    if not data_center.in_databases(from_database):
        message.error_message(from_database, "dbd")
        return False

    if options["method"] == "--g":
        data_center.copy_database(database, from_database)
        return True

    if options["method"] == "--i":
        data_center.add_databases(database, from_database)
        return True

    if options["method"] == "--m":
        data_center.merge_databases(database, from_database)
        return True
    
    return False

def handle(command):
    options = default_options

    if "--g" in command:
        options["method"] = "--g"
        command.remove("--g")
    elif "--i" in command:
        options["method"] = "--i"
        command.remove("--i")
    elif "--u" in command:
        options["method"] = "--u"
        command.remove("--u")

    if len(command) == 0:
        message.error_message("DB::NULL", "cmw")
        return False

    if len(command) == 1:
        message.error_message("FROM_DB:NULL", "cmw")
        return False

    if len(command) == 2:
        return act(command[0], command[1], options)

    message.error_message(command[2], "cmw")
    return False
