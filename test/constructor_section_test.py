from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import WEB_LINK
from pages.stellar_burgers_page import button_constructor, tab_buns, tab_sauces, tab_fillings, tab_buns_selected, \
    tab_sauces_selected, tab_fillings_selected


class TestConstructorSection:

    def test_transition_to_buns_in_constructor(self, browser):
        browser.get(WEB_LINK)
        browser.find_element(By.XPATH, button_constructor).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, tab_sauces))).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, tab_buns))).click()
        assert browser.find_element(By.XPATH, tab_buns_selected).is_displayed()

    def test_transition_to_sauces_in_constructor(self, browser):
        browser.get(WEB_LINK)
        browser.find_element(By.XPATH, button_constructor).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, tab_sauces))).click()
        assert browser.find_element(By.XPATH,tab_sauces_selected).is_displayed()

    def test_transition_to_fillings_in_constructor(self, browser):
        browser.get(WEB_LINK)
        browser.find_element(By.XPATH, button_constructor).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, tab_fillings))).click()
        assert browser.find_element(By.XPATH, tab_fillings_selected).is_displayed()

