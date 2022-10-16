""" 
    1st Problem :
    Download and change desktop Wallpapers automatically
"""
import requests
import json
import PyWallpaper

api_link = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'

# get json 
responce = requests.get(api_link)
content = responce.content.decode('UTF-8')
# print(responce)
# print(content)

# Convert String to json 
dist_content = json.loads(content)
# print(type(dist_content))

# get the image Url
image_url = dist_content['url']
# print(image_url)

# download the image  
res = requests.get(image_url)
# print(res)

# Save the image 
with open('apod.png', 'wb') as image:
    image.write(res.content)

# Set as Wallpaper 
PyWallpaper.change_wallpaper('C:/Users/Md Maruf/Desktop/python/module06/apod.png')



 

