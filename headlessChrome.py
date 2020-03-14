from selenium import webdriver
import os
from bs4 import BeautifulSoup

print("Result   ", os.environ['PATH'])

chrome_options = webdriver.ChromeOptions()
#chrome_options.binary_location=os.environ.get("GOOGLE_CHROME_BIN")
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
