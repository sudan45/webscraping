import pandas as pd
import numpy
import requests
from bs4 import BeautifulSoup
import csv

visiting_nepal = []
for x in range(1,45):
    url="https://www.bookmundi.com/nepal?page="
    r=  requests.get(url+str(x))

    htmlcontent=r.content

    soup=BeautifulSoup(htmlcontent,'html.parser')

    placelist=soup.find(id='tours-main-holder')
    place=placelist.find_all(class_='text-details')
    print(place[0].find('a',class_="target-link").get_text())

    placename=[places.find('a',class_="target-link").get_text() for places in place]


    bookmundi={
        'Thay':placename
    }
    visiting_nepal.append(bookmundi)


df=pd.DataFrame(visiting_nepal)
df.to_csv('bookmundi/bookmundi.csv')