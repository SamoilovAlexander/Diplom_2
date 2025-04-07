import requests

from data import BASE_URL, REG_USER_URL, generate_payload, USER_URL


class NewUserMethods:
    @staticmethod
    def create_user(payload):
        return requests.post(f'{BASE_URL}/{REG_USER_URL}', data=payload)

    @staticmethod
    def create_the_same_user(payload):
        requests.post(f'{BASE_URL}/{REG_USER_URL}', data=payload)
        return requests.post(f'{BASE_URL}/{REG_USER_URL}', data=payload)

    @staticmethod
    def create_user_without_name(payload):
        return requests.post(f'{BASE_URL}/{REG_USER_URL}',
                             data={'Логин': payload.get('email'), 'Пароль': payload.get('password')})

    @staticmethod
    def create_user_without_email(payload):
        return requests.post(f'{BASE_URL}/{REG_USER_URL}',
                             data={'Имя': payload.get('name'), 'Пароль': payload.get('password')})

    @staticmethod
    def create_user_without_password(payload):
        return requests.post(f'{BASE_URL}/{REG_USER_URL}',
                             data={'Имя': payload.get('name'), 'Логин': payload.get('email')})

    @staticmethod
    def delete_user(token):
        requests.delete(f'{BASE_URL}/{USER_URL}', headers={'Authorization': token})