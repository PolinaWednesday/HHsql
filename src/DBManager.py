import psycopg2
from config import config


class DBManager:
    def __init__(self, database_name, params=config()):
        self.database_name = database_name
        self.params = params

    def get_companies_and_vacancies_count(self):
        """ Метод для получения компаний и количества вакансий у каждой компании. """
        try:
            connection = psycopg2.connect(database=self.database_name, **self.params)
            with connection.cursor() as cursor:
                cursor.execute('SELECT company_name, COUNT(vacancy_id) '
                               'FROM companies '
                               'JOIN vacancies USING (company_id) '
                               'GROUP BY company_name;')

                rows = cursor.fetchall()
                data = "\n".join([str(row) for row in rows])

        except (Exception, psycopg2.DatabaseError) as error:
            return f'[INFO] {error}'

        connection.close()
        return data

    def get_all_vacancies(self):
        """ Метод для получения всех вакансий. """
        try:
            connection = psycopg2.connect(database=self.database_name, **self.params)
            with connection.cursor() as cursor:
                cursor.execute('SELECT title_vacancy, company_name, salary, vacancies.link '
                               'FROM vacancies '
                               'JOIN companies USING (company_id);')

                rows = cursor.fetchall()
                data = "\n".join([str(row) for row in rows])

        except (Exception, psycopg2.DatabaseError) as error:
            return f'[INFO] {error}'

        connection.close()
        return data

    def get_avg_salary(self):
        """ Метод для получения средней зарплаты. """
        try:
            connection = psycopg2.connect(database=self.database_name, **self.params)
            with connection.cursor() as cursor:
                cursor.execute('SELECT company_name, round(AVG(salary)) AS average_salary '
                               'FROM companies '
                               'JOIN vacancies USING (company_id) '
                               'GROUP BY company_name;')

                rows = cursor.fetchall()
                data = "\n".join([str(row) for row in rows])

        except (Exception, psycopg2.DatabaseError) as error:
            return f'[INFO] {error}'

        connection.close()
        return data

    def get_vacancies_wth_highest_salary(self):
        """ Метод для получения вакансий с максимальной зарплатой. """
        try:
            connection = psycopg2.connect(database=self.database_name, **self.params)
            with connection.cursor() as cursor:
                cursor.execute('SELECT * '
                               'FROM vacancies '
                               'WHERE salary > (SELECT AVG(salary) FROM vacancies);')

                rows = cursor.fetchall()
                data = "\n".join([str(row) for row in rows])

        except (Exception, psycopg2.DatabaseError) as error:
            return f'[INFO] {error}'

        connection.close()
        return data

    def get_vacancies_with_keyword(self, keyword):
        """ Метод для Поиска вакансий по ключевому слову. """
        try:
            connection = psycopg2.connect(database=self.database_name, **self.params)
            with connection.cursor() as cursor:
                cursor.execute(f"""
                SELECT * 
                FROM vacancies
                WHERE lower(title_vacancy) LIKE '%{keyword}%'
                OR lower(title_vacancy) LIKE '%{keyword}'
                OR lower(title_vacancy) LIKE '{keyword}%'""")

                rows = cursor.fetchall()
                data = "\n".join([str(row) for row in rows])

        except (Exception, psycopg2.DatabaseError) as error:
            return f'[INFO] {error}'

        connection.close()
        return data



