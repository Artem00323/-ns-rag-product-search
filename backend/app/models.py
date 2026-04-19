from datetime import datetime

from pgvector.sqlalchemy import Vector
from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

EMBEDDING_DIM = 384  # multilingual-e5-small


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    external_id: Mapped[str | None] = mapped_column(String(128), unique=True, index=True)
    name: Mapped[str] = mapped_column(String(512), nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    category: Mapped[str | None] = mapped_column(String(128), index=True)
    gender: Mapped[str | None] = mapped_column(String(32), index=True)
    color: Mapped[str | None] = mapped_column(String(64))
    material: Mapped[str | None] = mapped_column(String(128))
    price: Mapped[float | None] = mapped_column(Numeric(10, 2), index=True)
    image_url: Mapped[str | None] = mapped_column(Text)
    product_url: Mapped[str | None] = mapped_column(Text)
    embedding: Mapped[list[float] | None] = mapped_column(Vector(EMBEDDING_DIM))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )


class Query(Base):
    __tablename__ = "queries"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    llm_response: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    feedback: Mapped[list["Feedback"]] = relationship(back_populates="query")


class Feedback(Base):
    __tablename__ = "feedback"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    query_id: Mapped[int] = mapped_column(ForeignKey("queries.id", ondelete="CASCADE"))
    product_id: Mapped[int | None] = mapped_column(ForeignKey("products.id", ondelete="SET NULL"))
    rating: Mapped[int] = mapped_column(Integer, nullable=False)  # 1 or -1
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    query: Mapped["Query"] = relationship(back_populates="feedback")
