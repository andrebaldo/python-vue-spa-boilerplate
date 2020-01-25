# file path: /backend/services/auth.py
from entities.user import User
from flask import jsonify, request, session, redirect
from werkzeug import check_password_hash, generate_password_hash

class Auth():
    db = None
    def __init__(self, db):
        self.db = db
    def register(self, request):
        """
        This method will receive the data from the request form via POST method, 
        the data needed is email and password them it will try to save the data 
        into our database.
        """
        # Allow just POST HTTP requests request is a built-in object provided by flask
        if request.method == 'POST':  
            # Get data from the request, in this case
            requestPayload = request.get_json()  
            usernameFromBrowser = requestPayload['email']
            passwordFromBrowser = requestPayload['password']

            # Converts the plain text password into a hash using the method 'generate_password_hash' from the 'werkzeug' library/package
            passwordFromBrowser = generate_password_hash(passwordFromBrowser)
            error = None
            # The condition if not checks for None or empty values.
            if not usernameFromBrowser:
                error = 'Username is required.'
            # Also checks the password for None or empty values
            elif not passwordFromBrowser:
                error = 'Password is required.'
        
            # Query our database to check if the username is already registred
            user = User()
            result = user.query.filter_by(username=usernameFromBrowser).first()
            # If the result returns some user sets an error
            if result is not None:
                error = 'User {} is already registered.'.format(usernameFromBrowser)

            # If the error var still set as None, if is None proceed to the user creation
            # But if there is an error set, returns this error to the browser
            if error is None:
                newUser =  User(username=usernameFromBrowser, password=passwordFromBrowser, mobilePhone= requestPayload['mobilePhone'])
                self.db.session.add(newUser)
                self.db.session.commit()
                return jsonify({'success':True, 'message': 'User Created'})

            return jsonify({'success':False, 'message': error}), 500
