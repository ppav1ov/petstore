import json

import pytest
import requests

from backend.constants import SCHEMA_PET, SCHEMA_USER


@pytest.fixture
def service_url_fixt():
    return "https://petstore.swagger.io/v2"


@pytest.fixture
def api_key_fixt():
    return 'special-key'


@pytest.fixture
def schema_pet_fixt():
    return SCHEMA_PET


@pytest.fixture
def schema_user_fixt():
    return SCHEMA_USER


@pytest.fixture
def test_header_with_apikey_fixt(api_key_fixt):
    return {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': api_key_fixt
    }


@pytest.fixture
def test_header_without_apikey_fixt():
    return {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }


@pytest.fixture
def prepare_test_users_fixt(service_url_fixt, test_header_with_apikey_fixt):
    test_user_data = {
        "id": 1,
        "username": "user1",
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "password": "pswd1",
        "phone": "string",
        "userStatus": 0
    }
    url = service_url_fixt + "/user"
    response = requests.post(url,
                             data=json.dumps(test_user_data),
                             headers=test_header_with_apikey_fixt)
    assert response.status_code == 200, response.text

    url = service_url_fixt + "/user/absent_user"
    if requests.get(url).status_code == 200:
        requests.delete(url, headers=test_header_with_apikey_fixt)

    assert requests.get(url).status_code == 404, response.text
