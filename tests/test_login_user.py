from data import generate_payload
from methods.login_user_methods import LoginUserMethods


class TestLoginUser:
    def test_login_user(self, user):
        login_user = LoginUserMethods.login_user(user)
        assert login_user.json()['success'] == True and login_user.json()['accessToken'] is not None

    def test_login_user_with_wrong_email_and_password(self):
        login_user = LoginUserMethods.login_user_with_wrong_email_and_password()
        assert login_user.status_code == 401 and login_user.json()['message'] == 'email or password are incorrect'