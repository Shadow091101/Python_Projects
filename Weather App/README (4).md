
# 🌤️ Weather Forecast CLI App

This is a simple and interactive command-line Python application that allows users to fetch real-time weather and air quality information for any city using the **WeatherAPI**.

## 🔧 Features

### 🌍 Global Weather Lookup
- Enter the name of any city worldwide to get the latest weather information.

### 🕒 Time & Location Info
- Displays the **local time** of the city searched.
- Provides the **last updated time** of the weather data.
- Shows detailed location including **city**, **region**, and **country**.

### 🌤️ Current Weather Conditions
- Weather condition description (e.g., Clear, Cloudy, Rain).
- **Temperature** in Celsius and "feels like" temperature.
- **Humidity**, **wind speed & direction**, **pressure**, **cloud cover**, **visibility**, and **UV index**.

### 🌫️ Air Quality Index (AQI)
- Includes US EPA Air Quality Index with a **category label**:
  - Good
  - Moderate
  - Unhealthy for Sensitive Groups
  - Unhealthy
  - Very Unhealthy
  - Hazardous
- Displays concentrations of common pollutants:
  - **PM2.5**
  - **PM10**
  - **CO (Carbon Monoxide)**
  - **NO₂ (Nitrogen Dioxide)**
  - **SO₂ (Sulfur Dioxide)**
  - **O₃ (Ozone)**

### 🔁 Continuous Search Options
- Search for multiple cities in a single session.
- Return to the main menu or exit the application anytime.

## 🚀 Getting Started

To run this application:

1. Make sure you have Python installed.
2. Install the `requests` library if it's not already available:
   ```
   pip install requests
   ```
3. Replace `your_api_key` in the script with your actual API key from [WeatherAPI](https://www.weatherapi.com/).
4. Run the script in a terminal:
   ```
   python weather_forecast.py
   ```

## 🧪 Dependencies
- Python 3.x
- `requests` library for HTTP requests
- WeatherAPI (for accessing weather and AQI data)

## 📦 API Provider
- [WeatherAPI.com](https://www.weatherapi.com/) — Reliable source for current weather, air quality, and alerts.

## 📄 License
This project is for educational and personal use only. Attribution to [WeatherAPI](https://www.weatherapi.com/) is required when using their data.
