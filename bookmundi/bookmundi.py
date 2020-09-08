import pandas as pd
import numpy
import requests
from bs4 import BeautifulSoup
import csv

visitingnepal = [ ]
for x in range(1,45):
    url="https://www.bookmundi.com/nepal?page="
    r=  requests.get(url+str(x))

    htmlcontent=r.content

    soup=BeautifulSoup(htmlcontent,'html.parser')

    placelist=soup.find(id='tours-main-holder')
    place=placelist.find_all(class_='details-block')
    for places in place:
        placename=places.find('h4').get_text()
        print(placename)
        tourtype=places.find(class_="txt").get_text()

        bookmundi ={
            'Place': placename,
            'TourType': tourtype
        }
        visitingnepal.append(bookmundi)
    print(visitingnepal)


df=pd.DataFrame(visitingnepal)
df.to_csv('bookmundi/bookmundi.csv')