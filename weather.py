import requests

def get_weather():
    url = "https://api.openweathermap.org/data/2.5/weather?q=Stockholm,SE&units=metric&appid=YOUR_API_KEY"
    response = requests.get(url)
    data = response.json()
    weather_data = {
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description']
    }
    return weather_data
