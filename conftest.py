import pytest
from pycparser.ply.yacc import token

from data import generate_payload
from methods.creating_user_methods import NewUserMethods
from methods.login_user_methods import LoginUserMethods


@pytest.fixture()
def user():
    payload = generate_payload()
    resp = NewUserMethods.create_user(payload)
    yield payload
    NewUserMethods.delete_user(resp.json()['accessToken'])

@pytest.fixture()
def auth_user():
    payload = generate_payload()
    response = NewUserMethods.create_user(payload)
    response_2 = LoginUserMethods.login_user({'email': payload.get('email'), 'password': payload.get('password')})
    yield response_2
    NewUserMethods.delete_user(response.json()['accessToken'])

