# init library import
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd
import re

# load in the websites
turbosquidList_df = pd.read_csv('./turbosquid_url_4.csv')


# create an empty dataframe to store details about models
info_df = pd.DataFrame(columns=['Title', 'Publisher', 'Description', 
                                'Paid', 'Price', 'Date', 'Link', 'imgLink'])
info = []
n = 0


# loop thru the websites
for index, row in turbosquidList_df.iterrows():
    # set up the chromium driver 
    driver = webdriver.Chrome()


    # set paid to be True (default) 
    paid = True


    # assign link and imglink 
    link = row['TurboSquid_URL']
    imgLink = row['TurboSquidImg_URL']
    print(link)


    # load page and scroll for a bit
    driver.get(link)
    time.sleep(10)


    # title, publisher
    # handle exceptions
    try:
        title = (driver.find_element
                (By.CSS_SELECTOR, 
                '.overflow-hidden.text-ellipsis.whitespace-nowrap.asset-title.format-asset-title')).get_attribute("title")
        info.append(title)
        publisher = (driver.find_element(By.XPATH, '//*[@id="author"]/a')).get_attribute("innerText")
        info.append(publisher)    
        pass
    except NoSuchElementException:
        print("exception handled")
        continue


    # description of the model
    descrip_list = []
    temp_descrip = (driver.find_element(By.CSS_SELECTOR, '.p-5.overflow-hidden.text-\[13px\].break-all.bg-white-100.product-description.leading-5.break-keep.font-light')).get_attribute("innerText")
    temp_descrip = re.split("[\n\xa0]+",  temp_descrip)
    descrip = ' '.join(temp_descrip)
    info.append(descrip)


    # check if model is for a charge or free, and it's price
    price = (driver.find_element(By.CSS_SELECTOR, '.pr-1.text-xl.font-normal')).get_attribute("innerText")
    if price == "Free":
        paid = False
    info.append(paid)
    info.append(price)


    # published date 
    date = (driver.find_element(By.ID, 'FPDatePublished')).get_attribute("innerText")
    info.append(date)


    # append rest of data to dataframe 
    info.append(link)
    info.append(imgLink)


    # load data into dataframe 
    info_df.loc[n] = info
    n+=1
    info.clear()

info_df.to_csv('web_scrap_ts_4.csv', index=False)