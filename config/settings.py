import os
from pathlib import Path

from dotenv import dotenv_values, load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")


def get_env_value(name: str, default: str = "") -> str:
    """Return an environment value, rereading .env for changes made while Flask runs."""
    value = os.getenv(name, "").strip()
    if value:
        return value

    file_value = dotenv_values(BASE_DIR / ".env").get(name, default)
    return str(file_value or default).strip()


class Config:
    """Configuration loaded from environment variables."""

    SECRET_KEY = os.getenv("SECRET_KEY", "change-this-for-production")
    OPENWEATHER_API_KEY = get_env_value("OPENWEATHER_API_KEY")
    GROQ_API_KEY = get_env_value("GROQ_API_KEY")
    GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
    DEBUG = os.getenv("FLASK_DEBUG", "false").lower() in {"1", "true", "yes"}
    PORT = int(os.getenv("PORT", "5000"))
    WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"
