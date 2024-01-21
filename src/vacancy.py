class Vacancy:
    """
    Класс для работы с вакансиями
    """

    def __init__(self, name: str, url: str, salary_from: int, salary_to: int, schedule: str, town: str) -> None:
        """
        Создание экземпляра класса Vacancy
        """

        self.__name = name
        self.__url = url
        self.__salary_from = salary_from
        self.__salary_to = salary_to
        self.__schedule = schedule
        self.__town = town

    def __str__(self):
        """
        Возвращает информацию об экземпляре класса вакансии для пользователя
        """
        return f'Вакансия на должность {self.__name}\nЗарплата от {self.__salary_from} до {self.__salary_to} рублей'

    def __lt__(self, other) -> bool:
        """
        Возвращает результат сравнения минимальной зарплаты двух экземпляров класса
        """
        return self.__salary_from < other.__salary_from
