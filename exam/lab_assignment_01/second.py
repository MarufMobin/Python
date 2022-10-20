""" import requests
import json
import time 

api_url = 'https://api.openweathermap.org/data/2.5/weather?q=dhaka&appid=4b5f5c378962441c1c0063e2bb400c5c'


def weather_data( api_url ):
    response = requests.get(api_url)
    content = response.content.decode('UTF-8')
    dist_content = json.loads(content)
    # print(dist_content['weather'])
    display_output(dist_content)

def display_output( weather_info ):
    print("************Weather Information ***************")
    for key, value in weather_info.items():
        # if type(key) == 'dict':
        #     for key, val in value.items():
        #         print(f'  >> {key} : {val}')
        # elif type(key) == 'list':
        #     print(f'{key}')
        #     for val in value:
        #         print(f' : {val}')
        # else :
        print(f' >> {key} : {value}')
        


weather_data(api_url)

# while True:
#     weather_data(api_url)
#     time.sleep(3600) 
# 
# """

import requests
import time
import math
 
 
def weather_data():
    while True:
        city_name = 'dhaka'
        complete_url = "http://api.openweathermap.org/data/2.5/weather?appid=262513e9dace53bc78a34d30e0cd1983&q="+city_name
 
        response = requests.get(complete_url)
 
        x = response.json()
 
        y = x["main"]
 
        current_temperature = y["temp"]
        celsius = math.ceil(current_temperature-273.15)
 
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
 
        print("Temperature in Celsius = " + str(celsius) + ' C')
        print("humidity in percentage = " + str(current_humidity))
        print("description = " + str(weather_description))
 
        time.sleep(1800)
 
 
weather_data()