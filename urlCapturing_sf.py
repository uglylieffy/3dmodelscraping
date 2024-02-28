# init library import
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd

# set up the chromium driver 
driver = webdriver.Chrome()


# insert URL here to collect initial urls to be recorded
url = 'https://sketchfab.com/search?features=downloadable&q=dinosaur+fossil&type=models'

# load and scroll to the bottom of the page
driver.get(url)
print('moving...')
for i in range(1,30):
    print('//*[@id="view10"]/main/aside/div[2]/div/div[2]/div/div[1]/div['+str(i*24)+']')
    # handle exceptions
    try:
        iframe = driver.find_element(By.XPATH, '//*[@id="view10"]/main/aside/div[2]/div/div[2]/div/div[1]/div['+str(i*24)+']')
    except NoSuchElementException:
        print("exception handled")
        break
    ActionChains(driver)\
        .scroll_to_element(iframe)\
        .perform()
    time.sleep(3)


# parse over the pre-loaded page 
sketchfabList = []
links = driver.find_elements(By.CLASS_NAME,'card-model__thumbnail-link')
print(len(links))

# loop thru all loaded ietms on the page 
for link in links:
    sketchfabList.append(link.get_attribute("href"))

# turn sketchfabList into csv file 
sketchfabList_df = pd.DataFrame(sketchfabList, columns=['Sketchfab_URL'])
sketchfabList_df.to_csv('sketchfab_url.csv', index=False)
