from udsapi.exceptions import ResultsIndexNotFound
from udsapi.headers import Headers
import json


class CourseResultSet:
    def __init__(self, auth_session):
        self.__base_url = 'https://www.udsmis.com/students/coursesinformation'
        self.__fetch_eng = auth_session.get(self.__base_url, session=False)
        self.__table = None

    def parser_data(self):
        self.__table = self.__fetch_eng.find('table', {'id': 'GridView1'})
        table_ = self.__table.findAll('td')
        table_registered_courses = []
        for i in range(0, len(table_), 6):
            table_registered_courses.append(
                {'academic_year': table_[i].text, 'trimester': table_[i + 1].text, 'code': table_[i + 2].text,
                 'title': table_[i + 3].text, 'credit': table_[i + 4].text, 'type': table_[i + 5].text})
        return table_registered_courses

    def parser_data_json(self):
        return json.dumps(self.parser_data())


class TableFinalResultSet:
    def __init__(self, auth_session):
        self.header = Headers()
        self.__auth_session = auth_session
        self.header.event_target = 'btnSubmit'
        self.base_url = 'https://www.udsmis.com/students/searchresults'
        self._fetch_eng = self.__auth_session.get(self.base_url, session=False)
        self.header.event_validator = self._fetch_eng.find('input', {'name': '__EVENTVALIDATION'}).get('value')
        self.header.view_state = self._fetch_eng.find('input', {'name': '__VIEWSTATE'}).get('value')
        self.header.view_state_generator = self._fetch_eng.find('input', {'name': '__VIEWSTATEGENERATOR'}).get('value')
        self.result_labels = self._fetch_eng.findAll('label')

    @property
    def number_of_results_set(self):
        return len(self.result_labels)

    @property
    def results_names(self):
        return [i.text for i in self.result_labels]

    def dump_result(self, index):
        if int(index - 1) > self.number_of_results_set:
            raise ResultsIndexNotFound('Index Not Found')
        result_array = []
        self.header.request_header[f'chkResults${index-1}'] = 'on'
        self._fetch_eng = self.__auth_session.post('https://www.udsmis.com/students/searchresults',
                                                   data=self.header.request_header, session=False)
        form_action = self._fetch_eng.find('form').get('action')
        results_form = form_action.replace('.', "").replace("print", "resultsform")
        search_results = self.__auth_session.get(self.base_url.replace('/searchresults', results_form), session=False)
        results_data = search_results.find('table', {'id': 'grdCourses'})
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

    # TODO :: def dump_results(self):
    #     pass


class TableProvisionalResultSet:
    def __init__(self, auth_session):
        pass
