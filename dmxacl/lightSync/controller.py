from jsonrpc import jsonrpc_method
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from django.conf import settings

import simplejson as json
import logging
from sendtodmx import ArtNet

fs = FileSystemStorage(location=settings.MEDIA_ROOT)
artnet = ArtNet(broadcast=settings.ARTNETIP)

def loadLights():
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

def saveLights(jsonStore):
    jsonStoreFile = fs.open('lights.json', 'w')
    jsonStoreFile.write(json.dumps(jsonStore))
    jsonStoreFile.close()

def updateLights(newLights):
    jsonStore = loadLights()

    lightsNotFound = []
    for newLight in newLights:
        foundLamp = False
        for storeLight in jsonStore:
            if(storeLight['name'] == newLight['name']):
                storeLight['red'] = newLight['red']
                storeLight['green'] = newLight['green']
                storeLight['blue'] = newLight['blue']
                logging.debug("update: storeLight %s r %d g %d b %d" % (storeLight['name'], storeLight['red'], storeLight['blue'], storeLight['green']))
                logging.debug("update: newLight %s r %d g %d b %d" % (newLight['name'], newLight['red'], newLight['blue'], newLight['green']))
                foundLamp = True
        if not foundLamp:
            lightsNotFound.append(newLight['name'])

    for lights in lightsNotFound:
        logging.debug("light %s not found !" % lights)

    saveLights(jsonStore)

    logging.debug("new json data: %s" % json.dumps(jsonStore))
    artnet.send_light_list(jsonStore)

    return lightsNotFound
