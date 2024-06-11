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
button_constructor = '//p[contains(text(), "Конструктор")]'
button_order = '//button[contains(text(), "Оформить заказ")]'
cr_bun = '//p[contains(text(), "Краторная булка N-200i")]'
cr_bun_modal_window = '//img[@src="https://code.s3.yandex.net/react/code/bun-02.png" and @alt="tick animation"]'
spicy_sauce = '//p[contains(text(), "Соус Spicy-X")]'
spicy_sauce_modal_window = '//img[@src="https://code.s3.yandex.net/react/code/sauce-02.png" and @alt="tick animation"]'
bun_mini = '//p[contains(text(), "Мини-салат Экзо-Плантаго")]'
bun_mini_modal_window = '//img[@src="https://code.s3.yandex.net/react/code/salad.png" and @alt="tick animation"]'


# MyAccount
button_exit = '//button[contains(text(), "Выход")]'
link_profile = '//a[contains(text(), "Профиль")]'

