"""

Application Exceptions To Intercept

"""


class ValueNotFoundException(Exception):
    """
    Exception when value is not found
    """
    pass


class SignInFailedException(Exception):
    """
    Sign In Failed Exceptions
    """
    pass


class RequestFailedException(BaseException):
    """
    Request Failed Exception
    """
    pass


class DoubleRequestException(Exception):
    """
    Double Request Exception on Login
    """
    pass


class ResultsIndexNotFound(ValueError):
    """
    Value Of Results Not Found
    """
    pass


class ResultsNotFoundException(Exception):
    """
    Results Not Found Exceptions
    """
    pass
