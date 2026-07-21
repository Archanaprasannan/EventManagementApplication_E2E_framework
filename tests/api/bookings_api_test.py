import allure
import pytest

pytest.mark.regression
pytest.mark.api
class TestBookingsAPI:
    @allure.title("TC_API_005 - Create new booking")
    def test_create_booking(self,bookings_api,auth_token):
        payload={"customerEmail": "archiie1710@gmail.com",
                    "customerName": "Archana Prasannan",
                        "customerPhone": "7896541230",
                        "eventId": 3,
                            "quantity": 1}
        response= bookings_api.create_bookings(auth_token,payload)
        assert response.status==201

        response_body=response.json()["data"]
        assert response_body["eventId"]==payload["eventId"]
        assert response_body["customerName"] == payload["customerName"]
        assert response_body["customerEmail"] == payload["customerEmail"]
        assert response_body["quantity"] == payload["quantity"]

    @allure.title("TC_API_006 - verify all the event bookings")
    def test_get_my_bookings(self,bookings_api,auth_token,get_booking_details):
        first_booking_data_id=get_booking_details["id"]

        response=bookings_api.get_booking_details_by_id(auth_token,first_booking_data_id)
        data = response.json()["data"][0]
        print(type(data))
        print(data)
        #assert data["id"] == first_booking_data["id"]
        assert data["customerName"] == get_booking_details["customerName"]
        assert data["customerEmail"] == get_booking_details["customerEmail"]
        assert data["userId"] == get_booking_details["userId"]

    @allure.title("TC_API_007 - cancel the event booking")
    def test_cancel_booking(self,bookings_api,auth_token,get_booking_details):
        first_booking_data_id = get_booking_details["id"]

        response= bookings_api.cancel_booking(auth_token,first_booking_data_id)
        assert response.status==200

        response_body=response.json()
        print(response.url)
        print(response.status)
        print(response.text())
        assert response_body["message"]=="Booking cancelled"