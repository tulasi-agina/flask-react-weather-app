# app.py - Flask backend to fetch current temperature for a given city

from flask import Flask, request, jsonify  # Import Flask core, request handler, and JSON response
from flask_cors import CORS                # Import CORS to allow communication with frontend
import requests
import os
from dotenv import load_dotenv  # Load environment variables from .env

# Load environment variables from .env file
load_dotenv()

# Create a new Flask application instance
app = Flask(__name__)

# Enable CORS (Cross-Origin Resource Sharing) so React (on a different port) can talk to this API
CORS(app)

# Get the API key from environment
# official API endpoint for OpenWeatherMap's Current Weather Data API
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"

# Define a route that accepts POST requests at /api/message
@app.route('/api/message', methods=['POST'])
def get_weather():
    # Get JSON from request body
    data = request.get_json()
    city = data.get('text', '')  # Expecting { "text": "city name" }

    if not city:
        return jsonify({"response": "Please provide a city name."}), 400

    try:
        # Build request to OpenWeatherMap
        params = {
            'q': city,
            'appid': WEATHER_API_KEY,
            'units': 'imperial'  # Fahrenheit
        }
        res = requests.get(WEATHER_API_URL, params=params)
        res.raise_for_status()
        weather_data = res.json()

        # Extract and format temperature
        temp_f = weather_data['main']['temp']
        return jsonify({"response": f"The temperature in {city} is {temp_f}°F"})

    except Exception as e:
        return jsonify({"response": f"Could not get weather for '{city}'. Error: {str(e)}"}), 500

# Run the app only if this script is executed directly (not imported as a module)
if __name__ == '__main__':
    # Start the development server with debug mode on
    app.run(debug=True, port=5001)