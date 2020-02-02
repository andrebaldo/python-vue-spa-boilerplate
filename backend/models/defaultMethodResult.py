# models\defaultMethodResult.py
# Author : Andre Baldo (http://github.com/andrebaldo/)
# A default class to build a default request response
# throught json serialization
class DefaultMethodResult():
    success: False
    message: ''
    def __init__(self, success, message):
        self.success = success
        self.message = message