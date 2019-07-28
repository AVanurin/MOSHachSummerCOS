import time
import base64
from cryptography import fernet
from aiohttp import web
from aiohttp_session import setup, get_session, session_middleware
from aiohttp_session.cookie_storage import EncryptedCookieStorage
import aiohttp_jinja2
import jinja2

import handlers

async def handle_get_form(request):
    session = await get_session(request)

    return web.Response(text="Hello world")


def build():
    app = web.Application()

    aiohttp_jinja2.setup(app,
    loader=jinja2.FileSystemLoader('templates'))
    #app["static_root_url"] = '/static'
    #app.router.add_static('/static', settings.STATIC_DIR, name='static')

    fernet_key = fernet.Fernet.generate_key()
    secret_key = base64.urlsafe_b64decode(fernet_key)
    setup(app, EncryptedCookieStorage(secret_key))

    app.add_routes([web.get("/", handlers.index)])
    app.add_routes([web.get("/form", handlers.form)])
    app.add_routes([web.post("/form", handlers.post_form)])
    app.add_routes([web.get("/admin/tasks", handlers.admin_all_task)])
    app.add_routes([web.get("/task/{id}", handlers.solution)])

    app.add_routes([web.get("/res/logo", handlers.static_pic_logo)])

    return app


if __name__ == "__main__":
    web.run_app(build())

