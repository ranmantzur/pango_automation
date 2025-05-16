# 🌤 Weather Discrepancy Analyzer

A Python-based automation project that compares real-time weather data from [TimeAndDate.com](https://www.timeanddate.com/weather/) and [OpenWeatherMap](https://openweathermap.org/) API. The project stores the collected data in a SQLite database and generates a report highlighting temperature discrepancies.

---

## 📌 Project Features

- Scrapes "temperature" and "feels like" values from a weather website using Selenium.
- Fetches corresponding data from OpenWeatherMap API.
- Supports 20 configurable cities.
- Stores data in a local SQLite database.
- Calculates average temperature between sources.
- Generates an HTML report showing discrepancies exceeding a threshold.

---

## 🧰 Technologies Used

- Python 3.8+
- Selenium (for web scraping)
- Requests (for API calls)
- SQLite (local database)
- WebDriver Manager (automated ChromeDriver installation)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ranmantzur/pango_automation.git
cd pango_automation
