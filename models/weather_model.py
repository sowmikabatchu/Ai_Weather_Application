from dataclasses import dataclass
from typing import Any


@dataclass
class WeatherData:
    city: str
    country: str
    temperature: float
    feels_like: float
    description: str
    humidity: int
    wind_speed: float
    icon: str
    pressure: int
    visibility_km: float | None = None

    @classmethod
    def from_api_response(cls, payload: dict[str, Any]) -> "WeatherData":
        weather = payload["weather"][0]
        main = payload["main"]
        visibility = payload.get("visibility")
        return cls(
            city=payload["name"],
            country=payload["sys"]["country"],
            temperature=round(main["temp"]),
            feels_like=round(main["feels_like"]),
            description=weather["description"].capitalize(),
            humidity=main["humidity"],
            wind_speed=round(payload["wind"]["speed"] * 3.6, 1),
            icon=weather["icon"],
            pressure=main["pressure"],
            visibility_km=round(visibility / 1000, 1) if visibility is not None else None,
        )
