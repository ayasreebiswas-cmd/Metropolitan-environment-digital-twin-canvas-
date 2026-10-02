# Metropolitan Environment Digital Twin

A Flask-based web application for monitoring **urban environmental conditions** using live weather and air-pollution data. The application retrieves data from the OpenWeatherMap API based on a selected latitude and longitude, processes the information, and displays it through a web interface.

## Features

* 🌍 Location-based environmental monitoring
* 🌤️ Live weather information
* 🌫️ Live air-pollution information
* 📊 Air Quality Index (AQI) data
* 📍 Latitude and longitude-based data retrieval
* 💾 Stores collected telemetry data in a local JSON file
* 🗺️ Map API integration
* 🌐 Flask-based web application
* 🔐 API keys stored securely using environment variables

## Technologies Used

* **Python**
* **Flask**
* **HTML**
* **CSS**
* **JavaScript**
* **OpenWeatherMap API**
* **Map API**
* **JSON**
* **python-dotenv**
* **Git & GitHub**

## Project Structure

```text
Metropolitan_environment/
│
├── app.py
├── README.md
├── .env
├── .gitignore
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── telemetry_data.json
│
└── venv/
```

> **Note:** `.env` and `venv/` should not be uploaded to GitHub.

## How It Works

The application follows these basic steps:

1. The user opens the web application.
2. A latitude and longitude are provided.
3. Flask receives the location information.
4. The application requests weather information from OpenWeatherMap.
5. The application requests air-pollution information from OpenWeatherMap.
6. Weather and pollution information is processed.
7. The collected information is returned to the frontend as JSON.
8. The telemetry data is stored locally in `telemetry_data.json`.
9. The frontend can use the returned information to display environmental conditions.

## Environmental Data

The application collects weather information such as:

* Temperature
* Humidity
* Atmospheric pressure
* Wind speed
* Weather condition

It also collects air-pollution information such as:

* PM2.5
* PM10
* NO₂
* NH₃
* SO₂
* CO
* O₃
* AQI

## API Configuration

API keys are stored in a `.env` file instead of directly inside `app.py`.

Create a `.env` file in the project root:

```text
MAP_API_KEY=YOUR_MAP_API_KEY
OPENWEATHER_API_KEY=YOUR_OPENWEATHER_API_KEY
```

The application loads these values using `python-dotenv`.

### Security

Never upload `.env` to GitHub.

The `.gitignore` file should contain:

```text
.env
venv/
__pycache__/
*.pyc
```

If an API key has previously been exposed, revoke or rotate that key and replace it with a new one.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ayasreebiswas-cmd/Metropolitan-environment-digital-twin-canvas-.git
```

### 2. Open the Project

```bash
cd Metropolitan-environment-digital-twin-canvas-
```

### 3. Create a Virtual Environment

On Windows:

```cmd
python -m venv venv
```

### 4. Activate the Virtual Environment

```cmd
venv\Scripts\activate
```

### 5. Install Dependencies

```cmd
pip install -r requirements.txt
```

If `requirements.txt` has not been created yet, install the required packages:

```cmd
pip install flask requests python-dotenv
```

Then create the requirements file:

```cmd
pip freeze > requirements.txt
```

## Running the Application

Activate the virtual environment:

```cmd
venv\Scripts\activate
```

Then run:

```cmd
python app.py
```

The Flask application runs on:

```text
http://127.0.0.1:5000
```

Open the URL in your web browser.

## API Endpoints

### Home Page

```text
GET /
```

Displays the main web interface.

### Map Configuration

```text
GET /api/config
```

Returns the configured map API key for frontend map integration.

### Live Environmental Data

```text
GET /api/fetch-live-data
```

Latitude and longitude are required.

Example:

```text
/api/fetch-live-data?lat=22.5726&lon=88.3639
```

The endpoint returns weather, pollution, coordinates, timestamp, and AQI information.

## Example Response

```json
{
    "timestamp": "2026-08-18T08:30:00",
    "coordinates": {
        "lat": 22.5726,
        "lon": 88.3639
    },
    "weather": {
        "temp": 30,
        "humidity": 70,
        "pressure": 1005,
        "wind_speed": 3.5,
        "condition": "Clouds"
    },
    "pollutants": {
        "pm2_5": 25,
        "pm10": 40,
        "no2": 12,
        "nh3": 4,
        "so2": 3,
        "co": 300,
        "o3": 50
    },
    "aqi": 2
}
```

> The values above are only an example. Actual values are retrieved from the API.

## Data Storage

The application stores collected telemetry information in:

```text
telemetry_data.json
```

The stored information includes:

* Timestamp
* Coordinates
* Weather information
* Pollutant measurements
* AQI

## GitHub Workflow

After making changes to the project:

```cmd
git status
git add .
git commit -m "Update project"
git push
```

Before pushing, make sure that sensitive files such as `.env` are ignored.

## Future Improvements

Possible future improvements include:

* Real-time environmental dashboards
* Historical environmental data visualization
* Interactive pollution maps
* Data analytics and reporting
* Database integration
* User authentication
* Environmental alerts and notifications
* Predictive environmental analysis
* Deployment to a cloud platform

## Author - Ayasree biswas
## Live link -  https://metropolitan-environment-digital-twin.onrender.com

**Ayasree Biswas**

## License

This project is intended for educational and project-development purposes.

