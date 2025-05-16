from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def get_weather(driver, city_name):
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.timeanddate.com/weather/")

    search_box = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.main-content-div > header > div.fixed > div > form > input"))
    )
    search_box.clear()
    search_box.send_keys(city_name)
    search_box.send_keys(Keys.ENTER)

    city_link = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.main-content-div > section.bg--grey.pdflexi-t--small > div > section:nth-child(5) > div:nth-child(3) > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > a"))
    )
    city_link.click()

    temp_text = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#qlook > div.h2"))
    ).text
    temp = float(temp_text.split("°")[0])

    feel_like_text = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#qlook > p:nth-child(6)"))
    ).text

    feel_like_value = feel_like_text.replace("Feels Like:", "").strip().split("°")[0]
    feel_like = float(feel_like_value)

    return temp, feel_like

def search_city(city_name):
    driver = None
    try:
        driver = setup_driver()
        temp, feel_like = get_weather(driver, city_name)
        return temp, feel_like
    except Exception as e:
        print(f"Error occurred while scraping {city_name}: {e}")
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    result = search_city("Bangkok")
    if result:
        temp, feel_like = result
        print(f"Temperature: {temp}°C, Feels like: {feel_like}°C")
    else:
        print("Failed to get weather data.")
