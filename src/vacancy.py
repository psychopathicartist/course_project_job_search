class Vacancy:
    """
    Класс для работы с вакансиями
    """

    def __init__(self, name: str, url: str, salary_from: int, salary_to: int, schedule: str, town: str) -> None:
        """
        Создание экземпляра класса Vacancy
        """

        self.name = name
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.schedule = schedule
        self.town = town

    def __str__(self):
        """
        Возвращает информацию об экземпляре класса вакансии для пользователя
        """
        return f'Вакансия на должность {self.name}\nЗарплата от {self.salary_from} до {self.salary_to} рублей'

    def __lt__(self, other) -> bool:
        """
        Возвращает результат сравнения минимальной зарплаты двух экземпляров класса
        """
        return self.salary_from < other.salary_from
