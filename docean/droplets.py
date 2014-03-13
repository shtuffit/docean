from .docean import build_path, get_do

def list_droplets():
    return get_do('/droplets/')

def droplet_action(droplet_id, action='', params={}):
    path = '/droplets/' + droplet_id + '/'
    if action:
        path += action + '/'
    return get_do(path, params=params)

def get_droplet(droplet_id):
    return droplet_action(droplet_id)

def reboot(droplet_id):
    return droplet_action(droplet_id, action='reboot')

def power_cycle(droplet_id):
    return droplet_action(droplet_id, action='power_cycle')

def shutdown(droplet_id):
    return droplet_action(droplet_id, action='shutdown')

def power_off(droplet_id):
    return droplet_action(droplet_id, action='power_off')

def power_on(droplet_id):
    return droplet_action(droplet_id, action='power_on')

def password_reset(droplet_id):
    return droplet_action(droplet_id, action='password_reset')

def resize(droplet_id, size_id=None, size_slug=None):
    if size_id is not None:
        params = {'size_id': size_id}
    elif size_slug is not None:
        params = {'size_slug': size_slug}
    return droplet_action(droplet_id, action='resize', params=params)

def snapshot(droplet_id, name):
    return droplet_action(droplet_id, action='snapshot', params={'name': name})

def restore(droplet_id, image_id):
    return droplet_action(droplet_id, action='restore', params={'image_id': image_id})

def rebuild(droplet_id, image_id):
    return droplet_action(droplet_id, action='rebuild', params={'image_id': image_id})

def rename(droplet_id, name):
    return droplet_action(droplet_id, action='rename', params={'name': name})

def destroy(droplet_id, scrub_data=True):
    return droplet_action(droplet_id, action='destroy', params={'scrub_data': scrub_data})
