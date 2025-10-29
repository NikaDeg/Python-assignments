import requests
city = input("Enter municipality name:")
appcode = "fa30f5dc37496940f69479b66f47783e"
request = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={appcode}'
lat = ''
lon = ''
try:
    response = requests.get(request)
    if response.status_code == 200:
        lat = f"{response.json()[0]['lat']:.2f}"
        lon = f"{response.json()[0]['lon']:.2f}"
except Exception as e:
    print(e)

request2 = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={appcode}&units=metric'
try:
    response2 = requests.get(request2)

    if response2.status_code == 200:
        print(f"Weather: {response2.json()['weather'][0]['main']}")
        print(f"Temperature: {response2.json()['main']['temp']} Celsius")
except Exception as e:
    print(e)




