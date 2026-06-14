from telegram import Update
from telegram.ext import ContextTypes

from app.database.database import SessionLocal

from repositories.user_repository import UserRepository
from repositories.finance_repository import FinanceRepository

async def expense(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    try:
        amount = float(context.args[0])

        note = " ".join(context.args[1:])

        db = SessionLocal()

        user = UserRepository.get_by_telegram_id(
            db,
            update.effective_user.id,
        )

        tx = FinanceRepository.create_expense(
            db=db,
            user_id=user.id,
            amount=amount,
            notes=note,
        )

        await update.message.reply_text(
            f"Expense Rp{amount:,.0f} tersimpan"
        )

        db.close()

    except Exception as e:
        await update.message.reply_text(
            str(e)
        )