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
    for places in place:
        placename=places.find('h4').get_text()
        tourtype=places.find(class_="txt").get_text()


    bookmundi={
        'Thay':placename,
        'tour':tourtype
    }
    visiting_nepal.append(bookmundi)


df=pd.DataFrame(visiting_nepal)
df.to_csv('bookmundi/bookmundi.csv')