from pydantic import BaseModel


class UserReg(BaseModel):
    name: str
    password: str


class User(BaseModel):
    username: str
