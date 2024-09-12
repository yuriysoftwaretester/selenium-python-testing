import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.mark.smoketest
def test_alhym_records_navigation(browser):

    browser.get("https://alhymrecords.com/")

    # browser.find_element(By.ID, "menu-item-1397").click()
    # browser.find_element(By.CLASS_NAME, "menu-item-1397").click()
    # browser.find_element(By.LINK_TEXT, "ARTISTS").click()
    # browser.find_element(By.XPATH, "//li[@id='menu-item-1397']").click()
    browser.find_element(By.CSS_SELECTOR, 'li#menu-item-1397').click()
    browser.find_element(By.CSS_SELECTOR, 'a[id="slider-1-slide-1-layer-14"]').click()
    # browser.find_element(By.XPATH, '//li[@class="vl-flyout-nav__js-tab"][@data-currenttabindex="8"]').click()
    # browser.find_element(By.CSS_SELECTOR, 'input[value="Search"]')
    # browser.find_element(By.XPATH,        '//input[@value="Search"]')




