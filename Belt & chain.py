import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
params = {
    "q" : "belt or chain",
    'api_key':"      "
}
belt_or_chain_model_list = []
years=[]
model_names = []
all_data = []
belt_or_chain_list=[]
replacement = []
interfernce = []
#website = "      "
html = requests.get(website, params=params)
soup = BeautifulSoup(html.text, 'html.parser')
results = soup.find_all('a', class_='is-size-5')
belt_or_chain = results[14]
gc_tag = belt_or_chain['href']
link = website+gc_tag
html2 = requests.get(link)
soup2 = BeautifulSoup(html2.text, 'html.parser')
results2 = soup2.find_all("li")
for i in results2:
    soup3 = BeautifulSoup(str(i), 'html.parser')
    a_tag = soup3.find('a')
    if a_tag and 'href' in a_tag.attrs:
        href_value = a_tag['href']
        model_ground_clearance = website+href_value
        belt_or_chain_model_list.append(model_ground_clearance)
print(belt_or_chain_model_list)

for gc_data in belt_or_chain_model_list:
  html4 = requests.get(gc_data)
  soup4 = BeautifulSoup(html4.text, 'html.parser')
  # print(soup4)
  head = soup4.find_all("h3")
  for i in head:
      model_year = i.text.strip().split(" ")[0]
      years.append(model_year)
  head2 = soup4.find_all("h3")
  for i in head2:
      model_name = i.text.strip().split("Belt")[0]
      model_name_modified = model_name[5:]
      model_names.append(model_name_modified)
  belt_or_chain_value = soup4.find_all("tr")
  soup5 = BeautifulSoup(str(belt_or_chain_value), 'html.parser')
  td_tag = soup5.find_all('td', class_='text-center')
  for i in range(len(td_tag)):
      td_tag_scrap = td_tag[i].text
      all_data.append(td_tag_scrap)
print(years)
print(model_names)
for i in range(0, len(all_data)-1, 3):
  belt_or_chain_list.append(all_data[i])
  interfernce.append(all_data[i+1])
  replacement.append(all_data[i+2])
print(belt_or_chain_list)
print(interfernce)
print(replacement)
print(len(years))
print(len(model_names))
print(len(belt_or_chain_list))
print(len(interfernce))
print(len(replacement))


data = {
    "Year": years,
    "Model Name": model_names,
    "Belt or chain (cm)": belt_or_chain_list,
    "Interference or Non-interference": interfernce,
"Replacement Interval": replacement
}
df = pd.DataFrame(data)
print(df)
csv_file_path = "carspecs_belt_or_chain.csv"
df.to_csv(csv_file_path, index=False)
