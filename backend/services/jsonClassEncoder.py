from json import JSONEncoder
class JsonClassEncoder(JSONEncoder):
        def default(self, o):
            tomate = 1
            return o.__dict__  