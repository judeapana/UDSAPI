__author__ = 'Apana Jude Yinime'

"""
Authenticate User To Retrieve Session
"""
from udsapi.APIEngine.engine import FetchEngine
from udsapi.APIExceptions.exceptions import SignInFailedException, DoubleRequestException
from udsapi.APIHeaders.headers import Headers


class Auth:
    """
    Authentication Manager
    """

    def __init__(self, username, password, securityCode):
        self.__username = username
        self.__password = password
        self.__securityCode = securityCode
        self.__header = Headers()
        self.__fetch = FetchEngine()
        self.__base_url = 'https://mis.uds.edu.gh/signin'
        self.__response = self.__fetch.get(self.__base_url, session=False)
        self.__header.eventValidator = self.__response.find('input', {'name': '__EVENTVALIDATION'}).get('value')
        self.__header.viewState = self.__response.find('input', {'name': '__VIEWSTATE'}).get('value')
        self.__header.cboType = 'Login'
        self.__header.btnLogin = 'Sign In'
        self.__header.viewStateGenerator = self.__response.find('input', {'name': '__VIEWSTATEGENERATOR'}).get('value')
        self.__header.username = self.__username
        self.__header.password = self.__password

        print(self.__response.find('input', {'name': 'ctl00$ContentPlaceHolder1$ImageButton1'}).get('src'))

        self.__header.securityCode = self.__securityCode

    @property
    def sessionManager(self):
        """

        :return: session
        """
        return self.__fetch

    @property
    def response(self):
        """
        response object
        :return:
        """
        return self.__response

    def login(self):
        """
        Use this function should be used once in authentication
        if session dies or timeout it can be used again
        :return:
        """

        if not self.__fetch.session.cookies.get('Students') is None:
            raise DoubleRequestException('Cant have Double Authentication')

        self.__fetch.post(self.__base_url, self.__header.requestHeader)

        if self.__fetch.session.cookies.get('Students') is None:
            raise SignInFailedException('Login Failed, Please Check Credentials')
