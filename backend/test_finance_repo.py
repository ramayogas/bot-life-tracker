from app.database.database import SessionLocal

from repositories.user_repository import UserRepository
from repositories.finance_repository import FinanceRepository

db = SessionLocal()

user = UserRepository.get_by_telegram_id(
    db,
    123456789
)

tx = FinanceRepository.create_expense(
    db=db,
    user_id=user.id,
    amount=50000,
    category="Food",
    notes="Bakso"
)

print(tx.id)