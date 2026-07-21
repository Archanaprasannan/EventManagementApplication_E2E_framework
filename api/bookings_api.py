from api.base_api import BaseAPI
from constants.appconstants import AppConstants


class BookingsAPI(BaseAPI):

    def __init__(self,api_context):
        super().__init__(api_context)

    def create_bookings(self,auth_token,payload):
        endpoint=f"{AppConstants.BOOKING_ENDPOINT}"
        return self.post(endpoint,headers={"Authorization":f"Bearer {auth_token}"},data= payload)

    def get_all_bookings(self,auth_token):
        endpoint=f"{AppConstants.MY_BOOKING_ENDPOINT}"
        return self.get(endpoint,headers={"Authorization":f"Bearer {auth_token}"})

    def get_booking_details_by_id(self,auth_token,id):
        endpoint = f"{AppConstants.MY_BOOKING_ENDPOINT}/{id}"
        return self.get(endpoint,headers={"Authorization":f"Bearer {auth_token}"})

    def cancel_booking(self,auth_token,id):
        endpoint = f"{AppConstants.BOOKING_ENDPOINT}/{id}"
        print(endpoint)
        return self.delete(endpoint,headers={"Authorization":f"Bearer {auth_token}"})