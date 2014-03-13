docean
======

Python Wrapper for the Digital Ocean API

##Supported Actions

* Droplets
* Regions
* Images
* SSH_Keys
* Sizes
* Domains
* Events

##Dependencies

Currently the only dependecy is requests

```
pip install requests
```

##Usage

1) Create a config file in your home directory named .docean, needs the base api url, client_id and api_key

```
$ cat ~/.docean

{
  "base_url":	"https://api.digitalocean.com",
  "client_id":	"Vbk14dTVNqhvodGCEXZ14EbMpyGegk489",
  "api_key":	"GDzvx2vLqClqKeCFxCsGQNxZ6q5ndXcEc"
}

```

2) import the desired service and you should be GTG 

```python
>>> from docean import droplets, images, ssh_keys
>>>
>>> droplets.list_droplets()
{u'status': u'OK', u'droplets': []}
>>>
>>> ssh_keys.list_keys()
{u'status': u'OK', u'ssh_keys': []}
>>>
>>> images.list_images()
{u'status': u'OK', u'images': [{u'name': u'CentOS 5.8 x64', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 1601, u'distribution': u'CentOS', u'slug': u'centos-5-8-x64'}, {u'name': u'CentOS 5.8 x32', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 1602, u'distribution': u'CentOS', u'slug': u'centos-5-8-x32'}, {u'name': u'Debian 6.0 x64', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 12573, u'distribution': u'Debian', u'slug': u'debian-6-0-x64'}, {u'name': u'Debian 6.0 x32', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 12575, u'distribution': u'Debian', u'slug': u'debian-6-0-x32'}, {u'name': u'Ubuntu 10.04 x64', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 14097, u'distribution': u'Ubuntu', u'slug': u'ubuntu-10-04-x64'}, {u'name': u'Ubuntu 10.04 x32', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 14098, u'distribution': u'Ubuntu', u'slug': u'ubuntu-10-04-x32'}, {u'name': u'Fedora 17 x32', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 32387, u'distribution': u'Fedora', u'slug': u'fedora-17-x32'}, {u'name': u'Fedora 17 x32 Desktop', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 32399, u'distribution': u'Fedora', u'slug': u'fedora-17-x32-desktop'}, {u'name': u'Fedora 17 x64 Desktop', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 32419, u'distribution': u'Fedora', u'slug': u'fedora-17-x64-desktop'}, {u'name': u'Fedora 17 x64', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 32428, u'distribution': u'Fedora', u'slug': u'fedora-17-x64'}, {u'name': u'Debian 7.0 x32', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 303619, u'distribution': u'Debian', u'slug': u'debian-7-0-x32'}, {u'name': u'Debian 7.0 x64', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 308287, u'distribution': u'Debian', u'slug': u'debian-7-0-x64'}, {u'name': u'Ubuntu 13.04 x32', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 345791, u'distribution': u'Ubuntu', u'slug': u'ubuntu-13-04-x32'}, {u'name': u'Ubuntu 13.04 x64', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 350076, u'distribution': u'Ubuntu', u'slug': u'ubuntu-13-04-x64'}, {u'name': u'Arch Linux 2013.05 x64', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 350424, u'distribution': u'Arch Linux', u'slug': u'arch-linux-2013-05-x64'}, {u'name': u'Arch Linux 2013.05 x32', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 361740, u'distribution': u'Arch Linux', u'slug': u'arch-linux-2013-05-x32'}, {u'name': u'CentOS 6.4 x32', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 376568, u'distribution': u'CentOS', u'slug': u'centos-6-4-x32'}, {u'name': u'Ubuntu 12.10 x32', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 433240, u'distribution': u'Ubuntu', u'slug': u'ubuntu-12-10-x32'}, {u'name': u'LAMP on Ubuntu 12.04', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 459444, u'distribution': u'Ubuntu', u'slug': u'lamp-ubuntu-12.04'}, {u'name': u'Ubuntu 12.10 x64', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 473123, u'distribution': u'Ubuntu', u'slug': u'ubuntu-12-10-x64'}, {u'name': u'Ubuntu 12.10 x64 Desktop', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 473136, u'distribution': u'Ubuntu', u'slug': u'ubuntu-12-10-x64-desktop'}, {u'name': u'CentOS 6.4 x64', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 562354, u'distribution': u'CentOS', u'slug': u'centos-6-4-x64'}, {u'name': u'Fedora 19 x64', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 696598, u'distribution': u'Fedora', u'slug': u'fedora-19-x64'}, {u'name': u'Fedora 19 x32', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 697056, u'distribution': u'Fedora', u'slug': u'fedora-19-x32'}, {u'name': u'Ubuntu 13.10 x32', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 962304, u'distribution': u'Ubuntu', u'slug': u'ubuntu-13-10-x32'}, {u'name': u'MEAN on Ubuntu 12.04.3', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 1420643, u'distribution': u'Ubuntu', u'slug': u'mean-ubuntu-12.04'}, {u'name': u'Ubuntu 12.04.3 x64', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 1505447, u'distribution': u'Ubuntu', u'slug': u'ubuntu-12-04-x64'}, {u'name': u'Ubuntu 12.04.3 x32', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 1505527, u'distribution': u'Ubuntu', u'slug': u'ubuntu-12-04-x32'}, {u'name': u'Ubuntu 13.10 x64', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 1505699, u'distribution': u'Ubuntu', u'slug': u'ubuntu-13-10-x64'}, {u'name': u'Ruby on Rails on Ubuntu 12.10 (Nginx + Unicorn)', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 1608711, u'distribution': u'Ubuntu', u'slug': u'rails-unicorn-nginx-ubuntu-12.10'}, {u'name': u'CentOS 6.5 x64', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 1646467, u'distribution': u'CentOS', u'slug': u'centos-6-5-x64'}, {u'name': u'CentOS 6.5 x32', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 1646732, u'distribution': u'CentOS', u'slug': u'centos-6-5-x32'}, {u'name': u'Redmine on Ubuntu 12.04', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 1687372, u'distribution': u'Ubuntu', u'slug': u'redmine-ubuntu-12.04'}, {u'name': u'Ghost 0.4.0 on Ubuntu 12.04', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 1860934, u'distribution': u'Ubuntu', u'slug': u'ghost-ubuntu-12.04'}, {u'name': u'GitLab 6.5.1 CE', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 2105243, u'distribution': u'Ubuntu', u'slug': u'gitlab-ubuntu-13.10'}, {u'name': u'Dokku-v0.2.1 on Ubuntu 13.04', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 2118237, u'distribution': u'Ubuntu', u'slug': u'dokku-ubuntu-13.04'}, {u'name': u'Docker 0.8 Ubuntu 13.04 x64', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 2158507, u'distribution': u'Ubuntu', u'slug': u'docker-ubuntu-13.04-x64'}, {u'name': u'Wordpress on Ubuntu 13.10', u'region_slugs': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1'], u'public': True, u'regions': [1, 2, 3, 4, 5, 6], u'id': 2377834, u'distribution': u'Ubuntu', u'slug': None}]}
```
