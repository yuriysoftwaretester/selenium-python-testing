import pytest
from selenium.webdriver.common.by import By


@pytest.mark.
def test_google(browser):
    browser.get("https://www.google.com")
