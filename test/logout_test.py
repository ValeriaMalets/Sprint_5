from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import WEB_LINK
from pages.stellar_burgers_page import button_account, input_email, input_password, button_login, button_exit

EMAIL = 'valeriamalets9111@gmail.com'
PASSWORD = 'Sprint5'


class TestStellarBurgersLogout:

    def test_logout_from_my_account_by_button(self, browser):
        browser.get(WEB_LINK)
        browser.find_element(By.XPATH, button_account).click()
        browser.find_element(By.XPATH, input_email).send_keys(EMAIL)
        browser.find_element(By.XPATH, input_password).send_keys(PASSWORD)
        browser.find_element(By.XPATH, button_login).click()
        browser.find_element(By.XPATH, button_account).click()
        WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, button_exit))).click()
        WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, button_login)))
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/login'

