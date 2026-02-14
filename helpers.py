import random
import string

import allure


@allure.story("Генерирует данные для регистрации нового курьера")
class GenDataCourier:
    @allure.title("Генерирует данные для регистрации нового курьера и возвращает их в словарь payload")
    def generate_data_for_register_new_courier():
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        return payload