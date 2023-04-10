from telegram import Update


async def start(update: Update, _) -> None:
    u = update.message.from_user.first_name
    await update.message.reply_html(rf"Hi {u}!")


async def not_found(update: Update, _) -> None:
    await update.message.reply_text("Команда не найдена")
