docean
======

Python Wrapper for the Digital Ocean API

#Supported Actions

*Droplets
*Regions
*Images
*SSH_Keys
*Sizes
*Domains
*Events

Currently the only dependecy is requests

```
pip install requests
```

#Usage

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
>>> from docean import droplets
>>> droplets.list_droplets()
{u'status': u'OK', u'droplets': []}
```
