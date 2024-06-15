import string
import random


def generate_unique_email():
    random_digits = random.randint(100, 999)
    return f"valeria.malets9_{random_digits}@ya.ru"


def generate_valid_password():
    return "".join(random.choices(string.ascii_letters + string.digits, k=6))


def generate_invalid_password():
    return "".join(random.choices(string.ascii_letters + string.digits, k=5))
