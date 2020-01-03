"""

For Application Post And Get Headers

"""

from udsapi.APIExceptions.exceptions import ValueNotFoundException


class Headers:
    """
    Base Class Headers
    """

    __request = {}

    def __init__(self):
        self.__request['ctl00$cboType'] = ''
        self.__request['__EVENTARGUMENT'] = ''
        self.__request['__EVENTTARGET'] = ''
        self.__request['__VIEWSTATEENCRYPTED'] = ''
        self.__request['ctl00$ContentPlaceHolder1$btnlogin'] = ''
        self.__request['Accept'] = ''
        self.__request['User-Agent'] = ''
        self.__request['Content-Type'] = ''
        self.__request['ctl00$ContentPlaceHolder1$txtStudentID'] = ''
        self.__request['ctl00$ContentPlaceHolder1$txtPassword'] = ''
        self.__request['__EVENTVALIDATION'] = ''
        self.__request['__VIEWSTATE'] = ''
        self.__request['__VIEWSTATEGENERATOR'] = ''
        self.__request['ctl00_ScriptManager1_HiddenField'] = ''

    @property
    def btnLogin(self):
        """
        :return: value
        """
        return self.__request['ctl00$ContentPlaceHolder1$btnlogin']

    @property
    def eventValidator(self):
        """
        :return: value
        """
        return self.__request['__EVENTVALIDATION']

    @property
    def viewState(self):
        """
        :return: value
        """
        return self.__request['__VIEWSTATE']

    @property
    def viewStateGenerator(self):
        """
        :return: value
        """
        return self.__request['__VIEWSTATEGENERATOR']

    @property
    def hiddenField(self):
        """
        :return: value
        """
        return self.__request['ctl00_ScriptManager1_HiddenField']

    @property
    def requestHeader(self):
        """
        :return: value
        """
        return self.__request

    @property
    def password(self):
        """
        :return: value
        """
        return self.__request['ctl00$ContentPlaceHolder1$txtPassword']

    @property
    def username(self):
        """
        :return: value
        """
        return self.__request['ctl00$ContentPlaceHolder1$txtStudentID']

    @property
    def eventTarget(self):
        """
        :return: value
        """
        return self.__request['__EVENTTARGET']

    @property
    def cboType(self):
        """
        :return: value
        """
        return self.__request['ctl00$cboType']

    @username.setter
    def username(self, value):
        """
        :param value: username
        :return:
        """
        if value is None:
            raise ValueNotFoundException('Value Was Not Found')
        self.__request['ctl00$ContentPlaceHolder1$txtStudentID'] = value

    @password.setter
    def password(self, value):
        """
        :param value: password
        :return:
        """
        if value is None:
            raise ValueNotFoundException('Value Was Not Found')
        self.__request['ctl00$ContentPlaceHolder1$txtPassword'] = value

    @eventTarget.setter
    def eventTarget(self, value):
        """
        :param value:eventTarget
        :return:
        """
        if value is None:
            raise ValueNotFoundException('Value Was Not Found')
        self.__request['__EVENTTARGET'] = value

    @cboType.setter
    def cboType(self, value):
        """

        :param value: cbo type
        :return:
        """
        if value is None:
            raise ValueNotFoundException('Value Was Not Found')
        self.__request['ctl00$cboType'] = value

    @eventValidator.setter
    def eventValidator(self, value):
        """

        :param value:event Validator
        :return:
        """
        if value is None:
            raise ValueNotFoundException('Value Was Not Found')
        self.__request['__EVENTVALIDATION'] = value

    @viewState.setter
    def viewState(self, value):
        """

        :param value: view state
        :return:
        """
        if value is None:
            raise ValueNotFoundException('Value Was Not Found')
        self.__request['__VIEWSTATE'] = value

    @viewStateGenerator.setter
    def viewStateGenerator(self, value):
        """

        :param value: view state generator
        :return:
        """
        if value is None:
            raise ValueNotFoundException('Value Was Not Found')
        self.__request['__VIEWSTATEGENERATOR'] = value

    @hiddenField.setter
    def hiddenField(self, value):
        """

        :param value: hidden field
        :return:
        """
        if value is None:
            raise ValueNotFoundException('Value Was Not Found')
        self.__request['ctl00_ScriptManager1_HiddenField'] = value

    @btnLogin.setter
    def btnLogin(self, value):
        """

        :param value: button login
        :return:
        """
        if value is None:
            raise ValueNotFoundException('Value Was Not Found')
        self.__request['ctl00$ContentPlaceHolder1$btnlogin'] = value
