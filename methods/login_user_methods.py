import requests

from data import BASE_URL, REG_USER_URL, generate_payload, LOGIN


def create_user(payload):
    requests.post(f'{BASE_URL}/{REG_USER_URL}', data=payload)

class LoginUserMethods:
    @staticmethod
    def login_user(payload):
        return requests.post(f'{BASE_URL}/{LOGIN}',
                             data={'email': payload.get('email'), 'password': payload.get('password')})

    @staticmethod
    def login_user_with_wrong_email_and_password():
        return requests.post(f'{BASE_URL}/{LOGIN}',
                             data={'email': 'email', 'password': 'password'})
