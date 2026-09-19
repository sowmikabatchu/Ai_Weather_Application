from groq import Groq

from config.settings import Config, get_env_value
from models.weather_model import WeatherData
from utils.prompt_builder import build_weather_prompt


def get_weather_insight(weather: WeatherData, activity: str = "") -> str | None:
    """Return an AI briefing, or None so the core weather experience keeps working."""
    api_key = get_env_value("GROQ_API_KEY")
    if not api_key:
        return None

    try:
        client = Groq(api_key=api_key)
        completion = client.chat.completions.create(
            model=Config.GROQ_MODEL,
            messages=[{"role": "user", "content": build_weather_prompt(weather, activity)}],
            temperature=0.4,
            max_tokens=220,
        )
        return completion.choices[0].message.content.strip()
    except Exception:
        return None
