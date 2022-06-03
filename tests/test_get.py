import pytest
import requests
import json
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
def test_get_user_login():
    pass


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
    response = requests.get(url, headers=test_header_without_apikey_fixt)
    log_response(response)

    j = json.loads(response.text)
    assert response.status_code == 405, response.text
    assert j['code'] == 405, response.text
    assert j['type'] == 'unknown', response.text
