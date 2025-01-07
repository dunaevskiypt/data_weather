import requests
from dotenv import load_dotenv
import time
import json
import os
load_dotenv()

# API ключ
api_key = os.getenv('OPENWEATHERMAP_API_KEY')

# Список городов с их координатами
cities = [
    {'name': 'New York', 'lat': 40.7128, 'lon': -74.0060},
    {'name': 'Tokyo', 'lat': 35.6762, 'lon': 139.6503},
    {'name': 'London', 'lat': 51.5074, 'lon': -0.1278},
    {'name': 'Paris', 'lat': 48.8566, 'lon': 2.3522},
    {'name': 'Moscow', 'lat': 55.7558, 'lon': 37.6173},
    {'name': 'Sydney', 'lat': -33.8688, 'lon': 151.2093},
    {'name': 'Beijing', 'lat': 39.9042, 'lon': 116.4074},
    {'name': 'Los Angeles', 'lat': 34.0522, 'lon': -118.2437},
    {'name': 'Berlin', 'lat': 52.5200, 'lon': 13.4050},
    {'name': 'Cape Town', 'lat': -33.9249, 'lon': 18.4241},
    {'name': 'São Paulo', 'lat': -23.5505, 'lon': -46.6333},
    {'name': 'Mexico City', 'lat': 19.4326, 'lon': -99.1332},
    {'name': 'Mumbai', 'lat': 19.0760, 'lon': 72.8777},
    {'name': 'Cairo', 'lat': 30.0444, 'lon': 31.2357},
    {'name': 'Rio de Janeiro', 'lat': -22.9068, 'lon': -43.1729},
    {'name': 'Dubai', 'lat': 25.276987, 'lon': 55.296249},
    {'name': 'Toronto', 'lat': 43.65107, 'lon': -79.347015},
    {'name': 'Hong Kong', 'lat': 22.3193, 'lon': 114.1694},
    {'name': 'Seoul', 'lat': 37.5665, 'lon': 126.9780},
    {'name': 'Singapore', 'lat': 1.3521, 'lon': 103.8198},
    {'name': 'Buenos Aires', 'lat': -34.6037, 'lon': -58.3816},
    {'name': 'Istanbul', 'lat': 41.0082, 'lon': 28.9784},
    {'name': 'Jakarta', 'lat': -6.2088, 'lon': 106.8456},
    {'name': 'Lagos', 'lat': 6.5244, 'lon': 3.3792},
    {'name': 'Bangkok', 'lat': 13.7563, 'lon': 100.5018},
    {'name': 'Shanghai', 'lat': 31.2304, 'lon': 121.4737},
    {'name': 'Kuala Lumpur', 'lat': 3.1390, 'lon': 101.6869},
    {'name': 'Stockholm', 'lat': 59.3293, 'lon': 18.0686},
    {'name': 'Rome', 'lat': 41.9028, 'lon': 12.4964},
    {'name': 'Madrid', 'lat': 40.4168, 'lon': -3.7038},
    {'name': 'Oslo', 'lat': 59.9139, 'lon': 10.7522},
    {'name': 'San Francisco', 'lat': 37.7749, 'lon': -122.4194},
    {'name': 'Helsinki', 'lat': 60.1695, 'lon': 24.9354},
    {'name': 'Santiago', 'lat': -33.4489, 'lon': -70.6693},
    {'name': 'Athens', 'lat': 37.9838, 'lon': 23.7275},
    {'name': 'Vienna', 'lat': 48.2082, 'lon': 16.3738},
    {'name': 'Auckland', 'lat': -36.8485, 'lon': 174.7633},
    {'name': 'Milan', 'lat': 45.4642, 'lon': 9.1900},
    {'name': 'Lima', 'lat': -12.0464, 'lon': -77.0428},
    {'name': 'Tel Aviv', 'lat': 32.0853, 'lon': 34.7818},
    {'name': 'Lagos', 'lat': 37.1024, 'lon': -8.6749},
    {'name': 'Chicago', 'lat': 41.8781, 'lon': -87.6298},
    {'name': 'Vancouver', 'lat': 49.2827, 'lon': -123.1207},
    {'name': 'Manila', 'lat': 14.5995, 'lon': 120.9842},
    {'name': 'Edinburgh', 'lat': 55.9533, 'lon': -3.1883},
    {'name': 'Bangalore', 'lat': 12.9716, 'lon': 77.5946},
    {'name': 'Nairobi', 'lat': -1.2864, 'lon': 36.8172},
    {'name': 'Copenhagen', 'lat': 55.6761, 'lon': 12.5683},
    {'name': 'Florence', 'lat': 43.7696, 'lon': 11.2558},
    {'name': 'Barcelona', 'lat': 41.3784, 'lon': 2.1920},
    {'name': 'Medellín', 'lat': 6.2442, 'lon': -75.5812},
    {'name': 'Warsaw', 'lat': 52.2298, 'lon': 21.0118},
    {'name': 'Doha', 'lat': 25.276987, 'lon': 55.296249},
    {'name': 'Chennai', 'lat': 13.0827, 'lon': 80.2707}
]

# URL для запроса погоды
base_url = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

# Функция для получения данных о погоде


def get_weather_data(lat, lon, api_key):
    url = base_url.format(lat=lat, lon=lon, api_key=api_key)
    response = requests.get(url)
    return response.json()

# Основная логика для запроса и сохранения данных


def collect_weather_data():
    while True:
        weather_data = {}
        for city in cities:
            city_name = city['name']
            lat = city['lat']
            lon = city['lon']
            data = get_weather_data(lat, lon, api_key)
            weather_data[city_name] = data
            print(f"Собраны данные для города {city_name}")

        # Сохраняем данные в JSON файл
        with open("weather_data.json", "a") as f:
            json.dump(weather_data, f, indent=4)
            f.write("\n")  # Добавляем новый блок данных с новой строки

        # Ожидаем 2 минуты перед следующим запросом
        time.sleep(120)


# Запуск
if __name__ == "__main__":
    collect_weather_data()
