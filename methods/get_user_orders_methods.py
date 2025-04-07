import requests

from data import BASE_URL, ORDER_URL


class GetUserOrders:
    @staticmethod
    def get_user_orders_with_login(token):
        return requests.get(f'{BASE_URL}/{ORDER_URL}', headers={'Authorization': token})

    @staticmethod
    def get_user_orders_without_login():
        return requests.get(f'{BASE_URL}/{ORDER_URL}')