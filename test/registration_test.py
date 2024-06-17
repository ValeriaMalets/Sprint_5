from selenium.webdriver.common.by import By
from config import WEB_LINK
from test.data import NAME
from helpers import generate_unique_email, generate_valid_password, generate_invalid_password
from pages.stellar_burgers_page import link_registration, button_login_to_account, input_email, input_password, \
    button_register, input_name, input_error


class TestStellarBurgersRegistration:
    def test_registration_with_success(self, browser):
        unique_email = generate_unique_email()
        valid_password = generate_valid_password()
        browser.get(WEB_LINK)
        browser.find_element(By.XPATH, button_login_to_account).click()
        browser.find_element(By.XPATH, link_registration).click()
        browser.find_element(By.XPATH, input_name).send_keys(NAME)
        browser.find_element(By.XPATH, input_email).send_keys(unique_email)
        browser.find_element(By.XPATH, input_password).send_keys(valid_password)
        browser.find_element(By.XPATH, button_register).click()
        assert browser.find_element(By.XPATH, input_password).is_displayed()

    def test_registration_with_invalid_type_password_5_symbols(self, browser):
        unique_email = generate_unique_email()
        invalid_password = generate_invalid_password()
        browser.get(WEB_LINK)
        browser.find_element(By.XPATH, button_login_to_account).click()
        browser.find_element(By.XPATH, link_registration).click()
        browser.find_element(By.XPATH, input_name).send_keys(NAME)
        browser.find_element(By.XPATH, input_email).send_keys(unique_email)
        browser.find_element(By.XPATH, input_password).send_keys(invalid_password)
        browser.find_element(By.XPATH, button_register).click()
        assert browser.find_element(By.XPATH, input_error).is_displayed()
