BASE_URL = 'https://stellarburgers.nomoreparties.site'
REG_USER_URL = 'api/auth/register'
LOGIN = 'api/auth/login'
USER_URL = 'api/auth/user'
ORDER_URL = 'api/orders'


import random
import string

def generate_payload():
    def generate_random_string(lenght):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(lenght))
        return random_string

    name = generate_random_string(10)
    email = f'{generate_random_string(8)}@gmail.com'
    password = generate_random_string(10)

    payload = {
        'name': name,
        'email': email,
        'password': password
    }
    return payload

def generate_order_data():
    return {"ingredients": ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa6f"]}

def generate_order_data_wrong_ingredients():
    return {"ingredients": ["1","12"]}


