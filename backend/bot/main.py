import os

from dotenv import load_dotenv

from telegram.ext import (
    Application,
    CommandHandler,
)

from bot.handlers.start import start
from bot.handlers.finance import expense

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

app = Application.builder().token(TOKEN).build()

app.add_handler(
    CommandHandler(
        "start",
        start,
    )
)

app.add_handler(
    CommandHandler(
        "expense",
        expense,
    )
)

print("Bot running...")

app.run_polling()