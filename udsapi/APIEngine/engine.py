"""
This is the base of the web scrapper
Using Request and BeautifulSoup
"""

import requests
from bs4 import BeautifulSoup


class FetchEngine:
    def __init__(self):
        self.__session = requests.Session()

    @property
    def session(self):
        """
        Stores the session for routing within the web scrapper
        :return:session
        """
        return self.__session

    @staticmethod
    def soup(request):
        """

        :param request: request object
        :return: soup object
        """

        soup_obj = BeautifulSoup(request.content, features='html.parser')
        return soup_obj

    def get(self, url, session=True):
        """

        :param url: url to post or get from site
        :param session: if set to true will return a session or false to return BeautifulSoup object
        :return: Beautiful object or session
        """

        try:
            res = self.__session.get(url)
            if session:
                return res
            return self.soup(res)
        except ConnectionError:
            return None

    def post(self, url, data, session=True):
        """

        :param url: post url
        :param data: submit with data
        :param session: if set to true will return a session or false to return BeautifulSoup object
        :return: BeautifulSoup object or request object
        """

        try:
            res = self.__session.post(url, data)
            if session:
                return res
            return self.soup(res)
        except ConnectionError:
            return None
