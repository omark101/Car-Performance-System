import requests
from bs4 import BeautifulSoup
import csv

# urls = []

def extract_table_data(soup, year, make):
    table_data = []
    table = soup.find('h3', id=year).find_next('table')
    rows = table.find_all('tr')[1:]
    for row in rows:
        cells = row.find_all('td')
        trim_package = row.find('th').text.strip()
        engine = row.find_all('th')[1].text.strip()
        gas_tank_size_imperial = cells[0].text.strip()
        gas_tank_size_metric = cells[1].text.strip()
        full_tank_range_city = cells[2].text.strip()
        full_tank_range_highway = cells[3].text.strip()
        gas_mileage_city = cells[4].text.strip()
        gas_mileage_highway = cells[5].text.strip()

        table_data.append({
            'Make': make,
            'Year': year,
            'Trim Package': trim_package,
            'Engine': engine,
            'Gas Tank Size (imperial)': gas_tank_size_imperial,
            'Gas Tank Size (metric)': gas_tank_size_metric,
            'Full Tank Range - City': full_tank_range_city,
            'Full Tank Range - Highway': full_tank_range_highway,
            'Gas Mileage - City': gas_mileage_city,
            'Gas Mileage - Highway': gas_mileage_highway
        })
    return table_data

all_data = []

for url in urls:
    r = requests.get(url)
    html_content = r.content
    soup = BeautifulSoup(html_content, 'html.parser')
    
    make = soup.find('h1').text.split("Gas Tank")[0].strip()

    years = [h3['id'] for h3 in soup.find_all('h3') if h3['id'].isdigit()]

    for year in years:
        all_data.extend(extract_table_data(soup, year, make))

csv_file_name = 'acura_data_with_make.csv'

if all_data:
    with open(csv_file_name, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=all_data[0].keys())
        writer.writeheader()
        writer.writerows(all_data)

for entry in all_data:
    print(entry)
