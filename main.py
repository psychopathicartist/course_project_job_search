from src.api import HeadHunterAPI, SuperJobAPI
from src.saver import JSONSaver
from src.vacancy import Vacancy

# Получение основной информации о вакансиях по ключевому слову
hh_api = HeadHunterAPI()
superjob_api = SuperJobAPI()
hh_vacancies = hh_api.get_main_information("Python")
superjob_vacancies = superjob_api.get_main_information("Python")

# Создание экземпляра класса для работы с вакансиями
vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", 100000,
                  150000,"Полный день", "Москва")

# Сохранение информации о вакансиях в файл
json_saver = JSONSaver()
json_saver.save_vacancies(hh_vacancies)

# Добавление и удаление вакансии из файла
json_saver.add_vacancy(vacancy)
json_saver.delete_vacancy(vacancy)

# Вывод списков вакансий, отфильтрованных по городу и минимальной зарплате
print(json_saver.get_vacancies_by_salary(50000))
print(json_saver.get_vacancies_by_town('москва'))
