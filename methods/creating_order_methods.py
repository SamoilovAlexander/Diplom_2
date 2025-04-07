import requests

from data import BASE_URL, ORDER_URL


class CreatingOrder:
    @staticmethod
    def creating_order_with_login(token, order):
        return requests.post(f'{BASE_URL}/{ORDER_URL}', headers={'Authorization': token}, data=order)

    @staticmethod
    def creating_order_without_login(order):
        return requests.post(f'{BASE_URL}/{ORDER_URL}', data=order)