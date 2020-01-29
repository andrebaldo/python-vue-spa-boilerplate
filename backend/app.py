# file path: /backend/app.py
import flask 
from services.auth import Auth
from models.defaultMethodResult import DefaultMethodResult
from models.loginTokenResult import LoginTokenResult
from flask import jsonify, request, session, redirect
from services.database import Database
from services.jsonClassEncoder import JsonClassEncoder


database = Database()

app = flask.Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = database.getConnectionString()
app.secret_key = 'this will be used to cryptograph sensible data like authentication tokens'

db = database.createDatabaseInstance(app)
authModule = Auth(db)
db.create_all()
jsonClassEncoder = JsonClassEncoder()

# Sets the route for this endpoint, this will configure our web server to receive requests at this path.
@app.route('/register', methods=(['POST']))
def register():
    requestPayload = request.get_json()  
    username = requestPayload['email']
    password = requestPayload['password']
    mobilePhone= requestPayload['mobilePhone']

    registerResult = authModule.register(username, password, mobilePhone)
    if registerResult.success == True:
        return jsonClassEncoder.encode(registerResult), 200
    else:
        return jsonClassEncoder.encode(registerResult), 500

@app.route('/token', methods=(['POST']))
def token():
    requestPayload = request.get_json()  
    username = requestPayload['email']
    password = requestPayload['password']
    loginResult = authModule.getLoginToken(username, password, app.config['SECRET_KEY'])
    if loginResult.success == True:
        return jsonClassEncoder.encode(loginResult), 200
    else:
        return jsonClassEncoder.encode(loginResult), 401

def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    if request.method == 'OPTIONS':
        response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
        headers = request.headers.get('Access-Control-Request-Headers')
        if headers:
            response.headers['Access-Control-Allow-Headers'] = headers

    return response

app.after_request(add_cors_headers)

app.run()