from data import generate_payload
from methods.creating_user_methods import NewUserMethods


class TestCreatingUser:
    def test_creating_user(self):
        new_user = NewUserMethods.create_user(generate_payload())
        assert new_user.status_code == 200 and new_user.json()['success'] == True

    def test_creating_the_same_user(self):
        the_same_user = NewUserMethods.create_the_same_user(generate_payload())
        assert the_same_user.status_code == 403 and the_same_user.json()['message'] == 'User already exists'

    def test_creating_user_without_name(self):
        user_without_name = NewUserMethods.create_user_without_name(generate_payload())
        assert user_without_name.status_code == 403 and user_without_name.json()[
            'message'] == 'Email, password and name are required fields'

    def test_creating_user_without_email(self):
        user_without_email = NewUserMethods.create_user_without_email(generate_payload())
        assert user_without_email.status_code == 403 and user_without_email.json()[
            'message'] == 'Email, password and name are required fields'

    def test_creating_user_without_password(self):
        user_without_password = NewUserMethods.create_user_without_password(generate_payload())
        assert user_without_password.status_code == 403 and user_without_password.json()[
            'message'] == 'Email, password and name are required fields'
