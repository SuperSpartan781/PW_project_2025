from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field()
    description: str = Field()
    date: datetime = Field()
    location: str = Field()