from udsapi.exceptions import ValueNotFoundException


class Headers:
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
        return self.__request['ctl00$ContentPlaceHolder1$btnlogin']

    @property
    def eventValidator(self):
        return self.__request['__EVENTVALIDATION']

    @property
    def viewState(self):
        return self.__request['__VIEWSTATE']

    @property
    def viewStateGenerator(self):
        return self.__request['__VIEWSTATEGENERATOR']

    @property
    def hiddenField(self):
        return self.__request['ctl00_ScriptManager1_HiddenField']

    @property
    def requestHeader(self):
        return self.__request

    @property
    def password(self):
        return self.__request['ctl00$ContentPlaceHolder1$txtPassword']

    @property
    def username(self):
        return self.__request['ctl00$ContentPlaceHolder1$txtStudentID']

    @property
    def eventTarget(self):
        return self.__request['__EVENTTARGET']

    @property
    def cboType(self):
        return self.__request['ctl00$cboType']

    @username.setter
    def username(self, value):
        if value is None:
            raise ValueNotFoundException('Value Was Not Found')
        self.__request['ctl00$ContentPlaceHolder1$txtStudentID'] = value

    @password.setter
    def password(self, value):
        if value is None:
            raise ValueNotFoundException('Value Was Not Found')
        self.__request['ctl00$ContentPlaceHolder1$txtPassword'] = value

    @eventTarget.setter
    def eventTarget(self, value):
        if value is None:
            raise ValueNotFoundException('Value Was Not Found')
        self.__request['__EVENTTARGET'] = value

    @cboType.setter
    def cboType(self, value):
        if value is None:
            raise ValueNotFoundException('Value Was Not Found')
        self.__request['ctl00$cboType'] = value

    @eventValidator.setter
    def eventValidator(self, value):
        if value is None:
            raise ValueNotFoundException('Value Was Not Found')
        self.__request['__EVENTVALIDATION'] = value

    @viewState.setter
    def viewState(self, value):
        if value is None:
            raise ValueNotFoundException('Value Was Not Found')
        self.__request['__VIEWSTATE'] = value

    @viewStateGenerator.setter
    def viewStateGenerator(self, value):
        if value is None:
            raise ValueNotFoundException('Value Was Not Found')
        self.__request['__VIEWSTATEGENERATOR'] = value

    @hiddenField.setter
    def hiddenField(self, value):
        if value is None:
            raise ValueNotFoundException('Value Was Not Found')
        self.__request['ctl00_ScriptManager1_HiddenField'] = value

    @btnLogin.setter
    def btnLogin(self, value):
        if value is None:
            raise ValueNotFoundException('Value Was Not Found')
        self.__request['ctl00$ContentPlaceHolder1$btnlogin'] = value
