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
url = 'https://www.turbosquid.com/Search/3D-Models/dinosaur+skeleton?page_size=500'


# load page and scroll for a bit
driver.get(url)
time.sleep(5)
# scrolling 
iframe = driver.find_element(By.XPATH, '//*[@id="footer"]/div[1]/div')
ActionChains(driver)\
          .scroll_to_element(iframe)\
          .perform()
time.sleep(3)

# Now, parse over the pre-loaded page 
# find links of the detailed webpages 
turbosquidList = []
links = driver.find_elements(By.CLASS_NAME, 'mouseover_fplink')
# loop thru all loaded ietms on the page 
for link in links:
    turbosquidList.append(link.get_attribute("href"))


# find links to corresponding images 
turbosquidImgList = []
imgs = driver.find_elements(By.CSS_SELECTOR, '.thumbnail.thumbnail-md')
# loop thru all loaded image linkd 
for link in imgs:
    turbosquidImgList.append(link.get_attribute("data-thumbnail"))
print(len(turbosquidList), len(turbosquidImgList))
# input('Press any key...')


# turn turbosquidList & turbosquidImgList into csv file 
turbosquidList_df = pd.DataFrame({'TurboSquid_URL':turbosquidList, 'TurboSquidImg_URL':turbosquidImgList})
# Drop any duplicates due to webpage's nature 
turbosquidList_df = turbosquidList_df.drop_duplicates()
turbosquidList_df.to_csv('turbosquid_url.csv', index=False)