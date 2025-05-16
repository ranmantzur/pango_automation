import sqlite3

class DatabaseHelper:
    def __init__(self, db_name="data.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS weather_data (
                    city TEXT PRIMARY KEY,
                    temperature_web REAL,
                    feels_like_web REAL,
                    temperature_api REAL,
                    feels_like_api REAL,
                    avg_temperature REAL
                )
            ''')

    def insert_weather_data(self, city, temperature_web, feels_like_web, temperature_api, feels_like_api):
        avg_temperature = (temperature_web + temperature_api) / 2
        with self.conn:
            self.conn.execute('''
                INSERT INTO weather_data (city, temperature_web, feels_like_web, temperature_api, feels_like_api, avg_temperature)
                VALUES (?, ?, ?, ?, ?, ?)
                ON CONFLICT(city) DO UPDATE SET
                    temperature_web=excluded.temperature_web,
                    feels_like_web=excluded.feels_like_web,
                    temperature_api=excluded.temperature_api,
                    feels_like_api=excluded.feels_like_api,
                    avg_temperature=excluded.avg_temperature
            ''', (city, temperature_web, feels_like_web, temperature_api, feels_like_api, avg_temperature))

    def get_weather_data(self, city):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM weather_data WHERE city=?', (city,))
        row = cursor.fetchone()
        if row:
            return {
                'city': row[0],
                'temperature_web': row[1],
                'feels_like_web': row[2],
                'temperature_api': row[3],
                'feels_like_api': row[4],
                'avg_temperature': row[5],
            }
        else:
            return None

    def close(self):
        self.conn.close()

# דוגמה לשימוש
if __name__ == "__main__":
    db = DatabaseHelper()
    db.insert_weather_data("Rome", 18.0, 17.0, 19.0, 18.5)
    data = db.get_weather_data("Rome")
    print(data)
    db.close()
