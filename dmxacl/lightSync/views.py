from jsonrpc import jsonrpc_method
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from django.conf import settings

import simplejson as json
import logging
from sendtodmx import ArtNet

fs = FileSystemStorage(location=settings.MEDIA_ROOT)
artnet = ArtNet(broadcast=settings.ARTNETIP)

@jsonrpc_method('lightSync.pull()')
def pullSend(request):
    jsonStoreFile = fs.open('lights.json', 'r+')
    jsonStoreFile.seek(0)
    return jsonStoreFile.read()

@jsonrpc_method('lightSync.push(newLights=list)', validate=True)
def pushReceive(request, newLights=None):
    jsonStoreFile = fs.open('lights.json', 'r+')
    jsonStoreFile.seek(0)
    jsonStore = json.loads(jsonStoreFile.read())
    lightsNotFound = []
    for newLight in newLights:
        foundLamp = False
        for storeLight in jsonStore:
            if(storeLight['name'] == newLight['name']):
                logging.warn("lampe %s r %d g %d b %d" % (storeLight['name'], storeLight['red'], storeLight['blue'], storeLight['green']))
                storeLight['red'] = newLight['red']
                storeLight['green'] = newLight['green']
                storeLight['blue'] = newLight['blue']
                foundLamp = True
        if not foundLamp:
            lightsNotFound.append(newLight['name'])

    for lights in lightsNotFound:
        logging.warn("light %s not found !" % lights)
    jsonStoreFile.seek(0)
    jsonStoreFile.write(json.dumps(jsonStore))
    artnet.sendListToDMX(jsonStore)
    return "Hello %d " % len(newLights)

@jsonrpc_method('myapp.gimmeThat', authenticated=True)
def something_special(request, secred_data):
    return {'sauce': ['authenticated', 'sauce']}

