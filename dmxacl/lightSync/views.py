from controller import *

@jsonrpc_method('lightSync.pull()')
def pullSend(request):
    return loadLights()

@jsonrpc_method('lightSync.push(newLights=list)', validate=True)
def pushReceive(request, newLights=None):
    return updateLights(newLights)
