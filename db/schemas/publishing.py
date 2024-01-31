from pydantic import BaseModel
from datetime import datetime


class PublishingView(BaseModel):
    text: str

    plus_vote: str | None
    minus_vote: str | None

    post_data: datetime
