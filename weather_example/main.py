import requests


def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city}"

    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main_data = data["main"]
        # Convert from Kelvin to Celsius
        temperature = main_data["temp"] - 273.15
        pressure = main_data["pressure"]
        humidity = main_data["humidity"]

        weather_data = data["weather"]
        weather_description = weather_data[0]["description"]

        print(f"Temperature: {temperature}°C")
        print(f"Weather Description: {weather_description}")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
    else:
        print("City not found.")


if __name__ == "__main__":
    city = "London"  # replace with your desired city name
    # replace with your API key obtained from OpenWeatherMap
    api_key = 'your_api_key'
    get_weather(city, api_key)
