import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv

url="https://timesofindia.indiatimes.com/entertainment/latest-new-movies/horror-movies"

r=requests.get(url)
htmlcontent=r.content
soup=BeautifulSoup(htmlcontent,'html.parser')

movielist=soup.find(id="movies_wrapper")
movie=movielist.find_all(class_="mr_lft_box")


moviename=[movies.find('h3').get_text() for movies in movie]
# print(moviename)
actor_actoress=[movies.find(class_="castnames_wrapper").get_text() for movies in movie]
language_type=[movies.find('small').get_text() for movies in movie]
date_duration=[movies.find('h4').get_text() for movies in movie]



horror={
    'Moviename' : moviename,
    'Cast' : actor_actoress,
    'Language/Type' : language_type,
    'Date/Duration' : date_duration,
}


df=pd.DataFrame(horror,columns=['Moviename','Cast','Language/Type','Date/Duration'])
print(df)
df.to_csv('timesofindia/horror.csv')





