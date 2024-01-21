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
        return (f'Вакансия на должность {self.name}\nЗарплата от {self.salary_from} до {self.salary_to} рублей\n'
                f'{self.schedule}, город {self.town}\nСсылка на вакансию {self.url}')

    def __lt__(self, other) -> bool:
        """
        Возвращает результат сравнения минимальной зарплаты двух экземпляров класса
        """
        return self.salary_from < other.salary_from

    @property
    def name(self):
        return self.__name

    @property
    def url(self):
        return self.__url

    @property
    def salary_from(self):
        return self.__salary_from

    @property
    def salary_to(self):
        return self.__salary_to

    @property
    def town(self):
        return self.__town

    @property
    def schedule(self):
        return self.__schedule
