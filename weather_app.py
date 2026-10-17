import urllib.request
import json

def get_weather(city):
    #Open-Meteo
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    geo = json.loads(urllib.request.urlopen(geo_url).read())
    if not geo.get("results"):
        return None
    Iat, Ion = geo["results"][0]["latitude"], geo["results"][0]["longitude"]
    wx_url = (f"https://api.open-meteo.com/v1/forecast?" f"latitude={Iat}&longitude={Ion}&current=temperature_2m,weather_code")
    wx = json.loads(urllib.request.urlopen(wx_url).read())
    return wx["current"]

if __name__ == "__main__":
    city = input("City: ")
    print(get_weather(city))
