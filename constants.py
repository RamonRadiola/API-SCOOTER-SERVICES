class Constants:

    URL = 'https://qa-scooter.praktikum-services.ru/'
    URL_COURIER = URL + '/api/v1/courier'
    URL_LOGIN = URL_COURIER + '/login'
    URL_CREATE_ORDERS = URL + '/api/v1/orders'
    URL_COURIER_DEL = URL_COURIER + '/:id'

    ORDER_DATA = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha"
    }

    COLOR_PARAMETERS = [
        {"color": ["BLACK"]},
        {"color": ["GREY"]},
        {"color": ["BLACK", "GREY"]},
        {}
    ]

    ORDERS_LIST_PARAMS = {
        "nearestStation": '["1"]',
        "limit": 10,
        "page": 0
    }

    LOGIN_DATA = {"login": "ninjazq",
                "password": "1234zq",
                "firstName": "saskezq"}