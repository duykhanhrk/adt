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
def get_database(database):
    return database

def set_database(database, data):
    DATABASES[database] = database

def add_database(into_database, from_database):
    DATABASES[into_database] = DATABASES[into_database] + DATABASES[from_database]

def ufity_database(into_database, from_database):
    pass