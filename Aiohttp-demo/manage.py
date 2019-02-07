from aiohttp import web

from app import create_app
from app.routes import add_rules


app = create_app()

add_rules(app)

if __name__ == '__main__':
    web.run_app(app)

