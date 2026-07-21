import allure
import pytest

from constants.appconstants import AppConstants

pytest.mark.regression
pytest.mark.api
class TestAllEventsAPI:
    @allure.title("TC_API_002 - Verify user can get all events in the page")
    def test_all_events(self,auth_token,events_api):
        response= events_api.get_all_events(auth_token)
        assert response.status==200
        response_data=response.json()
        assert response_data["success"] is True
        assert len(response_data["data"])>0

    # def test_first_event(self,auth_token,events_api):
    #     response = events_api.get_all_events(auth_token)
    #     assert response.status == 200
    #     response_data = response.json()
    #     assert response_data["data"][0]["title"]=="Dilli Diwali Mela"
    #     assert response_data["data"][0]["venue"] == "Pragati Maidan Exhibition Grounds"
    #     assert response_data["data"][0]["price"] == "300"
    @allure.title("TC_API_003 - Verify user can get the fisrt event by ID")
    def test_event_by_id(self,auth_token,events_api):
        #get all evnts
        all_events = events_api.get_all_events(auth_token)
        all_events_data=all_events.json()
        #extarct teh fisrt event id
        first_event_id=all_events_data["data"][0]["id"]
        response= events_api.get_event_by_id(auth_token,first_event_id)
        assert response.status == 200
        event = response.json()["data"]
        assert event["id"] == first_event_id

    @allure.title("TC_API_004 - Verify event by ID")
    def test_event_details_by_id(self,auth_token,events_api):
        all_events = events_api.get_all_events(auth_token)
        assert all_events.status==200
        all_events_data = all_events.json()
        first_event = all_events_data["data"][0]
        event_id=first_event["id"]
        response = events_api.get_event_by_id(auth_token, event_id)
        data=response.json()["data"]
        assert data["id"]==first_event["id"]
        assert data["title"]==first_event["title"]
        assert data["venue"] == first_event["venue"]
        assert data["price"] == first_event["price"]






