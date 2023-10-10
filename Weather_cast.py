#!/usr/bin/python3
import json
import subprocess

# Chechk if we have requests module.if have not download
try:
    import requests
except ImportError:
    print("Requests library not found. Installing...")
    subprocess.check_call(["pip", "install", "requests"])
    import requests

# Enter the city name for which you want the weather forecast
city = input("Input which city weather forecast you want to know.")


# Create the url
url = f'https://goweather.herokuapp.com/weather/{city}'

# Send the request
response = requests.get(url)
print(response.json)
# Check response and print whether
if response.status_code == 200 and response.json()["temperature"]:
    data=response.json() 
    # Detailed Wheather 
    temperature=data["temperature"]
    wind_speed=data["wind"]
    description=data["description"]

    print(f"The wheather in {city.title()} {temperature} the wind speed is {wind_speed}: {description}")
    # Wheather
    while True: 
        wheather=input("Do you want to receive defined information?(temperature,description,wind) or No. ")
        if wheather.lower()=="no":
            break
        print(f"The {wheather.title()} is {data[wheather.lower()]}")

   
else:
    print("Error with response! Try again")