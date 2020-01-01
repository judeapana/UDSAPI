from udsapi.exceptions import ValueNotFound


class Headers:
    __request = {}

    def __init__(self):
        self.__request['ctl00$cboType'] = ''
        self.__request['__EVENTARGUMENT'] = ''
        self.__request['__EVENTTARGET'] = ''
        self.__request['__VIEWSTATEENCRYPTED'] = ''
        self.__request['ctl00$ContentPlaceHolder1$btnlogin'] = ''
        self.__request['Accept'] = ""
        self.__request['User-Agent'] = ""
        self.__request['Content-Type'] = ""
        self.__request['ctl00$ContentPlaceHolder1$txtStudentID'] = ''
        self.__request['ctl00$ContentPlaceHolder1$txtPassword'] = ''
        self.__request['__EVENTVALIDATION'] = ''
        self.__request['__VIEWSTATE'] = ''
        self.__request['__VIEWSTATEGENERATOR'] = ''
        self.__request['ctl00_ScriptManager1_HiddenField'] = ''

    @property
    def btnlogin(self):
        return self.__request['ctl00$ContentPlaceHolder1$btnlogin']

    @property
    def event_validator(self):
        return self.__request['__EVENTVALIDATION']

    @property
    def view_state(self):
        return self.__request['__VIEWSTATE']

    @property
    def view_state_generator(self):
        return self.__request['__VIEWSTATEGENERATOR']

    @property
    def hidden_field(self):
        return self.__request['ctl00_ScriptManager1_HiddenField']

    @property
    def request_header(self):
        return self.__request

    @property
    def password(self):
        return self.__request['ctl00$ContentPlaceHolder1$txtPassword']

    @property
    def username(self):
        return self.__request['ctl00$ContentPlaceHolder1$txtStudentID']

    @property
    def event_target(self):
        return self.__request['__EVENTTARGET']

    @property
    def cbo_type(self):
        return self.__request['ctl00$cboType']

    @username.setter
    def username(self, value):
        if value is None:
            raise ValueNotFound('Value Was Not Found')
        self.__request['ctl00$ContentPlaceHolder1$txtStudentID'] = value

    @password.setter
    def password(self, value):
        if value is None:
            raise ValueNotFound('Value Was Not Found')
        self.__request['ctl00$ContentPlaceHolder1$txtPassword'] = value

    @event_target.setter
    def event_target(self, value):
        if value is None:
            raise ValueNotFound('Value Was Not Found')
        self.__request['__EVENTTARGET'] = value

    @cbo_type.setter
    def cbo_type(self, value):
        if value is None:
            raise ValueNotFound('Value Was Not Found')
        self.__request['ctl00$cboType'] = value

    @event_validator.setter
    def event_validator(self, value):
        if value is None:
            raise ValueNotFound('Value Was Not Found')
        self.__request['__EVENTVALIDATION'] = value

    @view_state.setter
    def view_state(self, value):
        if value is None:
            raise ValueNotFound('Value Was Not Found')
        self.__request['__VIEWSTATE'] = value

    @view_state_generator.setter
    def view_state_generator(self, value):
        if value is None:
            raise ValueNotFound('Value Was Not Found')
        self.__request['__VIEWSTATEGENERATOR'] = value

    @hidden_field.setter
    def hidden_field(self, value):
        if value is None:
            raise ValueNotFound('Value Was Not Found')
        self.__request['ctl00_ScriptManager1_HiddenField'] = value

    @btnlogin.setter
    def btnlogin(self, value):
        if value is None:
            raise ValueNotFound('Value Was Not Found')
        self.__request['ctl00$ContentPlaceHolder1$btnlogin'] = value
