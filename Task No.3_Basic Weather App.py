import requests

api_key = '30d4741c779ba94c470ca1f63045390a'

print("Oasis Infobyte Basic Weather App\n")
user_input = input("City: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    humidity = weather_data.json()['main']['humidity']
    weather_description = weather_data.json()['weather'][0]['description']

    print(f"Temperature: {temp}ºF")
    print(f"Humidity: {humidity}%")
    print(f"Weather Conditions: {weather}")
