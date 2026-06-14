from uuid import uuid4

from sqlalchemy import Boolean, Date
from sqlalchemy import DateTime, ForeignKey
from sqlalchemy import String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class MasterTask(Base):
    __tablename__ = "master_tasks"

    id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    task_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    user = relationship(
        "User",
        back_populates="master_tasks",
    )

    daily_logs = relationship(
        "DailyTaskLog",
        back_populates="task",
    )


class DailyTaskLog(Base):
    __tablename__ = "daily_task_logs"

    id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    task_id: Mapped[str] = mapped_column(
        ForeignKey("master_tasks.id"),
        nullable=False,
    )

    log_date: Mapped[Date] = mapped_column(
        Date,
        nullable=False,
    )

    status: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    task = relationship(
        "MasterTask",
        back_populates="daily_logs",
    )