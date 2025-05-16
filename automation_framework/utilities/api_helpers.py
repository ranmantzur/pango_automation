import requests

class ApiHelper:
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    API_KEY = "f88d54cd8eddb5d1f23ff82a80b95fec"
    
    def get_current_weather(self, city):
        try:
            url = f"{self.BASE_URL}?q={city}&appid={self.API_KEY}"
            response = requests.get(url)
            data = response.json()
            return data["main"]["temp"], data["main"]["feels_like"]
        except Exception as e:
            print(f"[API ERROR] {city}: {e}")
            return None, None


if __name__ == "__main__":
    api = ApiHelper()
    print(api.get_current_weather(city="London"))