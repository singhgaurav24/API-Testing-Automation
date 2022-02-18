import pytest


class Test01:
    @pytest.mark.parametrize("api_operation_get", [["get", "https://reqres.in/api/users?page=2"],
                                                   ["delete", "https://reqres.in/api/users/2"]], indirect=True)
    def test_get(self, api_operation_get):
        assert api_operation_get == 200

    @pytest.mark.parametrize("api_operation_put", [["put", "https://reqres.in/api/users/2"],
                                                   ["post", "https://reqres.in/api/users"]], indirect=True)
    def test_put(self, api_operation_put):
        assert api_operation_put == 200

