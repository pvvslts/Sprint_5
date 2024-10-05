import random

class MyInfo:
    user_name = 'Павел Павел'
    login = 'pvvasile_13_998@ya.ru'
    password = 'password998'

class Generate:
    user_name = 'Testof test'
    login = f"Test_of_test{random.randint(100, 999)}@ya.ru"
    password = f"{random.randint(100, 999)}{random.randint(100, 999)}"
