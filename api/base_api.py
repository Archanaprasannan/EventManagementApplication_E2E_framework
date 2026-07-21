class BaseAPI:
    def __init__(self,api_context):
        self.api_context= api_context

    def get(self,endpoint,**kwargs):
        return self.api_context.get(endpoint,**kwargs)

    def post(self,endpoint,**kwargs):
        return self.api_context.post(endpoint,**kwargs)

    def delete(self,endpoint,**kwargs):
        return self.api_context.delete(endpoint,**kwargs)

    def put(self,endpoint,**kwargs):
        return self.api_context.put(endpoint,**kwargs)

    def patch(self,endpoint,**kwargs):
        return self.api_context.patch(endpoint,**kwargs)