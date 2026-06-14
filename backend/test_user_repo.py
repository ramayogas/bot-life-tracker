from app.database.database import SessionLocal
from repositories.user_repository import UserRepository

db = SessionLocal()

user = UserRepository.create(
    db=db,
    telegram_id=123456789,
    username="rama",
    first_name="Rama"
)

print(user.id)