from api.base_api import BaseAPI
from constants.appconstants import AppConstants


class EventsAPI(BaseAPI):
    def __init__(self,api_context):
        super().__init__(api_context)


    def get_all_events(self,token):
        endpoint=f"{AppConstants.EVENT_ENDPOINTS}"
        return self.get(endpoint,headers={"Authorization":f"Bearer {token}"})

    def get_event_by_id(self,token,event_id):
        endpoint=f"{AppConstants.EVENT_ENDPOINTS}/{event_id}"
        return self.get(endpoint,headers={"Authorization":f"Bearer {token}"})