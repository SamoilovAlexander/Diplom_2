from data import generate_payload
from methods.change_user_data_methods import ChangeUserData


class TestChangeUserData:
    def test_change_user_email_with_login(self, auth_user):
        random_email = generate_payload()['email']
        change_email = ChangeUserData.change_user_email_with_login(auth_user.json()['accessToken'], random_email)
        assert change_email.status_code == 200 and change_email.json()['user']['email'] == random_email

    def test_change_user_email_without_login(self):
        random_email = generate_payload()['email']
        change_email = ChangeUserData.change_user_email_without_login(random_email)
        assert change_email.status_code == 401 and change_email.json()['message'] == 'You should be authorised'