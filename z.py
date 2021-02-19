import requests
import json
base_url = "http://127.0.0.1:8000/"
endpoint = "api/"

def get_resources(id=None):
    data = {}
    if id is not None:
        data = {
            'id':id
        }
    resp = requests.get(base_url+endpoint,data = json.dumps(data))
    print(resp.status_code)
    print(resp.json())

get_resources(2)

