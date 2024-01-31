from pydantic import BaseModel
from pydantic import PastDate


class Publish(BaseModel):
    text: str
    date: PastDate
    author: str
    count_votes: str
    rating: str
