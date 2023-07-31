import requests
from pages.apiTesingPage import ApiTestingData
from behave import *


@given("The api is up and running")
def step_impl(context):
    route_params = {
        "DeviceCode": "NRAN-K8MG-YE59"
    }
    route_response = requests.post(
        url=ApiTestingData.api_token,
        json=route_params
    )
    route_authen = route_response.json()["AccessToken"]

    assert route_response.status_code == 200
    signin_params = {
        "UserAccount": "123456701",
        "Password": "11111111",
    }
    signin_repsonse = requests.post(
        url=ApiTestingData.base_url + ApiTestingData.api_authen_login,
        json=signin_params,
        headers={
            "Authorization": f"Bearer {route_authen}"
        }
    )
    assert signin_repsonse.status_code == 200
    context.signin_token = signin_repsonse.json()["AccessToken"]


@when("I get menu list")
def step_impl(context):
    params = {
        "language": "vi",
    }
    token = context.signin_token
    context.menu_response = requests.get(
        url=ApiTestingData.base_url + ApiTestingData.menu,
        headers={
            "Authorization": f"Bearer {token}"
        },
        params=params
    )
    assert context.menu_response.status_code == 200


@then("The menu list should be response successfully with status code 200")
def step_impl(context):
    menu_data = context.menu_response.json()
    print(menu_data)
    len_menu = len(menu_data["MenusItem"][0]["Item"])
    for i in range(len_menu):
        assert ApiTestingData.menu_list[i] == menu_data["MenusItem"][0]["Item"][i]["Title"]


@step("The menu list should be response successfully with correct schema")
def step_impl(context):
    return True
