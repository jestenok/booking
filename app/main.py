from settings import TG_TOKEN, TG_USE_WEBHOOK, TG_HOST
from remote.http.router import create_routes
from remote.http.middleware import log_middleware
from service.tg.bot import new_app

from aiohttp import web
import logging


if __name__ == '__main__':
    if TG_USE_WEBHOOK:
        logging.info('Starting webhook')
        app = web.Application()
        app.add_routes(create_routes(TG_TOKEN))
        app.middlewares.append(log_middleware)

        web.run_app(app,
                    access_log=None,
                    port=8080)
    else:
        logging.info('Starting polling')
        app_tg = new_app(TG_TOKEN, TG_USE_WEBHOOK, TG_HOST)
        app_tg.run_polling()
