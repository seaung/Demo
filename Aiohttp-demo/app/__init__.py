import aiohttp_jinja2
import jinja2
from aiohttp import web

from app.settings import config


def create_app():
    app = web.Application()
    app['config'] = config
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.PackageLoader('app', 'templates')
    )
    return app

