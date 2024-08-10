import requests
from bs4 import BeautifulSoup
import csv

# urls = 

all_data = []

def get_year(caption):
    return caption[:4]

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    h1_text = soup.find('h1').get_text(strip=True)
    model = h1_text.split('Headroom')[0]

    tables = soup.find_all('table', {'class': 'table is-bordered'})

    for table in tables:
        caption = table.find('caption').get_text(strip=True)
        year = get_year(caption)

        rows = table.find_all('tr')
        if len(rows) > 4:
            for row in rows[1:]:
                cells = row.find_all('td')
                model = row.find_all("th")
                if len(cells) >= 3:
                    all_data.append({
                        "make":model,
                        'Year': year,
                        'Model': model[0].get_text(strip=True),
                        'Front Row Headroom': cells[0].get_text(strip=True),
                        'Second Row Headroom': cells[1].get_text(strip=True),
                        'Third Row Headroom': cells[2].get_text(strip=True)
                    })
        elif len(rows) == 4:
            model = soup.find("h1")
            model = model.text.strip()
            model = model.split("Headroom")[0]

            all_data.append({
                "make":model,
                'Year': year,
                'Model': model,
                'Front Row Headroom': rows[1].find('td').get_text(strip=True),
                'Second Row Headroom': rows[2].find('td').get_text(strip=True),
                'Third Row Headroom': rows[3].find('td').get_text(strip=True)
            })

for data in all_data:
    print(f"Year: {data['Year']}, Model: {data['Model']}, Front Row Headroom: {data['Front Row Headroom']}, Second Row Headroom: {data['Second Row Headroom']}, Third Row Headroom: {data['Third Row Headroom']}")

csv_filename = 'Headroom.csv'

with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ["make",'Year', 'Model', 'Front Row Headroom', 'Second Row Headroom', 'Third Row Headroom']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for data in all_data:
        writer.writerow(data)

print(f"Data has been written to {csv_filename}")
