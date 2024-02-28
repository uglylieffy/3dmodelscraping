from selenium import webdriver
import time

browser=webdriver.Chrome()
browser.get("https://pythonbasics.org/selenium-scroll-down/")
# browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# time.sleep(3)
browser.close()

a = None
if not a:
    print('YEa')