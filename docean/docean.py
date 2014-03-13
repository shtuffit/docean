import json
from os.path import expanduser
import json
import requests

home = expanduser("~")
f = open(home+'/.docean')
conf = json.load(f)

def get_do(path, params = {}):
    url = conf['base_url'] + path
    params.update({
     'client_id': conf['client_id'],
     'api_key': conf['api_key']
    })
    return json.loads(requests.get(url, params=params).text)

def build_path(items=[]):
    path = "/"
    for i in items:
        path += str(i) + '/'
    return path

def list_regions():
    return get_do('/regions/')

def list_sizes():
    return get_do('/sizes/')

def get_event(event_id):
    return get_do('/events/')

