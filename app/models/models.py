from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class UserDB(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    place = Column(String) # List[float,float] разделитель ','
    place_name = Column(String)

    journal = relationship('JournalDB', back_populates='user')

class JournalDB(Base):
    __tablename__ = 'journal'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    place = Column(String) # List[float,float] разделитель ','
    place_name = Column(String)

    user = relationship('UserDB', back_populates='journal')