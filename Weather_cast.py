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
city = 'armenia'

# Create the url
url = f'https://goweather.herokuapp.com/weather/{city}'

# Send the request
response = requests.get(url)
# Check response and print whether
if response.status_code == 200:
    data=response.json() 
    # 
    temperature=data["temperature"]
    wind_speed=data["wind"]
    description=data["description"]

    print(f"The wheather in {city.title()} {temperature} the wind speed is {wind_speed}: {description}")
    # Wheather about next days
    while True:
        day=input("Want to know the weather tomorrow (1) the day after tomorrow (2) three days period (3).(Write Number) or No!  ")
        
        if day.lower()=="no":
        
            break
        wheather=data['forecast'][int(day)-1]
        ttemperature=wheather["temperature"]
        twind_speed=wheather["wind"]
        
        print(f"The wheather in {city.title()}  {ttemperature} the wind speed is {twind_speed}:")
        print("_________________________")
else:
    print("Error with response! Try again")