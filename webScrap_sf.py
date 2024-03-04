# init library import
import requests
from bs4 import BeautifulSoup
import pandas as pd

# load in the websites
sketchfabList_df = pd.read_csv('./sketchfab_url.csv')


# create an empty dataframe to store details about models
info_df = pd.DataFrame(columns=['Title', 'Publisher', 'Description', 
                                'Paid', 'Downloads', 'Views', 'Likes', 'Price', 'Date', 'Link', 'imgLink'])
info = []
n = 0


# loop thru the websites
for index, row in sketchfabList_df.iterrows():
    # set paid to be True (default) 
    paid = True

    # assign link and imglink 
    link = row['Sketchfab_URL']
    imgLink = row['SketchfabImg_URL']
    print(link)

    # web scraping 
    html = requests.get(link)
    soup = BeautifulSoup(html.content, 'html.parser')

    # title, publisher
    title = (soup.find('span', class_='model-name__label')).text
    publisher = (soup.find('span', class_='username-wrapper')).text

    # published date 
    date_parent = (soup.find('span', class_='model-meta-info help'))
    date = date_parent.find('div', class_='tooltip tooltip-down').text

    # description of the model
    descrip_list = []
    temp_descrip = soup.find('div', {'class':'C_9eTPtA markdown-rendered-content'})
    # if description is not provided
    if not temp_descrip:
        pass
    else:
        descrip = soup.find('div', {'class':'C_9eTPtA markdown-rendered-content'}).findAll('p')
        for i in descrip:
            descrip_list.append(i.text)

    # is paid model or not 
    store = soup.find('div', class_='store-informations__price')
    if not store:
        paid = False

    # stats of the model as following order.
    # free models: downloads (abbr.), downloads, views (abbr.), views, likes
    # paid models: views (abbr.), views, likes
    stats = soup.find_all('span', class_='count')
    
    if paid:
        # stats 
        downloads = 'n/a'
        views = stats[1].text
        likes = stats[2].text
        # price 
        price = store.text

    else:
        # stats 
        downloads = stats[1].text
        views = stats[3].text
        likes = stats[4].text
        # price 
        price = 'n/a'


    # append data into dataframe 
    info.append(title)
    info.append(publisher)
    info.append(descrip_list)
    info.append(paid)
    info.append(downloads)
    info.append(views)
    info.append(likes)
    info.append(price)
    info.append(date)
    info.append(link)
    info.append(imgLink)


    # load data into dataframe 
    info_df.loc[n] = info
    n+=1
    info.clear()

info_df.to_csv('web_scrap_sf.csv', index=False)
