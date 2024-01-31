from pydantic import BaseModel


class UserReg(BaseModel):
    name: str
