import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv


params = {
    "q" : "Gas Tank Size",
    'api_key':""
}
ground_clearance_model_list = []
years=[]
model_names = []
ground_clearance_values=[]
#website = 
html = requests.get(website, params=params)
soup = BeautifulSoup(html.text, 'html.parser')
results = soup.find_all('a', class_='is-size-5')
ground_clearance = results[7]
gc_tag = ground_clearance['href']
# print(gc_tag)
link = website+gc_tag
# print(link)
html2 = requests.get(link)
soup2 = BeautifulSoup(html2.text, 'html.parser')
results2 = soup2.find_all("li")
for i in results2:
    # print(i)
    soup3 = BeautifulSoup(str(i), 'html.parser')
    a_tag = soup3.find('a')
    if a_tag and 'href' in a_tag.attrs:
        href_value = a_tag['href']
        model_ground_clearance = website+href_value
        ground_clearance_model_list.append(model_ground_clearance)
print(ground_clearance_model_list)
