import aiohttp_jinja2
from aiohttp import web


async def handle_404(request):
    return aiohttp_jinja2.render_template('404.html', request, {})


async def handle_500(request):
    return aiohttp_jinja2.render_template('500.html', request, {})


def create_error_middleware(overrides):
    @web.middleware
    async def error_middleware(request, heandler):
        try:
            response = await handler(request)
            override = overrides.get(response.status)
            if override:
                return await override(request)
            return response
        except web.HTTPException as e:
            override = overrides.get(e.status)
            if override:
                return await override(request)

            raise
    return error_middleware
