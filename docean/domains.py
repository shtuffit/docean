from .docean import get_do

def list_domains():
    return get_do('/domains/')

def add_domain(name, ip_address):
    return get_do('/new/', params={'name': name, 'ip_address': ip_address})

def domain_action(domain_id, action='', extrapath='', params={}):
    path = '/domains/' + domain_id +'/'
    if action:
        path += action + '/'
    return get_do(path, params=params)

def get_domain(domain_id):
    return domain_action(domain_id)

def destroy(domain_id):
    return domain_action(domain_id, action='destroy')

def list_domain_records(domain_id):
    return domain_action(domain_id, action='records')

def domain_record_action(domain_id, record_id, action='', params={}):
    extrapath = 'records/' + record_id +'/'
    if action:
        extrapath += action 
    return domain_action(domain_id, action=extrapath, params=params)

def add_domain_record(domain_id, record_type, data, name=None, priority=None, port=None, weight=None):
    params = {'record_type': record_type, 'data': data}
    if name:
        params.update({'name': name})
    if priority:
        params.update({'priority': priority})
    if port:
        params.update({'port': port})
    if weight:
        params.update({'port': weight})
    return get_do('/domains/'+domain_id+'/records/new', params=params)

def get_domain_record(domain_id, record_id):
    return domain_record_action(domain_id, record_id)
    
def edit_domain_record(domain_id, record_id, record_type, data, name=None, priority=None, weight=None):
    params = {'record_type': record_type, 'data': data}
    if name:
        params.update({'name': name})
    if priority:
        params.update({'priority': priority})
    if port:
        params.update({'port': port})
    if weight:
        params.update({'port': weight})
    return get_do('/domains/'+domain_id+'/records/'+record_id+'/edit', params=params)

def destroy_domain_record(domain_id, record_id):
    return domain_record_action(domain_id, record_id)
