import time



from automation_framework.utilities.api_helpers import ApiHelper
from automation_framework.utilities.db_helpers import DatabaseHelper
from automation_framework.utilities.html_report import generate_html_report
from automation_framework.utilities.web_scraper import setup_driver, get_weather


def main():
    cities = [
        "Bangkok", "London", "Paris", "New York", "Tokyo",
        "Sydney", "Moscow", "Dubai", "Rome", "Berlin",
        "Madrid", "Toronto", "Mumbai", "Cairo", "Beijing",
        "Buenos Aires", "Cape Town", "Chicago", "Singapore", "Los Angeles"
    ]

    db = DatabaseHelper()
    api_helper = ApiHelper()
    driver = setup_driver()

    for city in cities:
        print(f"Processing {city}...")
        temp_web, feels_web = get_weather(driver, city)
        temp_api, feels_api = api_helper.get_current_weather(city)
        print(f"Web: {temp_web}, API: {temp_api}")

        db.insert_weather_data(city, temp_web, feels_web, temp_api, feels_api)
        time.sleep(1)

    driver.quit()

    data = db.conn.execute('SELECT * FROM weather_data').fetchall()
    generate_html_report(data)
    db.close()


if __name__ == "__main__":
    main()