
import pytest
import requests
import json


@pytest.fixture()
def api_operation_get(request):
    req = request.param[0]
    url = request.param[1]
    print(url)
    res = getattr(requests, req)(url)
    return res.status_code


@pytest.fixture()
def api_operation_put(request):
    url = request.param[1]
    file = open('F:\\gaurav.json', 'r')
    json_input = file.read()
    req_json = json.loads(json_input)
    req = request.param[0]

    res = getattr(requests, req)(url, req_json)
    return res.status_code
