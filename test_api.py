import requests

def handle_request(url):
    response = requests.get(url)

    if response.status_code == 200:
        print("Success, code:", response.status_code)
    else:
        raise Exception("Fail, code:", response.status_code)

    print(response.headers["Content-Type"])

    response_dict = response.json()
