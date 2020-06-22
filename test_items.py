from selenium import webdriver
import pytest
import time


browser = webdriver.Chrome()

@pytest.mark.xfail
@pytest.mark.parametrize()
def test_languages():
    browser.get('http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/')
    button = browser.find_element_by_css_selector('btn.btn-lg.btn-primary.btn-add-to-basket')
    button.click()
    browser.implicitly_wait(1)
    message = browser.find_element_by_class_name("alertinner")

    assert "был добавлен в вашу корзину." in message.text
