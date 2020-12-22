CONFIG = { }

DATABASES = { }

MESSAGE_TRAY = [ ]

# config
def get_exts_folder():
    return CONFIG["exts_folder"]

def get_nodes_folder():
    return CONFIG["nodes_folder"]

def get_current_node():
    return CONFIG["current_node"]

def set_current_node(node):
    CONFIG["current_node"] = node

def save_config():
    pass

# Database
def packet_count(database):
    return DATABASES[database].size()

def get_packet(database, index):
    return DATABASES[database][index]

def set_packet(database, index, data):
    DATABASES[database][index] = data

def append_packet(database, packet):
    DATABASES[database].append(packet)

def database_count():
    return DATABASES.keys().size()

def database_keys():
    return DATABASES.keys()

def get_database(database):
    return database

def set_database(database, data):
    DATABASES[database] = data

def append_database(database, data):
    DATABASES[database] = data

def add_databases(into_database, from_database):
    DATABASES[into_database] = DATABASES[into_database] + DATABASES[from_database]

def ufity_databases(into_database, from_database):
    for data in DATABASES[from_database]:
        if not data in DATABASES[into_database]:
            DATABASES[into_database].append(data)