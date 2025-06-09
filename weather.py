import requests
import sys

def main():
    try:
        weather_api = fetch_api()
        handle_reponse(weather_api)
    except requests.RequestException:
        sys.exit("City not found or API error.")
   
def fetch_api():
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={sys.argv[1]}&appid=f2d9d2b55392aa1bc1eb464ef00cc88d&units=metric")
    return  response.json()
   
def handle_reponse(weather_api):
    temp = weather_api['main']['temp']
    feels_like = weather_api['main']['feels_like']
    min_temp = weather_api['main']['temp_min']
    max_temp = weather_api['main']['temp_max']
    print(f"The temp in {sys.argv[1]} is {temp} it does feel like {feels_like} but the range is going to be {min_temp} to {max_temp}")

if __name__ == "__main__":
    main()