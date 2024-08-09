import requests
from bs4 import BeautifulSoup
import csv

# urls = 


all_data = []

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tables = soup.find_all('table', {'class': 'table is-bordered'})

    h1_tag = soup.find('h1')
    if h1_tag:
        make = h1_tag.get_text(strip=True).split("Tire")[0].strip()
    else:
        make = "Unknown"

    for table in tables:
        caption = table.find('caption').get_text(strip=True)
        year = caption[:4]  

        rows = table.find_all('tr')
        for row in rows[1:]:  
            model = row.find('th').get_text(strip=True)
            cells = row.find_all('td')
            if len(cells) >= 2:
                tire_size = cells[0].get_text(strip=True)
                wheel_rim_size = cells[1].get_text(strip=True)
                all_data.append({
                    'Make': make,
                    'Year': year,
                    'Model': model,
                    'Tire Size': tire_size,
                    'Wheel (Rim) Size': wheel_rim_size
                })

for data in all_data:
    print(f"Make: {data['Make']}, Year: {data['Year']}, Model: {data['Model']}, Tire Size: {data['Tire Size']}, Wheel (Rim) Size: {data['Wheel (Rim) Size']}")

csv_filename = 'tire_and_wheel_sizes.csv'

with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Make', 'Year', 'Model', 'Tire Size', 'Wheel (Rim) Size']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for data in all_data:
        writer.writerow(data)

print(f"Data has been written to {csv_filename}")
