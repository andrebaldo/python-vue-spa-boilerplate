class DefaultMethodResult():
    success: False
    message: ''
    def __init__(self, success, message):
        self.success = success
        self.message = message