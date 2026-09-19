from flask import Flask, render_template, request

from config.settings import Config, get_env_value
from services.groq_service import get_weather_insight
from services.weather_service import WeatherServiceError, get_current_weather
from utils.validators import validate_activity, validate_city


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.route("/", methods=["GET", "POST"])
    def index():
        weather = None
        insight = None
        error = None
        city = ""
        activity = ""

        if request.method == "POST":
            is_valid, city_or_error = validate_city(request.form.get("city"))
            city = (request.form.get("city") or "").strip()
            activity = validate_activity(request.form.get("activity"))

            if not is_valid:
                error = city_or_error
            else:
                try:
                    weather = get_current_weather(city_or_error)
                    insight = get_weather_insight(weather, activity)
                except WeatherServiceError as service_error:
                    error = str(service_error)

        return render_template(
            "index.html", weather=weather, insight=insight, error=error,
            city=city, activity=activity, ai_available=bool(get_env_value("GROQ_API_KEY")),
        )

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"], port=app.config["PORT"])
