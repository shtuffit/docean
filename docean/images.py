from .docean import build_path, get_do

def list_images():
    return get_do('/images/')

def image_action(image_id, action='', params={}):
    path = '/images/' + image_id + '/'
    if action:
        path += action + '/'
    return get_do(path, params=params)

def get_image(image_id):
    return image_action(image_id)

def destroy(image_id):
    return image_action(image_id, action='destroy')

def transfer(image_id, region_id):
    return image_action(image_id, action='transfer', params={'region_id': region_id})

