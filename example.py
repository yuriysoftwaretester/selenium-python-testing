import pytest
from selenium.webdriver.common.by import By


@pytest.mark.smoketest
def test_google(browser):
    browser.get("https://www.google.com")
    browser.find_element(By.ID, "something")