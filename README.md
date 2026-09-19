# AI Weather Application

A Flask web app that shows live weather from OpenWeather and creates personalized, practical weather advice with Groq.

## Setup

1. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Install packages:

   ```powershell
   pip install -r requirements.txt
   ```

3. Open `.env` and add an OpenWeather API key:

   ```env
   OPENWEATHER_API_KEY=your_openweather_key
   ```

   Add `GROQ_API_KEY=your_groq_key` as well to enable the AI weather note. The rest of the application works without Groq.

4. Run the app:

   ```powershell
   python app.py
   ```

5. Visit `http://127.0.0.1:5000` in your browser. Set `PORT` in `.env` if port 5000 is already in use.

## Environment variables

| Name | Required | Purpose |
| --- | --- | --- |
| `OPENWEATHER_API_KEY` | Yes | Current weather data from OpenWeather |
| `GROQ_API_KEY` | No | Personalized AI weather advice |
| `GROQ_MODEL` | No | Groq model, defaults to `llama-3.3-70b-versatile` |
| `FLASK_DEBUG` | No | Enables debug mode when `true` |
| `PORT` | No | Local server port, defaults to `5000` |

## Project structure

`app.py` owns HTTP routes. `services/` handles the external APIs, `models/` holds the weather data object, and `utils/` handles input validation and AI prompt construction.
