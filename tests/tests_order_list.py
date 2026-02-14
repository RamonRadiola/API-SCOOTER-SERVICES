import requests
from constants import Constants
import allure

@allure.story("Проверяет ручку 'Получение списка заказов'")
class TestOrderList:
    @allure.title("Проверка, что в тело ответа возвращается список заказов")
    def test_get_orders_with_nearest_station(self):
        response = requests.get(Constants.URL_CREATE_ORDERS, params=Constants.ORDERS_LIST_PARAMS)
        response_json = response.json()
        orders = response_json["orders"]
        assert isinstance(orders, list)