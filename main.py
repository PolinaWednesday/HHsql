from src.utils import get_employers, create_db, create_tables, fill_db, update_database_config
from config import config
from src.DBManager import DBManager

if __name__ == '__main__':
    companies = [1740,  # "Яндекс"
                 4181,  # "Банк ВТБ"
                 78638,  # "Тинькофф"
                 67611,  # "Тензор"
                 80,  # "Альфа-Банк"
                 9352463,  # "X5 Tech"
                 3529,  # "СБЕР"
                 2748,  # "Ростелеком"
                 733,  # "ЛАНИТ"
                 6093775  # "Aston"
                 ]

    print("Hello! Я скрипт для поиска вакансий в hh.ru")
    print("Введите имя базы данных: ")
    database_name = input().lower()
    update_database_config()
    params = config()
    print(f"Создаём базу данных {database_name}, пожалуйста подождите...")

    create_db(database_name, params)
    create_tables(database_name, params)
    fill_db(get_employers(companies), database_name, params)

    dbmanager = DBManager(database_name, params)

    while True:

        task = input(
            "Введите 1, чтобы получить список всех компаний и количество вакансий у каждой компании\n"
            "Введите 2, чтобы получить список всех вакансий с указанием названия компании, "
            "названия вакансии и зарплаты и ссылки на вакансию\n"
            "Введите 3, чтобы получить среднюю зарплату по вакансиям\n"
            "Введите 4, чтобы получить список всех вакансий, у которых зарплата выше средней по всем вакансиям\n"
            "Введите 5, чтобы получить список всех вакансий, в названии которых содержатся переданные в метод слова\n"
            "Введите Стоп, чтобы завершить работу\n"
        )

        if task == "Стоп":
            break
        elif task == '1':
            print(dbmanager.get_companies_and_vacancies_count())
            print()
        elif task == '2':
            print(dbmanager.get_all_vacancies())
            print()
        elif task == '3':
            print(dbmanager.get_avg_salary())
            print()
        elif task == '4':
            print(dbmanager.get_vacancies_wth_highest_salary())
            print()
        elif task == '5':
            keyword = input('Введите ключевое слово: ')
            print(dbmanager.get_vacancies_with_keyword(keyword))
            print()
        else:
            print('Неправильный запрос')
