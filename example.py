import pytest

@pytest.mark.smoketest
def test_google(browser):
    browser.get("https://www.google.com")