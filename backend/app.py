# file path: /backend/app.py
import flask 
from services.auth import Auth
from services.database import Database

database = Database()

app = flask.Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = database.getConnectionString()
app.secret_key = 'this will be used to cryptograph sensible data like authentication tokens'

db = database.createDatabaseInstance(app)
authModule = Auth(db)
db.create_all()

# Sets the route for this endpoint, this will configure our web server to receive requests at this path.
@app.route('/register', methods=(['POST']))
def register():
    return authModule.register(request)

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