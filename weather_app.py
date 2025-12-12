#Weather APP
import requests

def get_weather(city):
    api_key = "2be80c746745449dfe077378087ebe3b"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    params = {
        'q': city,
        'appid': api_key,  
        'units': 'metric'
    }   
    response = requests.get(base_url, params=params)
    
  
    if response.status_code == 200:
        data = response.json()
        print(f"\nWeather in {city.title()}:")
        print(f"🌡️ Temperature: {data['main']['temp']}°C")
        print(f"💧 Humidity: {data['main']['humidity']}%")
        print(f"🌤️ Condition: {data['weather'][0]['description'].title()}")
    else:
        print("❌ City not found or API error.")

city_name = input("Enter city name: ")
get_weather(city_name)

print("\nThank you for using the Weather App! ☀️🌧️❄️")