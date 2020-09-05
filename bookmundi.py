import pandas as pd
import numpy
import requests
from bs4 import BeautifulSoup
import csv

url="https://www.bookmundi.com/nepal"

r=  requests.get(url)

htmlcontent=r.content

soup=BeautifulSoup(htmlcontent,'html.parser')

placelist=soup.find(id='tours-main-holder')
place=placelist.find_all(class_='details-block')


print(place[0].find(class_="target-link").get_text())

placename=[places.find(class_='target-link').get_text() for places in place]
print(placename)

bookmundi=pd.DataFrame({
    'placenamelist':placename,
})
print(bookmundi)

bookmundi.to_csv('bookmundi.csv')