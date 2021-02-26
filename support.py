import data_center
import storage
import requests

# Get data
def get_data_from_url(url):
    r = requests.get(url)
    return r.text

# ext
def options_ext(url):
    options = []
    exts = storage.exts()

    for ext in exts:
        ext_json = storage.load_ext(ext)
        if ext_json.server in url:
            options.append(ext)
    
    return options
    
def choose_ext(url):
    exts = storage.exts()

    for ext in exts:
        ext_json = storage.load_ext(ext)
        if ext_json['server'] in url:
            return ext
    
    return None

def does_ext_support_server(ext_id, url):
    ext_json = storage.load_ext(ext_id)
    if ext_json.server in url:
        return True
    
    return False

# Num

def to_int(str):
    try:
        return int(str)
    except:
        return None

# Str

def map_vari(vari_str, varis):
    for vari in varis:
        vari_str = vari_str.replace(vari["var"], str(vari["value"]))

    return vari_str
