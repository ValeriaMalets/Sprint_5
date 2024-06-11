from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import WEB_LINK
from pages.stellar_burgers_page import button_constructor, tab_buns, tab_sauces, tab_fillings, cr_bun, spicy_sauce, \
    bun_mini, cr_bun_modal_window, spicy_sauce_modal_window, bun_mini_modal_window


class TestConstructorSection:

    def test_transition_to_buns_in_constructor(self, browser):
        browser.get(WEB_LINK)
        browser.find_element(By.XPATH, button_constructor).click()
        WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, tab_sauces))).click()
        WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, tab_buns))).click()
        WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, cr_bun))).click()
        assert browser.find_element(By.XPATH, cr_bun_modal_window).is_displayed()

    def test_transition_to_sauces_in_constructor(self, browser):
        browser.get(WEB_LINK)
        browser.find_element(By.XPATH, button_constructor).click()
        browser.find_element(By.XPATH, tab_sauces).click()
        WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, spicy_sauce))).click()
        assert browser.find_element(By.XPATH, spicy_sauce_modal_window).is_displayed()

    def test_transition_to_fillings_in_constructor(self, browser):
        browser.get(WEB_LINK)
        browser.find_element(By.XPATH, button_constructor).click()
        browser.find_element(By.XPATH, tab_fillings).click()
        WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, bun_mini))).click()
        assert browser.find_element(By.XPATH, bun_mini_modal_window).is_displayed()
