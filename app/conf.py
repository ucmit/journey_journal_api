import os
import requests

from app.schemas.api import PlaceWeather, Place


class API:
    def __init__(self, api_url:str, api_token:str):
        self._api_url = api_url
        self._api_token = api_token

    def _request(self, method:str, **data):
        pass

class MapBox(API):
    _geocoding_url: str = "geocoding/v5"
    _image_url: str = "/v4/"

    def _get_place_by_name(self, placename: str)->Place:
        """
        https://docs.mapbox.com/api/search/geocoding/#forward-geocoding
        Получение информации о месте используя поиск по имени
        """
        url = f"{self._api_url}/{self._geocoding_url}/mapbox.places/{placename}.json?access_token={self._api_token}"
        res = requests.get(url)

        return Place(**res.json()['features'][0])
    
    def _get_place_by_lat_lon(self, lon:float, lat:float)->Place:
        """
        https://docs.mapbox.com/api/search/geocoding/#reverse-geocoding
        Получение информации о месте используя поиск долготе и широте
        """
        url = f"{self._api_url}/{self._geocoding_url}/mapbox.places/{lon},{lat}.json?access_token={self._api_token}"
        res = requests.get(url)

        return Place(**res.json()['features'][0])

class OpenWeather(API):
    _one_call = "/data/2.5/onecall"

    def _get_weather_by_lat_lon(self, lat:float, lon:float)->PlaceWeather:
        url = self._api_url + self._one_call + '?'
        url += f'appid={self._api_token}&'
        url += f'lat={lat}&'
        url += f'lon={lon}&'
        url += f'exclude=minutely,hourly&'
        url += f'units=metric&'
        url += f'lang=en&' # ru - Русский, en - English, de - Deutsch

        res = requests.post(url)

        return PlaceWeather(**res.json())

MapApi = MapBox(
    os.getenv("MAP_API_URL"),
    os.getenv("MAP_API_TOKEN")
)

WeatherApi = OpenWeather(
    os.getenv("WEATHER_API_URL"),
    os.getenv("WEATHER_API_KEY")
)


