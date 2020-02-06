# models\loginTokenResult.py
# Author : Andre Baldo (http://github.com/andrebaldo/)
# A specialized model to build a response for login requests.
class LoginTokenResult():
    success = False
    message = ''
    token = ''

    def __init__(self, success, message, token):
        self.success = success
        self.message = message
        self.token = token
