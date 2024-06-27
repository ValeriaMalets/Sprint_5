import string
import random
from selenium.webdriver.common.by import By
from pages.stellar_burgers_page import input_email, input_password, button_login
from test.data import EMAIL, PASSWORD


def generate_unique_email():
    random_digits = random.randint(100, 999)
    return f"valeria.malets9_{random_digits}@ya.ru"


def generate_valid_password():
    return "".join(random.choices(string.ascii_letters + string.digits, k=6))


def generate_invalid_password():
    return "".join(random.choices(string.ascii_letters + string.digits, k=5))

def enter_email_password_click_login(browser):
    browser.find_element(By.XPATH, input_email).send_keys(EMAIL)
    browser.find_element(By.XPATH, input_password).send_keys(PASSWORD)
    browser.find_element(By.XPATH, button_login).click()
