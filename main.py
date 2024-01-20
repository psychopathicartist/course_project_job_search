from src.api import HeadHunterAPI, SuperJobAPI

hh_api = HeadHunterAPI()
superjob_api = SuperJobAPI()

# Получение основной информации о вакансиях по ключевому слову
hh_vacancies = hh_api.get_main_information("Python")
superjob_vacancies = superjob_api.get_main_information("Python")
