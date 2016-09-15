import time
from splinter import Browser 
import pytest

@pytest.yield_fixture
def browser(request):
    with Browser("chrome") as browser:
        yield browser



def test_pyconapac_seo_and_homepage(browser):
    browser.visit("http://www.google.com.tw")
    time.sleep(5)
    browser.fill("q", "pyconapac 2015\n")
    time.sleep(5)
    browser.click_link_by_href("https://tw.pycon.org/")
    assert browser.url == "https://tw.pycon.org/2015apac/zh/"

