from datetime import date
from sqlalchemy.orm import Session

from app.models.finance import FinanceTransaction


class FinanceRepository:

    @staticmethod
    def create_income(
        db: Session,
        user_id,
        amount: float,
        category: str = None,
        notes: str = None,
    ):
        transaction = FinanceTransaction(
            user_id=user_id,
            transaction_date=date.today(),
            type="income",
            amount=amount,
            category=category,
            notes=notes,
        )

        db.add(transaction)
        db.commit()
        db.refresh(transaction)

        return transaction

    @staticmethod
    def create_expense(
        db: Session,
        user_id,
        amount: float,
        category: str = None,
        notes: str = None,
    ):
        transaction = FinanceTransaction(
            user_id=user_id,
            transaction_date=date.today(),
            type="expense",
            amount=amount,
            category=category,
            notes=notes,
        )

        db.add(transaction)
        db.commit()
        db.refresh(transaction)

        return transaction

    @staticmethod
    def get_all(
        db: Session,
        user_id,
    ):
        return (
            db.query(FinanceTransaction)
            .filter(
                FinanceTransaction.user_id == user_id
            )
            .all()
        )