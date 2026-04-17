import requests
from pprint import pprint
from config import API_KEY


# url to coordinates of Nairobi, Kenya
url_get_location = f"http://api.openweathermap.org/geo/1.0/direct?q=nairobi,kenya&limit=1&appid={API_KEY}"

def extract():
    # get latitude and longitude coordinates of Nairobi 
    def get_loc():
        try:
            loc_response = requests.get(url_get_location)
            loc_response.raise_for_status
            data = loc_response.json()[0]
            #pprint(data)
            lat, lon = data.get("lat"), data.get("lon")
            return lat, lon
        except Exception as e:
            print(e)

        

    # url to get weather data of nairobi
    url_get_data = f"https://api.openweathermap.org/data/2.5/weather?lat={get_loc()[0]}&lon={get_loc()[1]}&appid={API_KEY}&units=metric"


    def source_data():
        try:
            data_response = requests.get(url_get_data)
            data_response.raise_for_status
            data = data_response.json()
            pprint(data)
            return data
        except Exception as ex:
            print(ex)

    data = source_data()

    return data


data = extract()
pprint(data)

