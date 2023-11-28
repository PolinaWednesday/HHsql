from src.utils import get_employers, create_db, create_tables, fill_db
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

    database_name = 'hh'
    params = config()

    create_db(database_name, params)
    create_tables(database_name, params)
    fill_db(get_employers(companies), database_name, params)

    db_manager = DBManager(database_name, params)