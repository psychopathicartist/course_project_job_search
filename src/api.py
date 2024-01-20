import os
import requests
from abc import ABC, abstractmethod


class API(ABC):

    @abstractmethod
    def get_vacancies(self, vacancy_name: str):
        pass

    @abstractmethod
    def get_main_information(self,vacancy_name: str):
        pass


class HeadHunterAPI(API):

    def get_vacancies(self, vacancy_name: str) -> list:
        hh_api_url = 'https://api.hh.ru/vacancies'
        payload = {
            'per_page': 20,
            'text': f'{vacancy_name}',
            'search_field': 'name',
            'only_with_salary': True
        }

        response = requests.get(hh_api_url, params=payload).json()
        return response['items']

    def get_main_information(self, vacancy_name: str):
        vacancies_main_info = []
        vacancies_info = self.get_vacancies(vacancy_name)
        for vacancy_info in vacancies_info:
            vacancy_main_info = {
                'name': vacancy_info['name'],
                'url': vacancy_info['alternate_url'],
                'salary_from': vacancy_info['salary']['from'],
                'salary_to': None if vacancy_info['salary']['to'] == 'null' else vacancy_info['salary']['to'],
                'schedule': vacancy_info['schedule']['name'],
                'town': vacancy_info['area']['name']
            }
            vacancies_main_info.append(vacancy_main_info)
        return vacancies_main_info


class SuperJobAPI(API):

    secret_key = os.getenv('SJ_SECRET_KEY')

    def get_vacancies(self, vacancy_name: str) -> list:
        sj_api_url = 'https://api.superjob.ru/2.0/vacancies/'
        headers = {
            'X-Api-App-Id': self.secret_key
        }
        payload = {
            'keywords': [[1], [], [f'{vacancy_name}']],
            'no_agreement': 1
        }

        response = requests.get(sj_api_url, headers=headers, params=payload).json()
        return response['objects']

    def get_main_information(self, vacancy_name: str):
        vacancies_main_info = []
        vacancies_info = self.get_vacancies(vacancy_name)
        for vacancy_info in vacancies_info:
            vacancy_main_info = {
                'name': vacancy_info['profession'],
                'url': vacancy_info['link'],
                'salary_from': vacancy_info['payment_from'],
                'salary_to': vacancy_info['payment_to'],
                'schedule': vacancy_info['type_of_work']['title'],
                'town': vacancy_info['town']['title']
            }
            vacancies_main_info.append(vacancy_main_info)
        return vacancies_main_info
