import pytest
from helpers import GenDataCourier
import requests
from constants import Constants


@pytest.fixture
def reg_courier(request):
    data = GenDataCourier.generate_data_for_register_new_courier()
    response = requests.post(Constants.URL_COURIER, data=data)
    if hasattr(request, "param") and request.param:
        yield response, data
    else:
        yield response
    login_data = {"login": data["login"], "password": data["password"]}
    login_response = requests.post(Constants.URL_LOGIN, data=login_data)
    courier_id = login_response.json().get("id")
    if courier_id:
        requests.delete(f"{Constants.URL_COURIER_DEL.replace(':id', str(courier_id))}")


@pytest.fixture
def create_order(request):
    order_data = Constants.ORDER_DATA.copy()
    if hasattr(request, "param") and request.param:
        order_data.update(request.param)
    response = requests.post(Constants.URL_CREATE_ORDERS, json=order_data)
    yield response
    track = response.json().get("track")
    if track:
        requests.put(f"{Constants.URL_CREATE_ORDERS}/cancel", json={"track": track})