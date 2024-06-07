from selenium.webdriver.common.by import By
import time

from pages.stellar_burgers_page import link_registration, button_login_to_account, input_email, input_password, \
    button_register, input_name, input_error

WEB_LINK = "https://stellarburgers.nomoreparties.site/"
EMAIL = 'valeriamalets9333@gmail.com'
PASSWORD = 'Sprint5'
INVALID_PASSWORD = 'Sprin'
NAME = 'Valeria Malets'


def test_registration_with_success (browser):
    browser.get(WEB_LINK)
    browser.find_element(By.XPATH, button_login_to_account).click()
    browser.find_element(By.XPATH, link_registration).click()
    browser.find_element(By.XPATH, input_name).send_keys(NAME)
    browser.find_element(By.XPATH, input_email).send_keys(EMAIL)
    browser.find_element(By.XPATH, input_password).send_keys(PASSWORD)
    browser.find_element(By.XPATH, button_register).click()
    time.sleep(2)
    assert browser.find_element(By.XPATH, input_password).is_displayed()


def test_registration_with_invalid_type_password_4_symbols (browser):
    browser.get(WEB_LINK)
    browser.find_element(By.XPATH, button_login_to_account).click()
    browser.find_element(By.XPATH, link_registration).click()
    browser.find_element(By.XPATH, input_password).send_keys(INVALID_PASSWORD)
    browser.find_element(By.XPATH, button_register).click()
    time.sleep(2)
    assert browser.find_element(By.XPATH, input_error).is_displayed()



