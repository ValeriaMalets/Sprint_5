from selenium.webdriver.common.by import By
from pages.stellar_burgers_page import button_login_to_account, input_email, input_password, button_login, button_order, \
    button_account, link_login, button_reset_password, link_registration
import time

EMAIL = 'valeriamalets9111@gmail.com'
PASSWORD = 'Sprint5'
WEB_LINK = "https://stellarburgers.nomoreparties.site/"

def enter_email_password_click_login(browser):
    browser.find_element(By.XPATH, input_email).send_keys(EMAIL)
    browser.find_element(By.XPATH, input_password).send_keys(PASSWORD)
    browser.find_element(By.XPATH, button_login).click()

def test_login_from_main_page_by_login_to_account_button(browser):
    browser.get(WEB_LINK)
    browser.find_element(By.XPATH, button_login_to_account).click()
    enter_email_password_click_login(browser)
    time.sleep(2)
    assert browser.find_element(By.XPATH, button_order).is_displayed()


def test_login_from_main_page_by_account_button(browser):
    browser.get(WEB_LINK)
    browser.find_element(By.XPATH, button_account).click()
    enter_email_password_click_login(browser)
    time.sleep(2)
    assert browser.find_element(By.XPATH, button_order).is_displayed()


def test_login_from_registration_page_by_login_link(browser):
    browser.get(WEB_LINK)
    browser.find_element(By.XPATH, button_account).click()
    browser.find_element(By.XPATH, link_registration).click()
    browser.find_element(By.XPATH, link_login).click()
    enter_email_password_click_login(browser)
    time.sleep(2)
    assert browser.find_element(By.XPATH, button_order).is_displayed()


def test_login_from_reset_password_page_by_login_link(browser):
    browser.get(WEB_LINK)
    browser.find_element(By.XPATH, button_login_to_account).click()
    browser.find_element(By.XPATH, button_reset_password).click()
    browser.find_element(By.XPATH, link_login).click()
    enter_email_password_click_login(browser)
    time.sleep(2)
    assert browser.find_element(By.XPATH, button_order).is_displayed()










