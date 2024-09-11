import pytest

@pytest.mark.regressiontest
def test_new(browser):
    browser.get('https://www.ebay.com')