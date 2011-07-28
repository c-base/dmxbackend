from jsonrpc import jsonrpc_method
from django.core.files import File
import simplejson as json
import logging


@jsonrpc_method('lightSync.pull()')
def pullSend(request):
    f = open('lights.json', 'r+')
    jsonStoreFile = File(f)
    jsonStoreFile.seek(0)
    return jsonStoreFile.read()

@jsonrpc_method('lightSync.push(newLights=list)', validate=True)
def pushReceive(request, newLights=None):
    f = open('lights.json', 'r+')
    jsonStoreFile = File(f)
    jsonStoreFile.seek(0)
    jsonStore = json.loads(jsonStoreFile.read())
    lightsNotFound = []
    for newLight in newLights:
        foundLamp = False
        for storeLight in jsonStore:
            if(storeLight['name'] == newLight['name']):
                logging.debug("lampe %s r %d g %d b %d" % (storeLight['name'], storeLight['red'], storeLight['blue'], storeLight['green']))
                storeLight['red'] = newLight['red']
                storeLight['green'] = newLight['green']
                storeLight['blue'] = newLight['blue']
                foundLamp = True
        if not foundLamp:
            lightsNotFound.append(newLight['name'])

    if lightsNotFound:
        logging.warn("light %s not found !" % storeLight['name'])
    else:
        jsonStoreFile.seek(0)
        jsonStoreFile.write(json.dumps(jsonStore))
    return "Hello %d " % len(newLights)

@jsonrpc_method('myapp.gimmeThat', authenticated=True)
def something_special(request, secred_data):
    return {'sauce': ['authenticated', 'sauce']}

