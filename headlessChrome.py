from selenium import webdriver
import os
from bs4 import BeautifulSoup

'''
On Heroku, open your App. Click on the Settings tab and scroll down to Buildpacks. Add the following:

Python (Select it from the officially supported buildpacks)
Headless Google Chrome: https://github.com/heroku/heroku-buildpack-google-chrome
Chromedriver: https://github.com/heroku/heroku-buildpack-chromedriver
'''

'''
CHROMEDRIVER_PATH = /app/.chromedriver/bin/chromedriver
GOOGLE_CHROME_BIN = /app/.apt/usr/bin/google-chrome
'''

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location=os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")


driver=webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://www.amazon.in/dp/B07DJCVTDN/ref=cm_sw_r_other_apa_i_tMlzEbF8NA78X')
soup = BeautifulSoup(driver.page_source, "html.parser")
title = None
price = None
try:
    title = soup.find(id="productTitle").get_text()
    print(title.strip())
    price = None
    price = soup.find(id="priceblock_dealprice").get_text()
    print(price)
except Exception as e:
    pass

try:
    title = soup.find(id="productTitle").get_text()
    print(title.strip())
    price = None
    price = soup.find(id="priceblock_ourprice").get_text()
    print(price)
except Exception as e:
    pass


driver.quit()
