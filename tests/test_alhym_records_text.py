import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.mark.regressiontest
def test_alhym_records_text(browser):
    browser.get("https://alhymrecords.com/")
    time.sleep(5)
    browser.find_element(By.LINK_TEXT, "CONTACT").click()
    time.sleep(5)
    send_button = browser.find_element(By.XPATH, "//input[@value='Send']")
    # print(send_button.text)
    print(send_button.get_attribute("value"))
    assert 'Send' == send_button.get_attribute("value")
    time.sleep(5)



