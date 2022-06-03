import pytest
import requests
import json
from jsonschema import validate
from backend.logger_funcs import log_response


#   ------------------------------- PET ---------------------------------------
def test_put_pet():
    pass


#   ------------------------------- USER --------------------------------------
@pytest.mark.current
@pytest.mark.parametrize(
    "username, new_user_data",
    [
        ("user1",
         {
             "id": 1,
             "username": "user1",
             "firstName": "changed_firstName",
             "lastName": "changed_lastName",
             "email": "lastName_email",
             "password": "changed_pswd",
             "phone": "changed_phone",
             "userStatus": 1
         }),
        ("absent_user",
         {
             "id": 1,
             "username": "absent_user",
             "firstName": "changed_firstName",
             "lastName": "changed_lastName",
             "email": "lastName_email",
             "password": "changed_pswd",
             "phone": "changed_phone",
             "userStatus": 1
         })
    ]
)
def test_put_user_username(
        service_url_fixt,
        prepare_test_users_fixt,
        schema_user_fixt,
        username,
        new_user_data,
        test_header_with_apikey_fixt):

    url = service_url_fixt + "/user/" + username

    response = requests.put(url,
                            data=json.dumps(new_user_data),
                            headers=test_header_with_apikey_fixt)
    log_response(response)

    if username == 'user1':
        assert response.status_code == 200, response.text
        get_user_response = requests.get(url)
        j = get_user_response.json()
        validate(instance=j, schema=schema_user_fixt)
        assert j['firstName'] == 'changed_firstName', get_user_response.text
        assert j['lastName'] == 'changed_lastName', get_user_response.text
        assert j['email'] == 'lastName_email', get_user_response.text
        assert j['password'] == 'changed_pswd', get_user_response.text
        assert j['phone'] == 'changed_phone', get_user_response.text
        assert j['userStatus'] == 1, get_user_response.text

    elif username == 'absent_user':     # BUG: sending 200 instead of 404
        get_user_response = requests.get(url)
        log_response(get_user_response)
        assert response.status_code == 404, response.text


#   ------------------------------- UNSUPPORTED -------------------------------
def test_put_unsupported():
    pass
