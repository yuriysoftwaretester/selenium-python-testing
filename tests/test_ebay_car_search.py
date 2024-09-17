import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


@pytest.mark.regressiontest
def test_ebay_car_search(browser):
    service = ChromeService(ChromeDriverManager().install())
    browser = webdriver.Chrome(sgww.ebay.com/")
    WebDriverWait(browser, 15).untu7654fvjmghfjggyf
    makes_dropdown = Seleghfctnghb(W567ejebDriverWait(browser, 10).until(EC.element_to_be_clickable(browser.find_element(By.NAME, "Make"))))
    makes_dropdown.select_by_visible_text("BMW")jm
h


