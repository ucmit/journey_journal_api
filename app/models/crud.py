from typing import List, Union
from app.database import Base
from app.schemas import user, journal
from app.models import models
from sqlalchemy.orm import Session

class CRUD():
    _model: Base
    _schema: object
    _schema_create: object

    def _create(self, db: Session, schema_create: '_schema_create')->'_schema':
        db_model = self._model(**schema_create.dict())
        db.add(db_model)
        db.commit()
        db.refresh(db_model)
        return db_model

    def _get_all(self, db: Session, offset: int = 0, limit: int = 50)->Union[None, List['_schema']]:
        return db.query(self._model).offset(offset).limit(limit).all()

class UserCRUD(CRUD):
    _model: models.UserDB = models.UserDB
    _schema: user.User = user.User
    _schema_create: user.UserCreate = user.UserCreate
    
    def _get_by_email(self, db: Session, email: str)->Union[None, '_schema']:
        return db.query(self._model).filter(self._model.email == email).first()

    def _get_by_id(self, db: Session, user_id: int)->Union[None, '_schema']:
        return db.query(self._model).filter(self._model.id == user_id).first()


class JournalCRUD(CRUD):
    _model: models.JournalDB = models.JournalDB
    _schema: journal.Journal = journal.Journal
    _schema_create: journal.JournalCreate = journal.JournalCreate
    

user_crud = UserCRUD()
journal_crud = JournalCRUD()

