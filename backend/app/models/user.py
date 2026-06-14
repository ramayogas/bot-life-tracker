from uuid import uuid4

from sqlalchemy import BigInteger, DateTime, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
from .base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    telegram_id: Mapped[int] = mapped_column(
        BigInteger,
        unique=True,
        nullable=False,
    )

    username: Mapped[Optional[str]] = mapped_column(
        String(100)
    )

    first_name: Mapped[Optional[str]] = mapped_column(
        String(100)
    )

    timezone: Mapped[str] = mapped_column(
        String(50),
        default="Asia/Makassar",
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    finance_transactions = relationship(
        "FinanceTransaction",
        back_populates="user",
    )

    health_logs = relationship(
        "HealthLog",
        back_populates="user",
    )

    master_tasks = relationship(
        "MasterTask",
        back_populates="user",
    )