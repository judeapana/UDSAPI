__author__ = 'Apana Jude Yinime'
"""
Class Retrieves Results Set
"""

from udsapi.APIExceptions.exceptions import ResultsIndexNotFound, ResultsNotFoundException
from udsapi.APIHeaders.headers import Headers
import json


class CourseResultSet:
    def __init__(self, auth_session):
        self.__base_url = 'https://mis.uds.edu.gh/students/coursesinformation'
        self.__fetch_eng = auth_session.get(self.__base_url, session=False)
        self.__table = None

    def parser_data(self):

        """
        retrieve data from course results set
        :return: registered course
        """

        self.__table = self.__fetch_eng.find('table', {'id': 'GridView1'})
        table = self.__table.findAll('td')
        if table is None:
            raise ResultsNotFoundException('Table Row Cant Be Found')
        registered_courses = []
        for i in range(0, len(table), 6):
            registered_courses.append(
                {'academic_year': table[i].text, 'trimester': table[i + 1].text, 'code': table[i + 2].text,
                 'title': table[i + 3].text, 'credit': table[i + 4].text, 'type': table[i + 5].text})
        return registered_courses

    def parser_data_json(self):
        """

        :return: json of registered course
        """
        return json.dumps(self.parser_data())


class TableFinalResultSet:
    """
    Retrieve Final Results Of A Trimester
    """

    def __init__(self, auth_session):
        self.__header = Headers()
        self.__auth_session = auth_session
        self.__header.eventTarget = 'btnSubmit'
        self.__base_url = 'https://mis.uds.edu.gh/students/searchresults'
        self.__fetch_eng = self.__auth_session.get(self.__base_url, session=False)
        self.__header.eventValidator = self.__fetch_eng.find('input', {'name': '__EVENTVALIDATION'}).get('value')
        self.__header.viewState = self.__fetch_eng.find('input', {'name': '__VIEWSTATE'}).get('value')
        self.__header.viewStateGenerator = self.__fetch_eng.find('input', {'name': '__VIEWSTATEGENERATOR'}).get('value')
        self.__result_labels = self.__fetch_eng.findAll('label')

    @property
    def numberOfResultsSet(self):
        """
        :return: number of final results
        """

        return len(self.__result_labels)

    @property
    def resultsNames(self):
        """
        :return: (LIST) of all available trimester results
        """

        return [i.text for i in self.__result_labels]

    def dumpResults(self, index):
        """
        :param index: index of results to retrieve
        :return: single final results
        """

        if int(index - 1) > self.numberOfResultsSet:
            raise ResultsIndexNotFound('Index Not Found')
        result_array = []
        self.__header.requestHeader[f'chkResults${index - 1}'] = 'on'
        self.__fetch_eng = self.__auth_session.post('https://mis.uds.edu.gh/students/searchresults',
                                                    data=self.__header.requestHeader, session=False)
        form_action = self.__fetch_eng.find('form').get('action')
        results_form = form_action.replace('.', '').replace('print', 'resultsform')
        search_results = self.__auth_session.get(self.__base_url.replace('/searchresults', results_form), session=False)
        results_data = search_results.find('table', {'id': 'grdCourses'})

        if results_data is None:
            raise ResultsNotFoundException('Table Row Cant Be Found')

        for td in results_data.findAll('td'):
            if 'trimester' in td.text.lower() or 'credit' in td.text.lower():
                pass
            else:
                result_array.append(td)
        results = []
        final_result = {}
        for i in range(0, len(result_array), 5):
            results.append(
                {'course_code': result_array[i].text,
                 'course_title': result_array[i + 1].text,
                 'credit_hours': result_array[i + 2].text,
                 'score': result_array[i + 3].text,
                 'grade': result_array[i + 4].text.strip()})

        final_result[results_data.findAll('td')[0].text] = results
        return final_result
