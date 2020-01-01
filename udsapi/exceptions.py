class ValueNotFound(Exception):
    pass


class SignInFailed(Exception):
    pass


class RequestFailedException(BaseException):
    pass


class DoubleRequestException(Exception):
    pass
