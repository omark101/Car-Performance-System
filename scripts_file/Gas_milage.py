import requests
from bs4 import BeautifulSoup
import csv

def extract_data_from_table(table, year, make):
    rows = table.find('tbody').find_all('tr')
    data = []

    for row in rows:
        cols = row.find_all('td')
        if len(cols) == 7:
            model = row.find('th').text.strip()
            engine = cols[0].text.strip()
            combined_gas_mileage_imperial = cols[1].text.strip()
            city_gas_mileage_imperial = cols[2].text.strip()
            highway_gas_mileage_imperial = cols[3].text.strip()
            combined_gas_mileage_metric = cols[4].text.strip()
            city_gas_mileage_metric = cols[5].text.strip()
            highway_gas_mileage_metric = cols[6].text.strip()
            data.append([make, model, year, engine, combined_gas_mileage_imperial, city_gas_mileage_imperial, highway_gas_mileage_imperial, combined_gas_mileage_metric, city_gas_mileage_metric, highway_gas_mileage_metric])
        else:
            print(f"Unexpected row structure in table, skipping row: {row}")

    return data

def scrape_gas_mileage(html_content, url):
    soup = BeautifulSoup(html_content, 'html.parser')
    tables = soup.find_all('table', class_='table is-bordered')
    all_data = []

    make = 'N/A'
    h1 = soup.find('h1')
    if h1:
        h1_text = h1.get_text(strip=True)
        if 'Gas Mileage' in h1_text:
            make = h1_text.split('Gas Mileage')[0].strip()
        else:
            print(f"Unexpected H1 structure, skipping URL: {url}")
            return all_data

    for table in tables:
        caption = table.find('caption')
        if caption:
            caption_text = caption.get_text(strip=True)
            year = caption_text.split()[0][:4]
        else:
            year = 'N/A'

        table_data = extract_data_from_table(table, year, make)
        all_data.extend(table_data)

    return all_data

def write_to_csv(data, filename='gas_mileage.csv'):
    headers = ["Make", "Model", "Year", "Engine", "Combined Gas Mileage (imperial)", "City Gas Mileage (imperial)", "Highway Gas Mileage (imperial)", "Combined Gas Mileage (metric)", "City Gas Mileage (metric)", "Highway Gas Mileage (metric)"]
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

# urls =

all_data = []
for url in urls:
    r = requests.get(url)
    html_content = r.content
    data = scrape_gas_mileage(html_content, url)
    all_data.extend(data)

write_to_csv(all_data)

for row in all_data:
    print(row)
