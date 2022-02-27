from pydantic import BaseModel
from typing import Optional, List

from app.schemas.journal import Journal


class UserBase(BaseModel):
    name:Optional[str]
    email:str
    place: Optional[str] = ''
    place_name: Optional[str] = ''

class UserCreate(UserBase):
    password:str

    def __init__(self, **data:dict) -> None:
        if data.get('place', None):
            data['place'] = ",".join(map(str, data['place']))
        super().__init__(**data)

class User(UserBase):
    id:int
    journal: List[Journal]

    class Config:
        orm_mode = True