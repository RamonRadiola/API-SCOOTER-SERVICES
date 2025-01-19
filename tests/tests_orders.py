import pytest
from constants import Constants
import allure


@allure.story("Проверяет ручку 'Создать заказ'")
class TestCreateOrders:
    @pytest.mark.parametrize("create_order", Constants.COLOR_PARAMETERS, indirect=True)
    @allure.title("Проверка возможности указания цвета при создании заказа")
    def test_create_order_with_colors(self, create_order):
        response = create_order
        assert response.status_code == 201

    @allure.title("Проверяется, что тело ответа содержит 'track'")
    def test_track_in_response(self, create_order):
        response = create_order
        assert 'track' in response.json()