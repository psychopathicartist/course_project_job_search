from src.api import HeadHunterAPI, SuperJobAPI

hh_api = HeadHunterAPI()
superjob_api = SuperJobAPI()


def get_vacancies_from_platform(user_choice: str, user_query: str) -> list:
    """
    Возвращает список вакансий с платформы, которую выбирает пользователь
    """

    vacancies_from_platform = []
    if user_choice == '1':
        vacancies_from_platform = hh_api.get_main_information(user_query)
    elif user_choice == '2':
        vacancies_from_platform = superjob_api.get_main_information(user_query)
    elif user_choice == '3':
        vacancies_from_platform = (hh_api.get_main_information(user_query) +
                                   superjob_api.get_main_information(user_query))
    else:
        print('Неверный ввод\nВведите 1 для поиска на HeadHunter, 2 - на SuperJob, 3 на обоих платформах')
    return vacancies_from_platform


def save_vacancies(saver, vacancies: list) -> list:
    """
    Возвращает лист с экземплярами класса вакансий
    """
    saver.save_vacancies(vacancies)
    vacancies_list = saver.read_vacancies()
    return vacancies_list


def print_top_vacancies(sorted_vacancies_list: list) -> None:
    """
    Выводит топ вакансий по зарплате
    """

    num_of_vacancies = len(sorted_vacancies_list)
    top_n = int(input(f"Введите количество вакансий для вывода в топ (не более {num_of_vacancies}): "))
    top_vacancies = sorted_vacancies_list[:top_n]
    for top_vacancy in top_vacancies:
        print(top_vacancy)
        print()


def print_sorted_vacancies(sorted_vacancies_list: list) -> None:
    """
    Выводит вакансии, отсортированные по зарплате
    """

    for sorted_vacancy in sorted_vacancies_list:
        print(sorted_vacancy)
        print()


def print_filtered_vacancies(filtered_vacancies_list: list) -> None:
    """
    Выводит отфильтрованные вакансии
    """

    if not filtered_vacancies_list:
        print('Вакансий с таким фильтром не найдено')
    else:
        for filtered_vacancy in filtered_vacancies_list:
            print(filtered_vacancy)
            print()
