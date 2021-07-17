import pytest
import time
from selenium import webdriver


def test_page_contains_button_add_to_cart(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(3)
    button_add_to_card = browser.find_element_by_css_selector("button.btn")
    time.sleep(3)
    assert button_add_to_card, "button is missing"