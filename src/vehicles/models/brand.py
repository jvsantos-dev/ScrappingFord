
from sqlalchemy import String, DateTime, func, ARRAY
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from .constants import Base


class Brand(Base):
    __tablename__ = "brands"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    country: Mapped[str] = mapped_column(String(100), nullalbe=False)
    foundation_year: Mapped[int] = mapped_column(nullalbe=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)