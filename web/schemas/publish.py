from pydantic import BaseModel
from datetime import datetime


class Publish(BaseModel):
    text: str
    date: datetime
    author: str
    count_votes: int
    rating: int
