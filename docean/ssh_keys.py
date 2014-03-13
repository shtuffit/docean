from .docean import build_path, get_do

def list_keys():
    return get_do('/ssh_keys/')

def add_key(name, pub_key):
    path = '/ssh_keys/new'
    return get_do(path, params={'name': name, 'ssh_pub_key': pub_key})

def key_action(key_id, action='', params={}):
    path = '/ssh_keys/' + str(key_id) +'/'
    if action:
        path += action + '/'
    return get_do(path, params=params)

def get_key(key_id):
    return key_action(key_id)

def edit(key_id, pub_key):
    return key_action(key_id, action='edit', params={'ssh_pub_key': pub_key})

def destroy(key_id):
    return key_action(key_id, action='destroy')

