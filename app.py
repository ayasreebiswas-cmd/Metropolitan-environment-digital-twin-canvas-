import os
import json
import requests
from datetime import datetime
from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

app = Flask(__name__)

# Get API keys from .env
MAP_API_KEY = os.getenv("MAP_API_KEY")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

DATA_FILE = "telemetry_data.json"


def save_data_to_file(data):
    """Step 3: Saves collected telemetry data to a local JSON file."""
    existing_data = []

    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                existing_data = json.load(f)
        except json.JSONDecodeError:
            existing_data = []

    existing_data.append(data)

    with open(DATA_FILE, "w") as f:
        json.dump(existing_data, f, indent=4)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/config')
def get_config():
    return jsonify({
        "mapApiKey": MAP_API_KEY
    })


@app.route('/api/fetch-live-data', methods=['GET'])
def fetch_live_data():
    """Steps 1 & 2: Fetches live air pollution and weather data from OpenWeatherMap API."""

    lat = request.args.get('lat')
    lon = request.args.get('lon')

    if not lat or not lon:
        return jsonify({
            "error": "Latitude and Longitude are required"
        }), 400

    try:

        # OpenWeatherMap Air Pollution API
        pollution_url = (
            f"http://api.openweathermap.org/data/2.5/air_pollution"
            f"?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}"
        )

        pollution_res = requests.get(pollution_url).json()

        # OpenWeatherMap Weather API
        weather_url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}&units=metric"
        )

        weather_res = requests.get(weather_url).json()

        components = pollution_res['list'][0]['components']
        weather_main = weather_res['main']

        payload = {
            "timestamp": datetime.now().isoformat(),

            "coordinates": {
                "lat": float(lat),
                "lon": float(lon)
            },

            "weather": {
                "temp": weather_main['temp'],
                "humidity": weather_main['humidity'],
                "pressure": weather_main['pressure'],
                "wind_speed": weather_res['wind']['speed'],
                "condition": weather_res['weather'][0]['main']
            },

            "pollutants": {
                "pm2_5": components.get('pm2_5'),
                "pm10": components.get('pm10'),
                "no2": components.get('no2'),
                "nh3": components.get('nh3'),
                "so2": components.get('so2'),
                "co": components.get('co'),
                "o3": components.get('o3')
            },

            "aqi": pollution_res['list'][0]['main']['aqi']
        }

        save_data_to_file(payload)

        return jsonify(payload)

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000
    )
