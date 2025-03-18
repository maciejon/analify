import requests

def handle_request(url, type, headers='', data=''):

    if type == 'GET':
        response = requests.get(url,headers=headers)

        if response.status_code == 200:
            print("Success, code:", response.status_code)
        else:
            raise Exception("Fail, code:", response.status_code)

        print(response.headers["Content-Type"])
    return response
    # response_dict = response.json()