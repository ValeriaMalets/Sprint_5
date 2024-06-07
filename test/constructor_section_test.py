from selenium.webdriver.common.by import By
import time
from pages.stellar_burgers_page import button_constructor, tab_buns, tab_sauces, tab_fillings, cr_bun, spicy_sauce, \
    bun_mini

WEB_LINK = "https://stellarburgers.nomoreparties.site/"


def test_transition_to_buns_in_constructor(browser):
    browser.get(WEB_LINK)
    browser.find_element(By.XPATH, button_constructor).click()
    browser.find_element(By.XPATH, tab_sauces).click()
    time.sleep(2)
    browser.find_element(By.XPATH, tab_buns).click()
    time.sleep(2)
    assert browser.find_element(By.XPATH, cr_bun).is_displayed()


def test_transition_to_sauces_in_constructor(browser):
    browser.get(WEB_LINK)
    browser.find_element(By.XPATH, button_constructor).click()
    browser.find_element(By.XPATH, tab_sauces).click()
    time.sleep(2)
    assert browser.find_element(By.XPATH, spicy_sauce).is_displayed()


def test_transition_to_fillings_in_constructor(browser):
    browser.get(WEB_LINK)
    browser.find_element(By.XPATH, button_constructor).click()
    browser.find_element(By.XPATH, tab_fillings).click()
    time.sleep(2)
    assert browser.find_element(By.XPATH, bun_mini).is_displayed()
