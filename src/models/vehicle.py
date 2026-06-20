from .constants import Base
from sqlalchemy import String, DateTime, func, ARRAY
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class Vehicle(Base):
    __tablename__ = "vehicles"

    id: Mapped[int] = mapped_column(primary_key=True)
    model: Mapped[str] = mapped_column(String(100), nullable=False)
    version: Mapped[str] = mapped_column(String(100))
    year: Mapped[int] = mapped_column(nullable=False)
    price: Mapped[float]
    colors: Mapped[list[str]] = mapped_column(
        ARRAY(String), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(),
    onupdate=func.now(), nullable=False)
