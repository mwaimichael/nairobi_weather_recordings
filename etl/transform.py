import pandas as pd
from datetime import date
from extract import extract

def transform():
    data = extract()
    cleaned_data = {
        "date" : date.today(),
        "weather_pattern": data.get("weather")[0].get("main"),
        "weather_description": data.get("weather")[0].get("description"),
        "temperature": data.get("main").get("temp"),
        "humidity(%)": data.get("main").get("humidity"),
        "pressure(hpa)": data.get("main").get("grnd_level"),
        "wind_speed": data.get("wind").get("speed")
    }


    df = pd.DataFrame(cleaned_data, index=[0])
    print(df)

    #print(cleaned_data)

    return df

transform()