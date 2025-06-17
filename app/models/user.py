from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel, table=True):
    username: str = Field(primary_key=True)
    name: str = Field()
    email: str = Field()