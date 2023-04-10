from aiohttp import web

from app.service.tg.bot import new_app
from app.settings import TG_TOKEN, TG_USE_WEBHOOK, TG_HOST

from telegram import Update


app_tg = new_app(TG_TOKEN, TG_USE_WEBHOOK, TG_HOST)


async def telegram_handle(request):
    json = await request.json()
    update = Update.de_json(json, app_tg.bot)

    await app_tg.process_update(update)

    return web.Response()
