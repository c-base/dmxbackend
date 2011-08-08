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

    try:
        jsonStore = json.loads(jsonStoreFile.read())
    except JSONDecodeError:
        # use defaults file
        defaultFile = fs.open('defaults.json', 'r')
        jsonStore = json.loads(defaultFile.read())
        defaultFile.close()

    jsonStoreFile.close()


    return jsonStore

@jsonrpc_method('lightSync.push(newLights=list)', validate=True)
def pushReceive(request, newLights=None):
    jsonStoreFile = fs.open('lights.json', 'r')

    try:
        jsonStore = json.loads(jsonStoreFile.read())
    except JSONDecodeError:
        # use defaults file
        defaultFile = fs.open('defaults.json', 'r')
        jsonStore = json.loads(defaultFile.read())
        defaultFile.close()

    jsonStoreFile.close()

    lightsNotFound = []
    for newLight in newLights:
        foundLamp = False
        for storeLight in jsonStore:
            if(storeLight['name'] == newLight['name']):
                storeLight['red'] = newLight['red']
                storeLight['green'] = newLight['green']
                storeLight['blue'] = newLight['blue']
                logging.warn("updated storeLight %s r %d g %d b %d" % (storeLight['name'], storeLight['red'], storeLight['blue'], storeLight['green']))
                logging.warn("updated   newLight %s r %d g %d b %d" % (newLight['name'], newLight['red'], newLight['blue'], newLight['green']))
                foundLamp = True
        if not foundLamp:
            lightsNotFound.append(newLight['name'])

    for lights in lightsNotFound:
        logging.warn("light %s not found !" % lights)
    jsonStoreFile.open(mode='w')
    jsonStoreFile.write(json.dumps(jsonStore))
    jsonStoreFile.close()
    logging.warn("new json data: %s" % json.dumps(jsonStore))
    artnet.sendListToDMX(jsonStore)
    return "Hello %d " % len(newLights)
