import asyncio
import atexit

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
)

from .handlers import (
    commands,
    photo,
    text,
    callback,
    reply
)


def new_app(token, use_webhook=False, host=None):
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler('start', commands.start))

    app.add_handler(CallbackQueryHandler(callback.callback_query))

    app.add_handler(MessageHandler(filters.PHOTO, photo.photo))
    app.add_handler(MessageHandler(filters.REPLY, reply.reply))
    app.add_handler(MessageHandler(filters.TEXT, text.text))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(app.initialize())

    if use_webhook:
        loop.run_until_complete(app.bot.set_webhook(f'{host}/jira-telegram-bot/{token}/'))
        atexit.register(
            lambda: loop.run_until_complete(
                app.bot.delete_webhook(f'{host}/jira-telegram-bot/{token}/')))
    elif host:
        loop.run_until_complete(app.bot.delete_webhook(f'{host}/jira-telegram-bot/{token}/'))

    return app
