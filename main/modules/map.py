import requests
import json

def get_location():
    API_KEY = "AIzaSyCF-swsZ0P4v0rMIYR0GP_a9Ro51uDmRC8"

    url = f'https://www.googleapis.com/geolocation/v1/geolocate?key={API_KEY}'

    data = {
        'considerIp': True,
    }

    result = requests.post(url, data) 
    location = json.loads(result.text)

    lat = location["location"]["lat"]
    lng = location["location"]["lng"]
    
    return lat, lng
    # print(lat, lng)