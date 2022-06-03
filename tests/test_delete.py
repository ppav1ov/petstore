import pytest
import requests
from backend.logger_funcs import log_response


#   ------------------------------- PET ---------------------------------------
def test_delete_pet_petid():
    pass


#   ------------------------------- STORE -------------------------------------
def test_delete_store_order_orderid():
    pass


#   ------------------------------- USER --------------------------------------
@pytest.mark.parametrize(
    "username",
    [
        'user1',
        'absent_user'
    ]
)
def test_delete_user_username(service_url_fixt,
                              prepare_test_users_fixt,
                              username,
                              test_header_with_apikey_fixt):
    url = service_url_fixt + "/user/" + username

    response = requests.delete(url, headers=test_header_with_apikey_fixt)
    log_response(response)

    if username == 'user1':
        assert response.status_code == 200, response.text
        assert response.json()['message'] == 'user1', response.text
        response_get_deleted_user = requests.get(url)
        assert response_get_deleted_user.status_code == 404, \
            response_get_deleted_user.text
    elif username == 'absent_user':
        assert response.status_code == 404, response.text
        assert response.text == '', response.text


#   ------------------------------- UNSUPPORTED -------------------------------
def test_delete_unsupported():
    pass
