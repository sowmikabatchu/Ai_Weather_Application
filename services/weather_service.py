from requests import RequestException, Session, get
from requests.exceptions import ProxyError

from config.settings import Config, get_env_value
from models.weather_model import WeatherData


class WeatherServiceError(Exception):
    """A user-safe message for weather API failures."""


def _request_weather(params: dict[str, str]):
    """Use the environment proxy when available, with a direct retry for a failed proxy."""
    try:
        return get(Config.WEATHER_API_URL, params=params, timeout=10)
    except ProxyError:
        with Session() as session:
            session.trust_env = False
            return session.get(Config.WEATHER_API_URL, params=params, timeout=10)


def get_current_weather(city: str) -> WeatherData:
    api_key = get_env_value("OPENWEATHER_API_KEY")
    if not api_key:
        raise WeatherServiceError("OPENWEATHER_API_KEY is missing. Add it to your .env file.")

    try:
        response = _request_weather({"q": city, "appid": api_key, "units": "metric"})
    except RequestException as error:
        raise WeatherServiceError("The weather service could not be reached. Try again shortly.") from error

    if response.status_code == 404:
        raise WeatherServiceError("City not found. Check the spelling and try again.")
    if response.status_code in {401, 403}:
        raise WeatherServiceError("The OpenWeather API key was rejected. Check your .env file.")
    if not response.ok:
        raise WeatherServiceError("The weather service returned an unexpected error. Try again shortly.")

    try:
        return WeatherData.from_api_response(response.json())
    except (KeyError, IndexError, TypeError, ValueError) as error:
        raise WeatherServiceError("Weather data arrived in an unexpected format. Try again shortly.") from error
