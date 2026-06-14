from typing import Optional
from uuid import uuid4

from sqlalchemy import Date, DateTime, ForeignKey
from sqlalchemy import Numeric, String, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class FinanceTransaction(Base):
    __tablename__ = "finance_transactions"

    id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    transaction_date: Mapped[Date] = mapped_column(
        Date,
        nullable=False,
    )

    type: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )  # income / expense

    amount: Mapped[float] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    category: Mapped[Optional[str]] = mapped_column(
        String(100)
    )

    notes: Mapped[Optional[str]] = mapped_column(
        Text
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    user = relationship(
        "User",
        back_populates="finance_transactions",
    )