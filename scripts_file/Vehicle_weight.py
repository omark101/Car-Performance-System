import requests
from bs4 import BeautifulSoup
import csv

# urls = []

def scrape_data(url):
    r = requests.get(url)
    html_content = r.content
    soup = BeautifulSoup(html_content, 'html.parser')

    model_name = soup.find('h1').text.strip().split("Vehicle")[0]

    tables = soup.find_all('table', class_='table is-bordered')

    data = []

    for table in tables:
        year_text = table.find_previous('h3').text.strip()
        year = year_text.split()[0]

        rows = table.find('tbody').find_all('tr')

        for row in rows:
            columns = row.find_all('td')
            if columns:
                trim_package = row.find('th', scope='row').text.strip()
                engine = columns[0].text.strip()
                weight_imperial = columns[1].text.strip()
                weight_metric = columns[2].text.strip()

                data.append([model_name, year, trim_package, engine, weight_imperial, weight_metric])

    return data

combined_data = []

for url in urls:
    data = scrape_data(url)
    combined_data.extend(data)

csv_file = "combined_weights.csv"

with open(csv_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Model Name", "Year", "Trim Package", "Engine", "Weight (imperial)", "Weight (metric)"])
    writer.writerows(combined_data)

print(f"All data from {len(urls)} URLs has been successfully saved to {csv_file}.")
