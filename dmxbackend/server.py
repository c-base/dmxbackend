#!/usr/bin/env python3
import os
import asyncio
from aiohttp import web
from PIL import Image
from io import BytesIO

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), '..')
image_queue = None


async def handle_get(request):
    # name = request.match_info.get('name', "Anonymous")
    text = "OK, Content-Type: " + request.content_type
    return web.Response(text=text)


async def retrieve_image(post_data):
    file = post_data['file'].file
    content = BytesIO(file.read())
    image = Image.open(content).convert('RGBA')
    return image


async def handle_post(request):
    global image_queue
    post_data = await request.post()
    message = "{} uploaded".format(post_data['file'].filename)
    image = await retrieve_image(post_data)
    await image_queue.put(image)
    return web.json_response(data={'success': True, 'message': message})


def setup_web_app(queue):
    global image_queue
    image_queue = queue
    app = web.Application()
    app.router.add_get('/', handle_get)
    app.router.add_post('/', handle_post)
    app.router.add_static('/static/',
                      path=os.path.join(PROJECT_ROOT, 'static'),
                      name='static')
    return app
