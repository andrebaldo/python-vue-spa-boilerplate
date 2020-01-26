# file path: /backend/services/auth.py
from entities.user import User
from models.defaultMethodResult import DefaultMethodResult
from werkzeug import check_password_hash, generate_password_hash

class Auth():
    db = None
    def __init__(self, db):
        self.db = db
    def register(self, username, password, mobilePhone) -> DefaultMethodResult:
        """
        This method will validate the data and create a new registration
        into our database.
        """
        error = self.validateRegisterData(username, password)

        # Converts the plain text password into a hash using the method 'generate_password_hash' from the 'werkzeug' library/package
        password = generate_password_hash(password)
        # If the error var still set as None, if is None proceed to the user creation
        # But if there is an error set, returns this error to the browser
        if error is None:
            newUser =  User(username = username, password = password, mobilePhone = mobilePhone)
            self.db.session.add(newUser)
            self.db.session.commit()
            return DefaultMethodResult(True, 'User Created')

        return DefaultMethodResult(False, error)
        
    def validateRegisterData(self, username, password):
        error = None
        # The condition if not checks for None or empty values.
        if not username:
            error = 'Username is required.'
        # Also checks the password for None or empty values
        elif not password:
            error = 'Password is required.'

        if len(password) < 7:
            error = 'Password length is less than 8.'
        
        # Query our database to check if the username is already registred
        user = User()
        result = user.query.filter_by(username=username).first()
        # If the result returns some user sets an error
        if result is not None:
            error = 'User {} is already registered.'.format(username)

        return error