#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import os
import json
import asyncio
import logging
import aiohttp
from aiohttp import web
from PIL import Image
from io import BytesIO
from dmxbackend import channel_state


log = logging.getLogger(__name__)
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
log.addHandler(ch)

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), '..')
image_queue = None

# TODO: Deleteme
light_mapping = None


async def handle_index(request):
    path=os.path.join(PROJECT_ROOT, 'static/index.html')
    with open(path, mode="r") as index_file:
        return web.Response(body=index_file.read(), content_type="text/html")


async def retrieve_image(post_data):
    file = post_data['file'].file
    content = BytesIO(file.read())
    image = Image.open(content).convert('RGBA')
    return image


async def handle_post(request):
    global image_queue
    post_data = await request.post()
    image = await retrieve_image(post_data)
    await image_queue.put(image)
    return web.json_response(data={'success': True, 'message': 'Uploaded'})


async def fixtures(request):
    ret = channel_state.fixtures()
    def dump(data, *args, **kwargs):
        return json.dumps(data, indent=4, *args, **kwargs)
    return web.json_response(ret, dumps=dump)


async def get_state(request):
    return web.json_response(channel_state.as_dict())


async def websocket_handler(request):
    log.debug("Websocket handler called")
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    ws.send_json(channel_state.as_list())

    async def on_update():
        if not ws.closed:
            ws.send_json(channel_state.as_list())
    channel_state.subscribe(on_update)

    async for msg in ws:
        log.debug("Got message %s" % msg.data)
        if msg.type == aiohttp.WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            else:
                new_data = json.loads(msg.data)
                log.debug("new data is type {}".format(type(new_data)))
                channel_state.update_channels(new_data)
        elif msg.type == aiohttp.WSMsgType.ERROR:
            log.warning('ws connection closed with exception %s' %
                  ws.exception())

    print('websocket connection closed')

    return ws


def setup_web_app(queue, mapping):
    global image_queue
    
    # TODO: Deleteme
    global light_mapping
    
    light_mapping = mapping
    image_queue = queue
    app = web.Application()
    app.router.add_get('/api/v1/fixtures/', fixtures)
    app.router.add_get('/api/v1/websocket_state/', websocket_handler)
    app.router.add_get('/api/v1/state/', get_state)
    app.router.add_static('/assets',
                          path=os.path.join(PROJECT_ROOT, 'static/assets'),
                          name='static')
    app.router.add_post('/', handle_post)
    # Catch all
    r = app.router.add_resource(r'/{name:.*}')
    r.add_route('GET', handle_index)
    return app
