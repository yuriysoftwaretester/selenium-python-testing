import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager

service = ChromeService(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)
browser.maximize_window()
browser.get("https://www.ebay.com/")
WebDriverWait(browser, 10).until(EC.title_is("Electronics, Cars, Fashion, Collectibles & More | eBay"))
assert 'Electronics, Cars, Fashion, Collectibles & More | eBay' == browser.title
browser.find_element(By.NAME, '_nkw').send_keys("Lexus")
element = WebDriverWait(browser,15).until(EC.presence_of_element_located((By.XPATH, '//a[@aria-label="lexus rx350 in Auto Parts & Accessories"]')))
browser.find_element(By.NAME, '_nkw').click()
element.click()
WebDriverWait(browser, 10).until(EC.title_is(""))
time.sleep(5)






