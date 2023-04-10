from aiohttp import web

from .handlers.tg import telegram_handle


def create_routes(token):
    routes = [web.post(f'/jira-telegram-bot/{token}/', telegram_handle)]
    return routes
