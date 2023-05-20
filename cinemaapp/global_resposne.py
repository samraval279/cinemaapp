
class ResponseInfo:
    
    def __init__(self, data, message, status):
        self.data = data
        self.message = message
        self.status = status

    def custom_success_payload(self):
        # if error in payload
        if 'error' in self.data:
            self.message = self.data['error']
            self.data = {}

        temp_custom_success = {
            "data": self.data,
            "message": self.message,
            "status": self.status
        }
        return temp_custom_success