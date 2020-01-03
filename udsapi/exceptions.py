class ValueNotFoundException(Exception):
    pass


class SignInFailedException(Exception):
    pass


class RequestFailedException(BaseException):
    pass


class DoubleRequestException(Exception):
    pass


class ResultsIndexNotFound(ValueError):
    pass


class ResultsNotFoundException(Exception):
    pass
