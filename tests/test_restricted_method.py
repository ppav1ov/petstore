import pytest
import requests
from backend.logger_funcs import log_response


#   ------------------------------- PET ---------------------------------------
def test_patch_pet(service_url,
                   prepare_test_users,
                   test_header_without_apikey):
    url = service_url + '/pet/user1'
    response = requests.head(url, headers=test_header_without_apikey)
    log_response(response)
    assert response.status_code == 405


#   ------------------------------- STORE -------------------------------------
def test_head_store():
    pass


#   ------------------------------- USER --------------------------------------
def test_head_user(service_url,
                   prepare_test_users,
                   test_header_without_apikey):
    url = service_url + '/user/user1'
    response = requests.head(url, headers=test_header_without_apikey)
    log_response(response)
    assert response.status_code == 405


#   ------------------------------- UNSUPPORTED -------------------------------
def test_head_unsupported_endpoint():
    pass
