import os
from fastapi.routing import APIRouter
from fastapi import Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.database import get_db
from app.conf import MapApi, WeatherApi
from app.schemas import user, journal
from app.models.crud import user_crud, journal_crud

router = APIRouter(prefix="/journal", tags=["Journal"])

@router.post('/', response_model=journal.Journal)
def create_journal(journal: journal.JournalCreate, db = Depends(get_db)):
    return journal_crud._create(db, journal)

