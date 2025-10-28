import requests

name = input("Enter your name: ")

request = f"https://api.agify.io?name={name}"
try:
    response = requests.get(request)
    if response.status_code == 200:
        print(f"Your age is {response.json()["age"]}")

except Exception as e:
    print(e)