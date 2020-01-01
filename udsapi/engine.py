import requests
from bs4 import BeautifulSoup


class FetchEngine:
    def __init__(self):
        self.__session = requests.Session()

    @property
    def session(self):
        return self.__session

    @staticmethod
    def soup(request):
        soup_obj = BeautifulSoup(request.content, features='html.parser')
        return soup_obj

    def get(self, url, session=True):
        try:
            res = self.__session.get(url)
            if session:
                return res
            return self.soup(res)
        except ConnectionError:
            return None

    def post(self, url, data, session=True):
        try:
            res = self.__session.post(url, data)
            if session:
                return res
            return self.soup(res)
        except ConnectionError:
            return None
