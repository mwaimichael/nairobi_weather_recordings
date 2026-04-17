from sqlalchemy import create_engine
from transform import transform
from config import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER
import pandas as pd



engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

def load():
    df = transform()

    if df.empty:
        print('No Data!')
        return

    try:
        df.to_sql(name='nairobi_weather_records', con=engine, if_exists='append', index=False)
    except Exception as e:
        print(e)

    print(df)