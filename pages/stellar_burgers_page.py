from selenium.webdriver.common.by import By

# Registration Form
input_name = '//label[contains(text(), "Имя")]/following-sibling::input'
input_email = '//label[contains(text(), "Email")]/following-sibling::input'
input_password = '//label[contains(text(), "Пароль")]/following-sibling::input'
input_error = '//p[contains(text(), "Некорректный пароль")]'
button_register = '//button[contains(text(), "Зарегистрироваться")]'
link_login = '//a[contains(text(), "Войти")]'

# Login
button_account = '//p[contains(text(), "Личный Кабинет")]'
button_login_to_account = '//button[contains(text(), "Войти в аккаунт")]'
button_reset_password = '//a[contains(text(), "Восстановить пароль")]'
button_login = '//button[contains(text(), "Войти")]'
link_registration = '//a[contains(text(), "Зарегистрироваться")]'

# Constructor

tab_buns = '//span[contains(text(), "Булки")]'
tab_sauces = '//span[contains(text(), "Соусы")]'
tab_fillings = '//span[contains(text(), "Начинки")]'
tab_buns_selected = '//div[contains(@class, "tab_tab__1SPyG") and .//span[text()="Булки"]]'
tab_sauces_selected = '//div[contains(@class, "tab_tab__1SPyG") and .//span[text()="Соусы"]]'
tab_fillings_selected = ('//div[contains(@class, "tab_tab__1SPyG") and contains(@class, "tab_tab_type_current__2BEPc") '
                         'and .//span[text()="Начинки"]]')


button_constructor = '//p[contains(text(), "Конструктор")]'
button_order = '//button[contains(text(), "Оформить заказ")]'


# MyAccount
button_exit = '//button[contains(text(), "Выход")]'
link_profile = '//a[contains(text(), "Профиль")]'
