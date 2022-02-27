from pydantic import BaseModel

class JournalBase(BaseModel):
    user_id: int
    place: str
    place_name: str
    
class JournalCreate(JournalBase):
    def __init__(self, **data:dict) -> None:
        data['place'] = ",".join(map(str, data['place']))
        super().__init__(**data)

class Journal(JournalBase):
    id:int

    class Config:
        orm_mode = True