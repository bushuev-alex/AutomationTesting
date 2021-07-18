import time


def test_page_contains_button_add_to_cart(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(4)
    button_add_to_card = browser.find_element_by_css_selector("#add_to_basket_form .btn-add-to-basket")
    time.sleep(4)
    assert button_add_to_card, "button is missing"