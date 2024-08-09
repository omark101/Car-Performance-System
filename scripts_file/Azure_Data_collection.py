import requests
import csv
%pip install beautifulsoup4
from bs4 import BeautifulSoup

#main_url = "  " 
response = requests.get(main_url)
soup = BeautifulSoup(response.content, 'html.parser')

brands = soup.find_all('div', class_='col-2')[1:]
href = []
brand_names = []
final_links = []

for brand in brands:
    href.append(brand.find('a')['href'])
    brand_names.append(brand.text.strip())
print(brand_names)

cars = []
cars_models = []
for brand_url in href:
    response = requests.get(brand_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    models = soup.find_all('div', class_='col-4')
    # print(models)
    for model in models:
        a = model.find('a')
        if a:
            cars.append(a['href'])
print(cars)


for car in cars:
    response = requests.get(car)
    soup = BeautifulSoup(response.content, 'html.parser')
    models = soup.find_all('div', class_='col-4')
    # print(models)
    for model in models:
        a = model.find('a')
        if a:
          link = a['href']
#            if link.startswith("      "): 
            cars_models.append(link)

for car_model in cars_models:
    response = requests.get(car_model)
    soup = BeautifulSoup(response.content, 'html.parser')
    models = soup.find_all('div', class_='col-6')
    for model in models:
        h3_tag = model.find('h3')
        if h3_tag:
            a = h3_tag.find('a')
            if a:
                link = a['href']
                # if link.startswith("    "): 
                    final_links.append(link)




csv_filename = 'FinalBigData.csv'

all_data = []
processed_links = set()

for url in final_links:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    head = soup.find("h1")
    name = head.text.split()
    modified_name = name[0] + ' ' + ' '.join(name[:-1])
    print(modified_name)

    combined_data_dict = {'URL': url, 'Name': modified_name}

    view_specss = soup.find_all("a", class_="viewphotosbutton")

    for view_specs in view_specss:
        view_specs_url = view_specs['href']
        if view_specs_url not in processed_links:
            processed_links.add(view_specs_url)
            view_response = requests.get(view_specs_url)
            view_soup = BeautifulSoup(view_response.text, 'html.parser')
            trs = view_soup.find_all("tr")

            for tr in trs:
                tds = tr.find_all("td")

                if len(tds) == 2:
                    key = tds[0].text.strip().rstrip(':')
                    value = tds[1].text.strip()

                    combined_data_dict[key] = value

    all_data.append(combined_data_dict)

all_keys = set()
for data in all_data:
    all_keys.update(data.keys())
print(len(all_keys))
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=all_keys)
    writer.writeheader()
    writer.writerows(all_data)

print(f"Data has been written to {csv_filename}")
print(len(combined_data_dict))
