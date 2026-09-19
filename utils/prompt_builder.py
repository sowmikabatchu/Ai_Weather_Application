from models.weather_model import WeatherData


def build_weather_prompt(weather: WeatherData, activity: str = "") -> str:
    """Create a bounded, weather-only prompt for the Groq model."""
    activity_note = f" The user plans to: {activity}." if activity else ""
    return (
        "You are a practical weather assistant. Give a friendly briefing in 3 short "
        "bullet points. Include clothing or umbrella advice and flag any meaningful "
        "comfort or safety consideration. Do not invent forecasts or facts beyond the data.\n\n"
        f"Location: {weather.city}, {weather.country}\n"
        f"Conditions: {weather.description}\n"
        f"Temperature: {weather.temperature} C (feels like {weather.feels_like} C)\n"
        f"Humidity: {weather.humidity}%\n"
        f"Wind: {weather.wind_speed} km/h\n"
        f"Visibility: {weather.visibility_km if weather.visibility_km is not None else 'unknown'} km."
        f"{activity_note}"
    )
