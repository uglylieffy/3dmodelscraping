import requests
from bs4 import BeautifulSoup
import pandas as pd
# paid model 
# url = 'https://sketchfab.com/3d-models/juvenile-triceratops-fossil-51b6e27147b043ef9fb266a7cda57e35'
# free model 
# url = 'https://sketchfab.com/3d-models/coelophysis-c8fee7a21dbc465d8fae98a0df4d190e'
url = 'https://sketchfab.com/3d-models/dinosaur-footprint-0d1a34d4b027443f805aae6b83e75c5b'

paid = True
html = requests.get(url)
s = BeautifulSoup(html.content, 'html.parser')
stats = s.find_all('span', class_='count')
print(stats)
print(len(stats))
print(stats[0].text)
# descrip = s.find_all('div', class_='C_9eTPtA markdown-rendered-content')
descrip = s.find('div', {'class':'C_9eTPtA markdown-rendered-content'}).findAll('p')
print(len(descrip))
print(descrip)
for i in descrip:
    print(i.text)
# store = s.find('div', class_='store-informations__price')
# print(store.text)
# if store is None:
#     paid = False
# print(paid)
# title, publisher
title = (s.find('span', class_='model-name__label')).text
print(title)

info_df = pd.DataFrame(columns=['Title', 'Publisher', 'Description', 
                                'Paid', 'Downloads', 'Views', 'Likes', 'Price'])
print(info_df)
info = []
info.append(title,stats[0].text)
print(info)
info_df = pd.DataFrame(columns=['Title', 'Publisher', 'Description', 
                                'Paid', 'Downloads', 'Views', 'Likes', 'Price', 'Link'])
info_df['Title']


# div.stats
# div.store-informations__header