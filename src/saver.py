import json
from abc import ABC, abstractmethod

from src.vacancy import Vacancy


class Saver(ABC):
    """
    Абстрактный класс для работы с сохранением вакансий
    """

    @abstractmethod
    def save_vacancies(self, vacancies: list) -> None:
        pass

    @abstractmethod
    def add_vacancy(self, vacancy) -> None:
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy) -> None:
        pass

    @abstractmethod
    def get_vacancies_by_salary(self, min_salary: int) -> list:
        pass

    @abstractmethod
    def get_vacancies_by_town(self, town: str) -> list:
        pass


class JSONSaver(Saver):
    """
    Класс для работы с сохранением вакансий в формате json
    """

    def __init__(self, file_name='vacancies.json') -> None:
        """
        Создание экземпляра класса JSONSaver
        """

        self.file_name = file_name

    @staticmethod
    def make_dict_from_vacancy(vacancy) -> dict:
        """
        Возвращает словарь из экземпляра класса вакансии
        """
        vacancy_dict = {
            'name': vacancy.__name,
            'url': vacancy.__url,
            'salary_from': vacancy.__salary_from,
            'salary_to': vacancy.__salary_to,
            'schedule': vacancy.__schedule,
            'town': vacancy.__town
        }
        return vacancy_dict

    def save_vacancies(self, vacancies: list) -> None:
        """
        Сохраняет список вакансий в json файл
        """

        with open(self.file_name, 'w', encoding='utf-8') as json_file:
            json.dump(vacancies, json_file, ensure_ascii=False, indent=4)

    def open_vacancies(self) -> list:
        """
        Возвращает список вакансий, полученный из json файла
        """

        with open(self.file_name, encoding='utf-8') as json_file:
            vacancies = json.load(json_file)
        return vacancies

    def read_vacancies(self) -> list:
        """
        Возвращает список из экземпляров класса вакансий, экземпляры
        создаются из списка, хранящегося в json файле
        """

        vacancies_list = []
        vacancies = self.open_vacancies()
        for vacancy in vacancies:
            vacancies_list.append(Vacancy(vacancy['name'], vacancy['url'], vacancy['salary_from'],
                                          vacancy['salary_to'], vacancy['schedule'], vacancy['town']))
        return vacancies_list

    def add_vacancy(self, vacancy) -> None:
        """
        Добавляет в json файл вакансию, передаваемую в виде экземпляра класса вакансий
        """

        vacancy_to_add = self.make_dict_from_vacancy(vacancy)
        vacancies_from_file = self.open_vacancies()
        vacancies_from_file.append(vacancy_to_add)
        self.save_vacancies(vacancies_from_file)

    def delete_vacancy(self, vacancy) -> None:
        """
        Удаляет из json файла вакансию, передаваемую в виде экземпляра класса вакансий
        """

        vacancy_to_del = self.make_dict_from_vacancy(vacancy)
        vacancies_from_file = self.open_vacancies()
        for vacancy_from_file in vacancies_from_file:
            if vacancy_to_del == vacancy_from_file:
                vacancies_from_file.remove(vacancy_from_file)
        self.save_vacancies(vacancies_from_file)

    def get_vacancies_by_salary(self, min_salary: int) -> list:
        """
        Возвращает список вакансий, в которых зарплата больше или равна переданной
        """

        vacancies_by_salary = []
        vacancies_from_file = self.open_vacancies()
        for vacancy_from_file in vacancies_from_file:
            if vacancy_from_file['salary_from'] >= min_salary:
                vacancies_by_salary.append(vacancy_from_file)
        return vacancies_by_salary

    def get_vacancies_by_town(self, town: str) -> list:
        """
        Возвращает список вакансий, в которых название города совпадает с переданным
        """

        vacancies_by_town = []
        vacancies_from_file = self.open_vacancies()
        for vacancy_from_file in vacancies_from_file:
            if vacancy_from_file['town'] == town.title():
                vacancies_by_town.append(vacancy_from_file)
        return vacancies_by_town
