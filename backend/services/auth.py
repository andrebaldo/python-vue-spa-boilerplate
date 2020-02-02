# services\auth.py
# Author : Andre Baldo (http://github.com/andrebaldo/)
# This module deals with the authentication process and authentication checks.
import jwt
from entities.user import User
from entities.userSession import UserSession
from models.defaultMethodResult import DefaultMethodResult
from models.loginTokenResult import LoginTokenResult
from werkzeug import check_password_hash, generate_password_hash
from datetime import datetime, timedelta
from sqlalchemy import and_, or_, update
from entities.databaseSessionManager import SessionManager



JWT_EXP_DELTA_SECONDS = 20
SESSION_TIMEOUT_IN_HOURS = 24

class Auth():
    dbSession = SessionManager().session
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
            self.dbSession.add(newUser)
            self.dbSession.commit()
            return DefaultMethodResult(True, 'User Created')

        return DefaultMethodResult(False, error)
        
    def validateRegisterData(self, username, password) -> LoginTokenResult:
        """
        Check if the username and password are correct, returns a text error if
        they are not correct.
        """
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
        result = self.dbSession.query(User).filter_by(username=username).first()
        # If the result returns some user sets an error
        if result is not None:
            error = 'User {} is already registered.'.format(username)

        return error

    def getLoginToken(self, username, password, appSecret):
        """
        It does some basic validations first and then checks if the password
        matches with the one stored into the database, case the credentials
        were accepted a login token is created onto the database and returned.
        """
        error = None
        # The condition if not checks for None or empty values.
        if not username:
            error = 'Username is required.'
        # Also checks the password for None or empty values
        elif not password:
            error = 'Password is required.'
        # Query our database to check username exists
        result = self.dbSession.query(User).filter_by(username=username).first()
        if result is None:
            error = 'Invalid credentials'
        else:
            if check_password_hash(result.password, password) == False:
                error = 'Invalid credentials'

        success = False
        if error is None:
            success = True
            payload = {
                'userId': result.userId,
                'exp': datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)
            }
            jwt_token = jwt.encode(payload, appSecret,algorithm='HS256')
            #decodedToken = jwt.decode(jwt_token, appSecret, algorithms=['HS256'])
            jwtDecoded = jwt_token.decode("utf-8")
            self.createUserSessionOnDatabase(result.userId, jwtDecoded)
            return LoginTokenResult(success, 'login result', jwtDecoded)
        else:
            return LoginTokenResult(False, error, '')

    def createUserSessionOnDatabase(self, userId, jwToken):
        """
        Adds a new register into UserSession table to keep the user session 
        kactive until it expires or revoked via logout
        """
        userSession = UserSession(
            userId = userId,
            loggedOut = False,
            loginDate = datetime.now(),
            expireDate = datetime.now() + timedelta(hours=SESSION_TIMEOUT_IN_HOURS), 
            jwToken=jwToken
        )
        self.dbSession.add(userSession)
        self.dbSession.commit()

    def load_user(self, user_id):
        return self.dbSession.query(User).get(int(user_id))

    def GetUserByEmail(self, email):
        return self.dbSession.query(User).filter_by(username=email).first()

    def GetUserByToken(self, jwt):
        filtered = self.dbSession.query(UserSession).order_by(UserSession.userSessionId).filter(
           and_(UserSession.jwToken==jwt ,UserSession.expireDate > datetime.now(), UserSession.loggedOut == False)
           )
        activeSession = filtered.first()

        if activeSession is not None:
            return self.dbSession.query(User).get(activeSession.userId)
        else:
            return None
    
    def SessionLogout(self, jwt, url):
        """
        Sets the session as logged out and set the logoutDate.
        """
        if jwt is not None:
            currentUserSession = self.dbSession.query(UserSession).filter_by(jwToken=jwt).first()
            if currentUserSession is not None:
                if currentUserSession.loggedOut == False:
                    currentUserSession.loggedOut = True
                    currentUserSession.logoutDate = datetime.now()
                    currentUserSession.url = url
                    self.dbSession.commit()
                return DefaultMethodResult(True, 'Logout completed')
        
        return DefaultMethodResult(False, 'Error trying to logout')

    def GetActiveSession(self, jwt):
        """
        Returns an active login session for the give JWToken, if it exists.
        """
        if jwt is not None:
            currentUserSession = self.dbSession.query(UserSession).filter_by(jwToken=jwt).first()
            if currentUserSession is not None:
                if currentUserSession.loggedOut == False:
                    return currentUserSession
        return None

 

    

      