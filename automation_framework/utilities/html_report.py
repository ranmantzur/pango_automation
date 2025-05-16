import os
import statistics
import webbrowser


def generate_html_report(data, threshold=2.0, filename="weather_report.html"):
    discrepant_cities = []
    discrepancies = []

    for row in data:
        city, temp_web, feels_web, temp_api, feels_api, avg_temp = row
        if None in (temp_web, temp_api):
            continue
        diff = abs(temp_web - temp_api)
        discrepancies.append(diff)
        if diff > threshold:
            discrepant_cities.append((city, temp_web, temp_api, diff))

    mean_diff = statistics.mean(discrepancies) if discrepancies else 0
    max_diff = max(discrepancies) if discrepancies else 0
    min_diff = min(discrepancies) if discrepancies else 0

    html_content = f"""
    <html>
    <head><title>Weather Discrepancy Report</title></head>
    <body>
        <h1>Weather Discrepancy Report</h1>
        <p>Threshold: {threshold}°C</p>
        <h2>Cities with Discrepancies</h2>
        <table border="1" cellpadding="5" cellspacing="0">
            <tr><th>City</th><th>Temp Web</th><th>Temp API</th><th>Difference</th></tr>
    """

    for city, temp_web, temp_api, diff in discrepant_cities:
        html_content += f"<tr><td>{city}</td><td>{temp_web}</td><td>{temp_api}</td><td>{diff:.2f}</td></tr>"

    html_content += f"""
        </table>
        <h3>Summary</h3>
        <ul>
            <li>Mean discrepancy: {mean_diff:.2f}°C</li>
            <li>Max discrepancy: {max_diff:.2f}°C</li>
            <li>Min discrepancy: {min_diff:.2f}°C</li>
        </ul>
    </body>
    </html>
    """

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Report generated: {filename}")
    webbrowser.open('file://' + os.path.realpath(filename))