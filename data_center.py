import storage

CONFIG = { }

DATABASES = { }

# config
def in_config(config):
    return config in CONFIG

def get_exts_folder():
    return CONFIG["exts_folder"]

def get_nodes_folder():
    return CONFIG["nodes_folder"]

def get_current_node():
    return CONFIG["current_node"]

def set_current_node(node):
    CONFIG["current_node"] = node

def load_config():
    global CONFIG
    CONFIG = storage.load("config.json")
    return True

def save_config():
    storage.save(CONFIG["config_file"], CONFIG)

# Database
def packet_count(database):
    return len(DATABASES[database])

def get_packet(database, index):
    return DATABASES[database][index]

def set_packet(database, index, data):
    DATABASES[database][index] = data

def append_packet(database, packet):
    DATABASES[database].append(packet)

def database_count():
    return len(DATABASES.keys())

def database_keys():
    return DATABASES.keys()

def is_true_database_name(database_name):
    chrs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
    for c in database_name:
        if not c in chrs:
            return False
    return True

def in_databases(database):
    return database in DATABASES

def get_database(database):
    return database

def set_database(database, data):
    DATABASES[database] = data

def append_database(database, data):
    DATABASES[database] = data

def remove_database(database):
    del DATABASES[database]

def copy_database(database, from_database):
    DATABASES[database] = DATABASES[from_database]

def add_databases(into_database, from_database):
    DATABASES[into_database] = DATABASES[into_database] + DATABASES[from_database]

def merge_databases(into_database, from_database):
    for data in DATABASES[from_database]:
        if not data in DATABASES[into_database]:
            DATABASES[into_database].append(data)

def load_node():
    global DATABASES
    node = storage.load_node(get_current_node())
    DATABASES = node["databases"]
    return True

def save_node(node_name):
    storage.save_node(node_name, { "name": node_name, "databases": DATABASES })
