from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import WEB_LINK
from pages.stellar_burgers_page import button_account, input_email, input_password, button_login, link_profile, \
    button_exit
from test.data import EMAIL, PASSWORD


class TestStellarBurgersGoToMyAccount:

    def test_from_main_page_go_to_my_account(self, browser):
        browser.get(WEB_LINK)
        browser.find_element(By.XPATH, button_account).click()
        browser.find_element(By.XPATH, input_email).send_keys(EMAIL)
        browser.find_element(By.XPATH, input_password).send_keys(PASSWORD)
        browser.find_element(By.XPATH, button_login).click()
        browser.find_element(By.XPATH, button_account).click()
        WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, button_exit)))
        assert browser.find_element(By.XPATH, link_profile).is_displayed()