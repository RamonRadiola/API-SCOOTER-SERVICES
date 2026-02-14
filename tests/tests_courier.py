from constants import Constants
from helpers import GenDataCourier
import requests
import pytest
import allure

@allure.story("Проверяет ручку 'Создать курьера'")
class TestCreateCourier:
    @allure.title("Проверка возможности создания курьера")
    def test_create_courier(self, reg_courier):
        assert 201 == reg_courier.status_code


    @allure.title("Проверка ожидаемого ответа при успешной регистрации курьера")
    def test_create_courier_ok_is_true(self, reg_courier):
        assert "ok" in reg_courier.json()


    @allure.title("Проверка на отсутствие возможности регистрации двух одинаковых курьеров")
    @pytest.mark.parametrize("reg_courier", [True], indirect=True)
    def test_no_create_couriers_with_same_data(self, reg_courier):
        response, data = reg_courier
        response_second = requests.post(Constants.URL_COURIER, data=data)
        assert 409 == response_second.status_code


    @allure.title("Проверка на отсутствие возможности создания курьера без заполнения одного из обязательных полей")
    @pytest.mark.parametrize("field_to_remove, reg_courier", [("login", True), ("password", True)], indirect=["reg_courier"])
    def test_no_create_courier_without_required_fields(self, reg_courier, field_to_remove):
        response, data = reg_courier
        courier_data = data.copy()
        courier_data.pop(field_to_remove, None)
        response = requests.post(Constants.URL_COURIER, json=courier_data)
        assert 400 == response.status_code


    @allure.title("проверка на возвращение ошибки при попытке создания пользователя с логином, который уже используется")
    @pytest.mark.parametrize("reg_courier", [True], indirect=True)
    def test_no_create_courier_with_login_same(self, reg_courier):
        response, data = reg_courier
        payload = GenDataCourier.generate_data_for_register_new_courier()
        payload["login"] = data["login"]
        response_second = requests.post(Constants.URL_COURIER, data=payload)
        error_message = response_second.json().get("message")
        assert 409 == response_second.status_code and error_message == "Этот логин уже используется. Попробуйте другой."