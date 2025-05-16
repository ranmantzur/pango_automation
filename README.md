# 🌤 Weather Discrepancy Analyzer

A Python automation framework that compares real-time temperature data between [TimeAndDate.com](https://www.timeanddate.com/weather/) and the [OpenWeatherMap API](https://openweathermap.org/). It stores the data in a SQLite database and generates a detailed HTML report identifying discrepancies between the two sources.

---

## 📦 Features

✅ Scrape current weather data (temperature + feels like) from TimeAndDate.com using Selenium  
✅ Fetch real-time weather data from OpenWeatherMap API  
✅ Automatically handle 20 random or predefined cities  
✅ Store results in a local SQLite database  
✅ Calculate average temperature from both sources  
✅ Generate an interactive HTML report with discrepancy summaries  

---

## 🧰 Tech Stack

- **Python 3.8+**
- **Selenium** – for website scraping  
- **Requests** – for REST API interactions  
- **SQLite** – for local data storage  
- **WebDriver Manager** – for automatic ChromeDriver setup  

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ranmantzur/pango_automation.git
cd pango_automation
```
### 2. Create a virtual environment
python -m venv venv

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run the application
python automation_framework/main.py






