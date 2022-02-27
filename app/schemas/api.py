from pydantic import BaseModel
from typing import List, Optional

class Place(BaseModel):
    id: str
    place_type: List[str]
    place_name: str
    lat: float
    lon: float

    def __init__(self, **data: dict) -> None:
        if data.get('center', None):
            # Разбираем 'center' на lon, lat
            data['lon'], data['lat']= data['center'][0], data['center'][1]

        super().__init__(**data)


class WeatherAlerts(BaseModel):
    sender_name: str
    event: str
    start: int
    end: int
    description: str
    tags: List[str]

class WeatherMain(BaseModel):
    main: str
    description: str

class WeatherDailyTemp(BaseModel):
    morn: float
    day: float
    eve: float

    night: Optional[float]
    min: Optional[float]
    max: Optional[float]

class WeatherDailyFeelsLike(BaseModel):
    morn: float 
    day: float
    eve: float

    night: float

class PlaceWeatherCurrent(BaseModel):
    dt: int
    
    sunrise: int
    sunset: int

    moonrise: Optional[int]
    moonset: Optional[int]
    moon_phase: Optional[float]

    temp: float
    feels_like: float

    pressure: int
    humidity: int
    clouds: int
    visibility: int

    wind_speed: float
    wind_gust: Optional[float]
    wind_deg: int
    uvi: float

    rain: Optional[dict]
    snow: Optional[dict]

    weather: List[WeatherMain]

class PlaceWeatherDaily(BaseModel):
    dt: int
    wind_speed: float
    uvi: float
    pop: float

    temp: WeatherDailyTemp

    feels_like: Optional[WeatherDailyFeelsLike]

    weather: List[WeatherMain]

class PlaceWeather(BaseModel):
    lat: float
    lon: float
    timezone: str
    timezone_offset: float
    current: PlaceWeatherCurrent
    daily: List[PlaceWeatherDaily]
    alerts: Optional[WeatherAlerts]
