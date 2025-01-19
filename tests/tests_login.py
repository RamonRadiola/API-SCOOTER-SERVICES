from constants import Constants
import requests
import pytest
import allure

@allure.story("Проверяет ручку 'Логин курьера'")
class TestLogin:
    @allure.title("Проверка авторизации курьера с параметрами, переданными после регистрации")
    @pytest.mark.parametrize("reg_courier", [True], indirect=True)
    def test_just_login(self, reg_courier):
        response, data = reg_courier
        response_login = requests.post(Constants.URL_LOGIN, data=data)
        assert 200 == response_login.status_code

    @allure.title("Проверка на авторизацию только с обязательными параметрами(login, password)")
    @pytest.mark.parametrize("reg_courier", [True], indirect=True)
    def test_login_with_required_fields(self, reg_courier):
        response, data = reg_courier
        data.pop("firstName", None)
        response_login = requests.post(Constants.URL_LOGIN, data=data)
        assert 200 == response_login.status_code

    @allure.title("проверка на отсутствие возможности авторизации с одним неправильным обязательным параметром")
    @pytest.mark.parametrize("key_to_modify, reg_courier", [
        ("login", True),
        ("password", True)
    ], indirect=["reg_courier"])
    def test_no_login_with_unright_param(self, reg_courier, key_to_modify):
        response, data = reg_courier
        modified_data = data.copy()
        modified_data[key_to_modify] += 'a'
        response_login = requests.post(Constants.URL_LOGIN, data=modified_data)
        assert 404 == response_login.status_code

    @allure.title("проверка на отсутствие возможности авторизации без одного поля")
    @pytest.mark.parametrize("reg_courier", [True], indirect=True)
    def test_no_login_without_login(self, reg_courier):
        response, data = reg_courier
        modified_data = data.copy()
        modified_data.pop("login", None)
        modified_data.pop("firstName", None)
        response_login = requests.post(Constants.URL_LOGIN, json=modified_data)
        assert 400 == response_login.status_code

    @allure.title("проверка на отсутствие возможности авторизации несуществующего пользователя")
    def test_no_login_with_unreal_courier(self):
        response_login = requests.post(Constants.URL_LOGIN, json=Constants.LOGIN_DATA)
        assert 404 == response_login.status_code

    @allure.title("проверяется, что успешный запрос возвращает id")
    @pytest.mark.parametrize("reg_courier", [True], indirect=True)
    def test_login_return_id(self, reg_courier):
        response, data = reg_courier
        response_login = requests.post(Constants.URL_LOGIN, data=data)
        response_body = response_login.json()
        assert "id" in response_body