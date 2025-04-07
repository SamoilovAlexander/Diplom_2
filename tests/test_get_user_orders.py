from data import generate_order_data
from methods.creating_order_methods import CreatingOrder
from methods.get_user_orders_methods import GetUserOrders


class TestUserOrders:

    def test_get_user_orders_with_login(self, auth_user):
        CreatingOrder.creating_order_with_login(auth_user.json()['accessToken'], generate_order_data())
        response = GetUserOrders.get_user_orders_with_login(auth_user.json()['accessToken'])
        assert (response.status_code == 200
                and response.json()['success'] == True
                and response.json()['orders'] is not None)


    def test_get_user_orders_without_login(self):
        response = GetUserOrders.get_user_orders_without_login()
        assert (response.status_code == 401
                and response.json()['success'] == False
                and response.json()['message'] == "You should be authorised")

