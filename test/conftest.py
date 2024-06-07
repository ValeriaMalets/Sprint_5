import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def chrome_driver_path():
    # Устанавливаем ChromeDriver один раз за сессию
    path = ChromeDriverManager().install()
    return path


@pytest.fixture(scope="function")
def browser(chrome_driver_path):

    # Настройка ChromeDriver
    service = ChromeService(executable_path=chrome_driver_path)
    options = webdriver.ChromeOptions()

    # Создание экземпляра браузера
    driver = webdriver.Chrome(service=service, options=options)

    # Ожидание до завершения теста
    yield driver

    # Закрытие браузера после завершения теста
    driver.quit()
