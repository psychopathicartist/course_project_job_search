from src.saver import JSONSaver
from src.user_interface import *


def user_interaction():
    """
    Функция для взаимодействия с пользователем
    """

    # Получение параметров поиска от пользователя
    search_query = input("Введите поисковый запрос: ")
    print("Поиск можно произвести на:\n 1 - HeadHunter\n 2 - SuperJob\n 3 - Обе платформы")
    user_platform_choice = input("На какой платформе производить поиск: ")

    # Получение списка вакансий по запросу пользователя
    vacancies_from_platform = get_vacancies_from_platform(user_platform_choice, search_query)
    if not vacancies_from_platform:
        print("По введенному запросу нет вакансий")
    else:
        # Сохранение результатов поиска в файл
        file_name = input("Введите название файла, куда будет сохранен результат поиска: ")
        json_saver = JSONSaver(f'{file_name}.json')

        # Создание списка из экземпляров класса вакансий и его сортировка
        vacancies_list = save_vacancies(json_saver, vacancies_from_platform)
        sorted_vacancies = sorted(vacancies_list, reverse=True)

        # Возможные действия по сортировке и фильтрации для пользователя
        while True:
            interaction = input("Выберите дальнейшее действие:\n 1 - Показать топ вакансий по зарплате \n "
                                "2 - Отсортировать вакансии по зарплате\n 3 - Отфильтровать вакансии по минимальной "
                                "зарплате\n 4 - Отфильтровать вакансии по городу\n 5 - Завершить работу\n")
            if interaction == '1':
                print_top_vacancies(sorted_vacancies)
            elif interaction == '2':
                print_sorted_vacancies(sorted_vacancies)
            elif interaction == '3':
                minimum_salary = int(input("Введите минимальную желаемую зарплату: "))
                salary_filtered_vacancies = json_saver.get_vacancies_by_salary(minimum_salary)
                print_filtered_vacancies(salary_filtered_vacancies)
            elif interaction == '4':
                town_name = input("Введите город: ")
                town_filtered_vacancies = json_saver.get_vacancies_by_town(town_name)
                print_filtered_vacancies(town_filtered_vacancies)
            elif interaction == '5':
                break
            else:
                print("Введите существующий код операции:\n 1 - Показать топ вакансий по зарплате \n "
                      "2 - Отсортировать вакансии по зарплате\n 3 - Отфильтровать вакансии по минимальной "
                      "зарплате\n 4 - Отфильтровать вакансии по городу\n 5 - Завершить работу")


if __name__ == "__main__":
    user_interaction()
