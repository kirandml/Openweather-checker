import requests

# Function to get weather data
def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # This will give the temperature in Celsius
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        temperature = main['temp']
        description = weather['description']
        print(f"The temperature in {city} is {temperature}°C with {description}.")
    else:
        print(f"City {city} not found or an error occurred.")

# Main script
if __name__ == "__main__":
    api_key = "84535988c5ed8028f572355c5e2cfaa9"
    city = input("Enter the city name: ")
    get_weather(city, api_key)
