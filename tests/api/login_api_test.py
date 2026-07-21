import allure
import pytest

from constants.appconstants import AppConstants
from utils.config_reader_util import ConfigReader
pytest.mark.regression
pytest.mark.api
class TestLoginPageAPI:
    @allure.title("TC_API_001 - Verify user can Login to teh page")
    def test_login_api(self,auth_api):
        response= auth_api.api_login(AppConstants.LOGIN_ENDPOINT,ConfigReader.get_email(),ConfigReader.get_password())
        #verify the HTTP status
        assert response.status == 200
        # Convert APIResponse -> Python Dictionary
        response_data=response.json()
        # Verify Response Body
        assert response_data["success"] is True
        assert response_data["token"]!=""
        assert response_data["user"]["id"]>0
        assert response_data["user"]["email"]==ConfigReader.get_email()

