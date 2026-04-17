import requests
from pprint import pprint
from config import API_KEY


# url to coordinates of Nairobi, Kenya
url_get_location = f"http://api.openweathermap.org/geo/1.0/direct?q=nairobi,kenya&limit=1&appid={API_KEY}"

# get latitude and longitude coordinates of Nairobi 
def get_loc():
    try:
        response = requests.get(url_get_location)
        print(response.raise_for_status)
        data = response.json()[0]
        #pprint(data)
        lat, lon = data.get("lat"), data.get("lon")
        return lat, lon
    except Exception as e:
        print(e)

print(get_loc())