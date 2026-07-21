from playwright.sync_api import APIRequestContext

from api.base_api import BaseAPI


class AuthAPI(BaseAPI):
    def __init__(self, api_context):
        super().__init__(api_context)

    def api_login(self, endpoint, email, password):
        return self.post(endpoint, data={"email": email, "password": password})
