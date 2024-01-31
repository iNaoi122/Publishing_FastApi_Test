from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship, Mapped

from db.models.base import Base


class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = Column(Integer, primary_key=True, unique=True)
    username: Mapped[str] = Column(String(128))

    hashed_password: Mapped[str] = Column(String(256))

    publish = relationship("Publish", backref="author")
