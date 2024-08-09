import requests
from bs4 import BeautifulSoup
import re
import csv
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def process_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching URL {url}: {e}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.title.text.strip()
    model_type = title.split('-')[0].strip()

    headings = soup.select('h3')
    tables = soup.find_all('table')
    data = []

    for heading, table in zip(headings, tables):
        year_text = heading.get_text(strip=True)
        year = year_text.split()[0]

        header_row = table.find('tr')
        if header_row:
            headers = [header.text.strip() for header in header_row.find_all(['th', 'td'])]
            if 'Horsepower' in headers and 'Torque' in headers:
                rows = table.find_all('tr')[1:]
                for row in rows:
                    cells = row.find_all(['th', 'td'])
                    if len(cells) >= 4:
                        model = cells[0].text.strip()
                        engine_capacity = cells[1].text.strip()
                        horsepower = cells[2].text.strip()
                        torque = cells[3].text.strip()

                        turbo = ["Supercharged", "Turbo"]
                        turbo_or_supercharger = "N/A"
                        for tur in turbo:
                            if tur in model:
                                turbo_or_supercharger = tur

                        cylinders = None
                        motor_type = ["V12", "V8", "V6","4 Cyl","6 Cyl","8 Cyl"]
                        for item in motor_type:
                            if item in model:
                                cylinders = item

                        car_types = ["Coupe", "SUV", "Hatchback", "4x4", "4x2", "Sedan", "Wagon"]
                        car_type = next((car_type for car_type in car_types if car_type in model), "N/A")

                        driving_modes = ["AWD", "FWD", "RWD", "2WD", "4WD"]
                        driving_mode = next((mode for mode in driving_modes if mode in model), "N/A")

                        data.append([model, model_type.split("Horsepower")[0], car_type, year,
                                     engine_capacity, horsepower, torque, driving_mode, cylinders, turbo_or_supercharger])
                    else:
                        logging.warning(f"Skipping row in {url} due to insufficient columns: {row}")

    return data

#urls =
csv_file_path = r"C:\Users\omera\Desktop\newfile.csv"

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Model", "Type", "Year", "Engine Capacity", "Horsepower", "Torque",
                     "Driving Mode", "Cylinders", "Turbo or SuperCharger"])

    for url in urls:
        data = process_url(url)
        writer.writerows(data)

logging.info(f"Data successfully written to {csv_file_path}")

print(len(urls))
