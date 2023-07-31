import requests
from pages.apiTesingPage import ApiTestingData

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
print(route_authen)
print(signin_repsonse)

# assert signin_repsonse.status_code == 200
# signin_token = signin_repsonse.json()["AccessToken"]
