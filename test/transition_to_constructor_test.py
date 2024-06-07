from selenium.webdriver.common.by import By
import time

from pages.stellar_burgers_page import button_account, input_email, input_password, button_login, button_constructor, \
    tab_buns

EMAIL = 'valeriamalets9111@gmail.com'
PASSWORD = 'Sprint5'
WEB_LINK = "https://stellarburgers.nomoreparties.site/"


def test_transition_from_my_account_to_constructor(browser):
    browser.get(WEB_LINK)
    browser.find_element(By.XPATH, button_account).click()
    browser.find_element(By.XPATH, input_email).send_keys(EMAIL)
    browser.find_element(By.XPATH, input_password).send_keys(PASSWORD)
    browser.find_element(By.XPATH, button_login).click()
    browser.find_element(By.XPATH, button_account).click()
    browser.find_element(By.XPATH, button_constructor).click()
    time.sleep(2)
    assert browser.find_element(By.XPATH, tab_buns).is_displayed()

