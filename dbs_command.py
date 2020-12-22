import data_center
import message

def act(databases):
    message.normal_message("{:4s} {:24s} {:5s}".format("STT", "Name", "Count"))
    stt = 0
    for database in databases:
        stt += 1
        message.normal_message("{:4d} {:24s} {:5d}".format(stt, database , data_center.packet_count(database)))

def handle(command):
    if len(command) == 0:
        act(data_center.database_keys())
        return True

    for database in command:
        if not data_center.in_databases(database):
            message.error_message(database, "dbd")
            return False

    act(command)
    return True
