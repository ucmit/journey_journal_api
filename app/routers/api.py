from fastapi.routing import APIRouter
from fastapi import HTTPException
from app.conf import MapApi, WeatherApi
from app.schemas import api

router = APIRouter(prefix="/api", tags=["API"])


"""
[GET]/place
QUERY_PARAM
priority=> placename:str
lat:float
lon:float
"""
@router.get("/place", response_model=api.Place)
async def place_get_by_placename(placename:str = None, lat:float = None, lon:float = None):
    if placename:
        return MapApi._get_place_by_name(placename)
    elif lat and lon:
        return MapApi._get_place_by_lat_lon(lon, lat)
    
    raise HTTPException(status_code=400, detail='Неправильный запрос')

"""
[GET]/weather
QUERY_PARAMS
priority=> placename:str
lat:float
lon:float
"""
@router.get('/weather', response_model=api.PlaceWeather)
async def weather_get_by_lat_lon(placename:str = None, lat:float = None, lon:float = None):
    if placename:
        place = MapApi._get_place_by_name(placename)
        lat, lon = place.lat, place.lon
        return WeatherApi._get_weather_by_lat_lon(lon, lat)
    elif lat and lon:
        return WeatherApi._get_weather_by_lat_lon(lon, lat)
    
    raise HTTPException(status_code=400, detail='Неправильный запрос')

