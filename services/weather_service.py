# services/weather_service.py

from datetime import datetime


class WeatherService:
    """
    Smart Stadium Weather Service
    """

    def __init__(self):

        self.weather = {
            "condition": "Sunny",
            "temperature": 30,
            "humidity": 55,
            "wind_speed": 12,
            "rain_probability": 10
        }

    # ---------------------------------
    # Current Weather
    # ---------------------------------

    def current_weather(self):

        return {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "condition": self.weather["condition"],
            "temperature": self.weather["temperature"],
            "humidity": self.weather["humidity"],
            "wind_speed": self.weather["wind_speed"]
        }

    # ---------------------------------
    # Match Weather
    # ---------------------------------

    def match_weather(self):

        return {
            "condition": self.weather["condition"],
            "temperature": self.weather["temperature"],
            "status": "Good for Match"
        }

    # ---------------------------------
    # Weather Forecast
    # ---------------------------------

    def forecast(self):

        return [
            {
                "day": "Today",
                "condition": "Sunny",
                "temperature": 30
            },
            {
                "day": "Tomorrow",
                "condition": "Cloudy",
                "temperature": 28
            },
            {
                "day": "Day 3",
                "condition": "Rainy",
                "temperature": 26
            }
        ]

    # ---------------------------------
    # Rain Alert
    # ---------------------------------

    def rain_alert(self):

        if self.weather["rain_probability"] >= 50:
            return "Rain Expected"

        return "No Rain Expected"

    # ---------------------------------
    # Update Weather
    # ---------------------------------

    def update_weather(
        self,
        condition,
        temperature,
        humidity,
        wind_speed,
        rain_probability
    ):

        self.weather["condition"] = condition
        self.weather["temperature"] = temperature
        self.weather["humidity"] = humidity
        self.weather["wind_speed"] = wind_speed
        self.weather["rain_probability"] = rain_probability

        return {
            "message": "Weather Updated Successfully"
        }

    # ---------------------------------
    # Health Check
    # ---------------------------------

    def health(self):

        return {
            "service": "Weather Service",
            "status": "Running"
        }


# Singleton Object

weather_service = WeatherService()