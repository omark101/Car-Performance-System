import requests
import csv
from bs4 import BeautifulSoup

def extract_data_from_table(table, year, make):
    rows = table.find_all('tr')
    data = []

    if len(rows) == 3:
        imperial_clearance = rows[1].find_all('td')[0].text.strip()
        metric_clearance = rows[2].find_all('td')[0].text.strip()
        model_trim_package = make
        data.append([make, year, model_trim_package, imperial_clearance, metric_clearance])
    else:
        for row in rows[1:]:
            cols = row.find_all('td')
            if len(cols) == 2:
                model_trim_package = row.find('th').text.strip()
                imperial_clearance = cols[0].text.strip()
                metric_clearance = cols[1].text.strip()
                data.append([make, year, model_trim_package, imperial_clearance, metric_clearance])

    return data

def scrape_ground_clearance(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    print(soup)
    tables = soup.find_all('table', class_='table is-bordered')
    all_data = []

    for table in tables:
        caption = table.find('caption').text.strip()
        year = caption.split()[0]
        make = soup.find('h1').text.split("Ground Clearance")[0].strip()
        table_data = extract_data_from_table(table, year, make)
        all_data.extend(table_data)

    return all_data

def process_urls(urls):
    all_data = []

    for url in urls:
        r = requests.get(url)
        html_content = r.content
        data = scrape_ground_clearance(html_content)
        all_data.extend(data)

    return all_data

def write_to_csv(data, filename='ground_clearance.csv'):
    headers = ["Make", "Year", "Model-Trim Package", "Min. Ground Clearance (imperial)", "Min. Ground Clearance (metric)"]
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

# List of URLs to scrape
# urls = []


data = process_urls(urls)
write_to_csv(data)

for row in data:
    print(row)
