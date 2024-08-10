import requests
from bs4 import BeautifulSoup
import csv

def scrape_vehicle_dimensions(url):
    csv_data = []

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    make = 'N/A'
    h1 = soup.find('h1')
    if h1:
        h1_text = h1.get_text(strip=True)
        if 'Vehicle Dimensions' in h1_text:
            make = h1_text.split('Vehicle Dimensions')[0].strip()

    tables = soup.find_all('table', {'class': 'table'})
    if not tables:
        print(f"No tables found, skipping URL: {url}")
    else:
        for table in tables:
            model = 'N/A'
            year = 'N/A'
            length = 'N/A'
            width = 'N/A'
            height = 'N/A'
            wheelbase = 'N/A'

            caption = table.find('caption')
            if caption:
                caption_text = caption.get_text(strip=True)
                parts = caption_text.split()
                year = parts[0][:4]
                model = caption_text[4:].split('Vehicle Dimensions')[0].strip()

            thead = table.find('thead')
            tbody = table.find('tbody')

            if thead and tbody:
                trs = tbody.find_all('tr')
                for tr in trs:
                    tds = tr.find_all('td')
                    if len(tds) >= 4:
                        model = tr.find('th').get_text(strip=True)
                        length = tds[0].get_text(strip=True)
                        width = tds[1].get_text(strip=True)
                        height = tds[2].get_text(strip=True)
                        wheelbase = tds[3].get_text(strip=True)
                        csv_data.append({'Make': make, 'Year': year, 'Model': model, 'Length': length, 'Width': width, 'Height': height, 'Wheelbase': wheelbase})

            elif tbody:
                trs = tbody.find_all('tr')
                if len(trs) >= 5:
                    for i in range(1, 5):
                        tds = trs[i].find_all('td')
                        if len(tds) >= 1:
                            if i == 1:
                                length = tds[0].get_text(strip=True)
                            elif i == 2:
                                width = tds[0].get_text(strip=True)
                            elif i == 3:
                                height = tds[0].get_text(strip=True)
                            elif i == 4:
                                wheelbase = tds[0].get_text(strip=True)
                    csv_data.append({'Make': make, 'Year': year, 'Model': model, 'Length': length, 'Width': width, 'Height': height, 'Wheelbase': wheelbase})

    return csv_data

# urls =

all_csv_data = []
for url in urls:
    print(f"Scraping data from URL: {url}")
    csv_data = scrape_vehicle_dimensions(url)
    all_csv_data.extend(csv_data)

csv_filename = "all_vehicle_dimensions.csv"
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Make', 'Year', 'Model', 'Length', 'Width', 'Height', 'Wheelbase']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for data in all_csv_data:
        writer.writerow(data)

print(f"All data saved to {csv_filename}")
