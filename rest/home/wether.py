import requests
from datetime import datetime, timedelta


def get_weather_forecast(latitude, longitude):
    # Dates for the past week
    today = datetime.now()
    week_dates = [(today - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(7)]
    week_dates.reverse()  # To get the dates from Saturday to Friday

    # Dictionary to store weather data
    weather_data = {}

    # Names of the days of the week in English
    days_of_week = [
        "Saturday",
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
    ]

    # Fetch weather data from the API
    response = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min,weathercode&timezone=Asia/Tehran"
    )
    data = response.json()

    # Map weather codes to weather conditions
    weather_code_mapping = {
        0: "Clear",
        1: "Clear",
        2: "Clear",
        3: "Clear",
        45: "Foggy",
        48: "Foggy",
        51: "Rainy",
        53: "Rainy",
        55: "Rainy",
        56: "Rainy",
        57: "Rainy",
        61: "Rainy",
        63: "Rainy",
        65: "Rainy",
        66: "Rainy",
        67: "Rainy",
        71: "Rainy",
        73: "Rainy",
        75: "Rainy",
        77: "Rainy",
        80: "Rainy",
        81: "Rainy",
        82: "Rainy",
        85: "Rainy",
        86: "Rainy",
        95: "Rainy",
        96: "Rainy",
        99: "Rainy",
    }

    # Populate the dictionary with the received data
    for i in range(7):
        date = week_dates[i]
        day_of_week = days_of_week[i]  # Use the correct day of the week
        max_temp = data["daily"]["temperature_2m_max"][i]
        min_temp = data["daily"]["temperature_2m_min"][i]
        weather_code = data["daily"]["weathercode"][i]
        weather_status = weather_code_mapping.get(weather_code, "Unknown")
        weather_data[day_of_week] = [weather_status, max_temp, min_temp]

    return weather_data
