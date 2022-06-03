import json
import time

import pytest
import requests
from jsonschema import validate

from backend.logger_funcs import log_response


#   ------------------------------- PET ---------------------------------------
@pytest.mark.parametrize(
    "status",
    [
        "available",
        "pending",
        "sold",
        "unsupported"
    ]
)
def test_get_pet_findbystatus(service_url_fixt,
                              status,
                              schema_pet_fixt,
                              test_header_without_apikey_fixt):
    url = service_url_fixt + '/pet/findByStatus'
    param_request = {'status': status}
    response = requests.get(url,
                            params=param_request,
                            headers=test_header_without_apikey_fixt)
    log_response(response)

    if status == 'unsupported':
        assert response.status_code == 400, response.text
        validate(instance=response.json(), schema='')
    else:
        for value in response.json():
            validate(instance=value, schema=schema_pet_fixt)
        assert response.status_code == 200, response.text


def test_get_pet_findbytags():
    pass


def test_get_pet_petid():
    pass


#   ------------------------------- STORE -------------------------------------
def test_get_store_inventory():
    pass


def test_get_store_order_orderid():
    pass


#   ------------------------------- USER --------------------------------------
@pytest.mark.parametrize(
    "request_params",
    [
        {"username": "user1",
         "password": "pswd1"},
        {"username": "absent_user",
         "password": "pswd1"},
        {"username": "user1"},

    ]
)
@pytest.mark.current
def test_get_user_login(service_url_fixt,
                        prepare_test_users_fixt,
                        test_header_without_apikey_fixt,
                        request_params):
    url = service_url_fixt + '/user/login'

    response = requests.get(url,
                            params=request_params,
                            headers=test_header_without_apikey_fixt)
    log_response(response)

    if request_params.get("username") == "user1":
        if "password" not in request_params.keys():
            assert response.status_code != 200, response.text
        else:
            assert response.status_code == 200, response.text
            assert int(response.headers.get("X-Rate-Limit")) > 0
            expire_time = response.headers.get("X-Expires-After")
            t = time.strptime(expire_time, "%a %b %d %H:%M:%S %Z %Y")
            assert time.mktime(t) > time.mktime(time.gmtime())
            assert response.headers.get("Set-Cookie") != ""
    elif request_params.get("username") == "absent_user":
        assert response.status_code == 400, response.text


def test_get_user_logout():
    pass


def test_get_user_username():
    pass


#   ------------------------------- UNSUPPORTED -------------------------------
@pytest.mark.parametrize(
    "endpoint",
    [
        "/user",
        "/pet",
        "/pet/pet/uploadImage",
        "/store/order",
        "/user/createWithArray",
        "/user/createWithList"
    ]
)
def test_get_unsupported(service_url_fixt,
                         endpoint,
                         test_header_without_apikey_fixt):
    url = service_url_fixt + endpoint
    response = requests.get(url,
                            headers=test_header_without_apikey_fixt)
    log_response(response)

    j = json.loads(response.text)
    assert response.status_code == 405, response.text
    assert j['code'] == 405, response.text
    assert j['type'] == 'unknown', response.text
