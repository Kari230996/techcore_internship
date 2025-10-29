from typing import Optional
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase


class Base(DeclarativeBase):
    pass


class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(256), nullable=False)

    # Один ко многим
    books: Mapped[list["Book"]] = relationship("Book", back_populates="author")

    def __repr__(self):
        return f"Author(id={self.id}, name={self.name})"


class Book(Base):
    __tablename__ = "books"

    id: Mapped[id] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(256), nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=True)

    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    author: Mapped["Author"] = relationship("Author", back_populates="books")

    def __repr__(self):
        return f"Book(id={self.id}, title={self.title}, year={self.year})"
