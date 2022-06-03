import json

import pytest
import requests

from backend.logger_funcs import log_response


#   ------------------------------- PET ---------------------------------------
def test_post_pet_petid_uploadimage():
    pass


def test_post_pet_petid():
    pass


def test_post_pet():
    pass


#   ------------------------------- STORE -------------------------------------
def test_post_store_order():
    pass


#   ------------------------------- USER --------------------------------------
@pytest.mark.parametrize(
    "request_body",
    [
        {
            "id": 1,
            "username": "user1",
            "firstName": "string",
            "lastName": "string",
            "email": "string",
            "password": "pswd1",
            "phone": "string",
            "userStatus": 0
        },
        {
            "id": "f",
            "username": "user_wrongid",
            "firstName": "string",
            "lastName": "string",
            "email": "string",
            "password": "pswd1",
            "phone": "string",
            "userStatus": 0
        },
        {
            "id": 2,
            "username": "user_wrong_userstatus",
            "firstName": "string",
            "lastName": "string",
            "email": "string",
            "password": "pswd1",
            "phone": "string",
            "userStatus": 2147483649
        }
    ]
)
def test_post_user_authenticated(service_url_fixt,
                                 request_body,
                                 test_header_with_apikey_fixt):
    url = service_url_fixt + "/user"

    response = requests.post(url,
                             data=json.dumps(request_body),
                             headers=test_header_with_apikey_fixt)
    log_response(response)

    if request_body["username"] == "user_wrongid":
        assert response.status_code == 400, response.text
    elif request_body["username"] == "user_wrong_userstatus":
        assert response.status_code == 400, response.text
    else:
        assert response.status_code == 200, response.text
        assert response.json()['message'] == str(request_body['id'])


def test_post_user_unauthenticated(service_url_fixt):
    url = service_url_fixt + "/user"
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    request_body = {
        "id": 1,
        "username": "user1",
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "password": "pswd1",
        "phone": "string",
        "userStatus": 0
    }

    response = requests.post(       # BUG: works without API key
        url, data=json.dumps(request_body), headers=headers)
    log_response(response)
    assert response.status_code != 200, response.text


def test_post_user_createwitharray():
    pass


def test_post_user_createwithlist():
    pass


#   ------------------------------- UNSUPPORTED -------------------------------
def test_post_unsupported():
    pass