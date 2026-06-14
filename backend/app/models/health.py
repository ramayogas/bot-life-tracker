from typing import Optional
from uuid import uuid4

from sqlalchemy import Date, DateTime, ForeignKey
from sqlalchemy import Integer, Numeric, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class HealthLog(Base):
    __tablename__ = "health_logs"

    id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    log_date: Mapped[Date] = mapped_column(
        Date,
        nullable=False,
    )

    weight_kg: Mapped[Optional[float]] = mapped_column(
        Numeric(5, 2)
    )

    height_cm: Mapped[Optional[float]] = mapped_column(
        Numeric(5, 2)
    )

    systolic_bp: Mapped[Optional[int]] = mapped_column(
        Integer
    )

    diastolic_bp: Mapped[Optional[int]] = mapped_column(
        Integer
    )

    body_temp_c: Mapped[Optional[float]] = mapped_column(
        Numeric(4, 1)
    )

    heart_rate: Mapped[Optional[int]] = mapped_column(
        Integer
    )

    spo2: Mapped[Optional[int]] = mapped_column(
        Integer
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
        back_populates="health_logs",
    )