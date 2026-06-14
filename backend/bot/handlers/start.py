from telegram import Update
from telegram.ext import ContextTypes

from app.database.database import SessionLocal
from repositories.user_repository import UserRepository


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    db = SessionLocal()

    telegram_user = update.effective_user

    user = UserRepository.get_by_telegram_id(
        db,
        telegram_user.id,
    )

    if not user:
        user = UserRepository.create(
            db=db,
            telegram_id=telegram_user.id,
            username=telegram_user.username,
            first_name=telegram_user.first_name,
        )

    await update.message.reply_text(
        "Life Tracker aktif ✅"
    )

    db.close()