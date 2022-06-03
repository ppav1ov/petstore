import requests
from backend.logger_funcs import log_response


#   ------------------------------- PET ---------------------------------------
def test_patch_pet(service_url_fixt,
                   prepare_test_users_fixt,
                   test_header_without_apikey_fixt):
    url = service_url_fixt + '/pet/user1'
    response = requests.head(url, headers=test_header_without_apikey_fixt)
    log_response(response)
    assert response.status_code == 405


#   ------------------------------- STORE -------------------------------------
def test_head_store():
    pass


#   ------------------------------- USER --------------------------------------
def test_head_user(service_url_fixt,
                   prepare_test_users_fixt,
                   test_header_without_apikey_fixt):
    url = service_url_fixt + '/user/user1'
    response = requests.head(url, headers=test_header_without_apikey_fixt)
    log_response(response)
    assert response.status_code == 405


#   ------------------------------- UNSUPPORTED -------------------------------
def test_head_unsupported_endpoint():
    pass
