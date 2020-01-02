from udsapi.exceptions import SignInFailed, DoubleRequestException
from udsapi.headers import Headers
from udsapi.engine import FetchEngine


class Auth:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__header = Headers()
        self.__fetch = FetchEngine()
        self.__base_url = 'https://www.udsmis.com/signin'
        self._response = self.__fetch.get(self.__base_url, session=False)
        self.__header.event_validator = self._response.find('input', {'name': '__EVENTVALIDATION'}).get('value')
        self.__header.view_state = self._response.find('input', {'name': '__VIEWSTATE'}).get('value')
        self.__header.cbo_type = 'Login'
        self.__header.btnlogin = 'Sign In'
        self.__header.view_state_generator = self._response.find('input', {'name': '__VIEWSTATEGENERATOR'}).get('value')
        self.__header.username = self.__username
        self.__header.password = self.__password

    @property
    def auth_sessions(self):
        return self.__fetch

    @property
    def response(self):
        return self._response

    def login(self):
        if not self.__fetch.session.cookies.get('Students') is None:
            raise DoubleRequestException('Cant have Double Authentication')

        self.__fetch.post(self.__base_url, self.__header.request_header)

        if self.__fetch.session.cookies.get('Students') is None:
            raise SignInFailed('Login Failed, Please Check Credentials')

        return self.auth_sessions


