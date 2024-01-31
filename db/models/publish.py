import datetime

from sqlalchemy import Integer, Column, Text, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.types import Date

from db.models.base import Base


class Publish(Base):
    __tablename__ = "publishing"

    id: Mapped[int] = Column(Integer, primary_key=True, unique=True)
    text: Mapped[str] = Column(Text)

    plus_vote: Mapped[int] = Column(Integer)
    minus_vote: Mapped[int] = Column(Integer)

    post_data: Mapped[str] = Column(Date, default=datetime.date.today())

    author_id = Column(Integer, ForeignKey("authors.id"))
