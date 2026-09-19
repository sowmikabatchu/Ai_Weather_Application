import re


def validate_city(city: str | None) -> tuple[bool, str]:
    """Validate a city name before it is sent to the weather provider."""
    value = (city or "").strip()
    if not value:
        return False, "Enter a city name to check its weather."
    if len(value) > 100:
        return False, "City names must be 100 characters or fewer."
    if not re.fullmatch(r"[A-Za-zÀ-ÿ .,'-]+", value):
        return False, "Use letters, spaces, apostrophes, commas, or hyphens in the city name."
    return True, value


def validate_activity(activity: str | None) -> str:
    """Keep optional user context concise for the AI prompt."""
    return (activity or "").strip()[:120]
