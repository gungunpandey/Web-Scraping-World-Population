import requests
from bs4 import BeautifulSoup
import os
from csv import writer
import pandas as pd

url = "https://www.worldometers.info/world-population/population-by-country/"

def scrape(url):
    responses = requests.get(url)
    soup = BeautifulSoup(responses.text, 'html.parser')
    return soup

scraped = scrape(url)

rows = scraped.find('table',{'id':'example2'})

countries_list = []
for i in rows.find_all('th'):
    countries_list.append(i.text)

path = os.path.join(os.getcwd(), "World_population_by_county.csv")

with open(path, 'wt', newline = "", encoding = 'utf-8') as csv_file:
    csv_writer = writer(csv_file, delimiter='|')
    csv_writer.writerow(countries_list)

    for row in rows.find_all('tr')[1:]:
        td = row.find_all('td')
        r = [i.text.replace('\n', '') for i in td]
        csv_writer.writerow(r)
