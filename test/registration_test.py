import string
import random
from selenium.webdriver.common.by import By
from config import WEB_LINK
from pages.stellar_burgers_page import link_registration, button_login_to_account, input_email, input_password, \
    button_register, input_name, input_error

NAME = 'Valeria Malets'


class TestStellarBurgersRegistration:
    def generate_unique_email(self):
        random_digits = random.randint(100, 999)
        return f"valeria.malets9_{random_digits}@ya.ru"

    def generate_valid_password(self):
        return "".join(random.choices(string.ascii_letters + string.digits, k=6))

    def generate_invalid_password(self):
        return "".join(random.choices(string.ascii_letters + string.digits, k=5))

    def test_registration_with_success(self, browser):
        unique_email = self.generate_unique_email()
        valid_password = self.generate_valid_password()
        browser.get(WEB_LINK)
        browser.find_element(By.XPATH, button_login_to_account).click()
        browser.find_element(By.XPATH, link_registration).click()
        browser.find_element(By.XPATH, input_name).send_keys(NAME)
        browser.find_element(By.XPATH, input_email).send_keys(unique_email)
        browser.find_element(By.XPATH, input_password).send_keys(valid_password)
        browser.find_element(By.XPATH, button_register).click()
        assert browser.find_element(By.XPATH, input_password).is_displayed()

    def test_registration_with_invalid_type_password_4_symbols(self, browser):
        unique_email = self.generate_unique_email()
        invalid_password = self.generate_invalid_password()
        browser.get(WEB_LINK)
        browser.find_element(By.XPATH, button_login_to_account).click()
        browser.find_element(By.XPATH, link_registration).click()
        browser.find_element(By.XPATH, input_name).send_keys(NAME)
        browser.find_element(By.XPATH, input_email).send_keys(unique_email)
        browser.find_element(By.XPATH, input_password).send_keys(invalid_password)
        browser.find_element(By.XPATH, button_register).click()
        assert browser.find_element(By.XPATH, input_error).is_displayed()



