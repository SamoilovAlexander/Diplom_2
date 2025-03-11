import requests

from data import BASE_URL, USER_URL


class ChangeUserData:
    @staticmethod
    def change_user_email_with_login(token, new_mail):
        return requests.patch(f'{BASE_URL}/{USER_URL}', headers={'Authorization': token}, data={'email': new_mail})

    @staticmethod
    def change_user_email_without_login(new_mail):
        return requests.patch(f'{BASE_URL}/{USER_URL}', data={'email': new_mail})