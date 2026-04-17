# Nairobi Weather ETL Pipeline

A lightweight ETL pipeline that extracts daily midday weather data for Nairobi, Kenya from the OpenWeatherMap API, transforms it into a structured format, and loads it into a PostgreSQL database.
The pipeline runs daily at 12:00 noon (EAT) and collects the following meteorological elements using metric units:
1. Temperature(°C)
2. Humidity(%)
3. Atmospheric Pressure(hPa)
4. Wind Speed(m/s)
5. General weather pattern

### Pipeline Architecture
Extract $\huge\rightarrow$ Transform $\huge\rightarrow$ Load

Extract - Fetches current weather data from the OpenWeatherMap API using an API key

Transform - Parses and structures the raw JSON response into a Pandas DataFrame.Date of record is also added.

Load - Appends the transformed records into a PostgreSQL database
