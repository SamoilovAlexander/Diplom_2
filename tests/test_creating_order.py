from methods.creating_order_methods import CreatingOrder
from data import generate_order_data, generate_order_data_wrong_ingredients


class TestCreatingOrder:
    def test_creating_order_with_login(self, auth_user):
        order = CreatingOrder.creating_order_with_login(auth_user.json()['accessToken'], generate_order_data())
        assert order.status_code == 200 and order.json()['success'] == True

    def test_creating_order_without_login(self):
        order = CreatingOrder.creating_order_without_login(generate_order_data())
        assert order.status_code == 403 #В служебной документации по API не описано поведение системы при попытке
        # сделать заказ без регистрации. Я предположил, что верным ответом сервера должно быть 403

    def test_creating_order_with_login_without_ingredients(self, auth_user):
        order = CreatingOrder.creating_order_with_login(auth_user.json()['accessToken'], {"ingredients": []})
        assert order.status_code == 400 and order.json()['success'] == False and order.json()['message'] == 'Ingredient ids must be provided'

    def test_creating_order_with_login_with_wrong_ingredients(self, auth_user):
        order = CreatingOrder.creating_order_with_login(auth_user.json()['accessToken'], generate_order_data_wrong_ingredients())
        assert order.status_code == 500
