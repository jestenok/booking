from telegram import Update


async def reply(update: Update, context=None):
    if len(update.message.reply_to_message.entities) == 0:
        return
