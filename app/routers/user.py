import os
from typing import List
from fastapi import Depends, HTTPException, Request
from fastapi.routing import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.database import get_db
from app.schemas import user, api
from app.models.crud import user_crud
from app.conf import MapApi, WeatherApi

router = APIRouter(prefix="/user", tags=["User"])
templates = Jinja2Templates(directory=os.getenv('TEMPLATES_PATH'))

"""
[GET]/
Рендер HTML со списком всех пользователей
"""
@router.get('/', response_class=HTMLResponse)
async def user_main_page(request: Request, db = Depends(get_db)):
    users: List[user.User] = user_crud._get_all(db)
    
    return templates.TemplateResponse(
        'user/all.html',
        {"request": request, "users": users}
    )

@router.get('/{user_id}',  response_class=HTMLResponse)
async def user_detail_page(user_id:int, request: Request, db = Depends(get_db)):
    user_detail: user.User = user_crud._get_by_id(db, user_id)

    weather = {}
    for j in user_detail.journal:
        lat, lon = j.place.split(',')

        weather[str(j.id)] = WeatherApi._get_weather_by_lat_lon(float(lat), float(lon))

    return templates.TemplateResponse(
        'user/detail.html',
        {"request": request, "user": user_detail, "weather": weather}
    )



"""
[POST]/create
REQUEST_BODY
User
"""
@router.post('/create', response_model=user.User, status_code=201)
def create_user(user: user.UserCreate, db = Depends(get_db)):
    if user_crud._get_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Пользователь с таким email уже существует")
    
    return user_crud._create(db, user)

"""
[GET]/weather
"""
@router.get('/all', response_model=List[user.User])
def get_users(db = Depends(get_db)):
    return user_crud._get_all(db)



