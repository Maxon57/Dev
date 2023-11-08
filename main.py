from database import PostgresDB
from download_data import download_data

from queryies import create_table_employees, get_employees

Postgres = PostgresDB(
    user='postgres',
    password='postgres',
    host='localhost',
    port='5432',
    database='postgres'
)


def main():
    try:
        with Postgres as db:
            cursor = db.connection.cursor()

            cursor.execute(create_table_employees)  # Создание таблицы employees
            db.commit()  # Фиксация транзакции

            download_data(cursor)  # Загрузка тестовых данных
            db.commit()

            while True:
                user_input = input("Введите идентификатор сотрудника: ")

                if user_input.lower() == 'выход':
                    break  # Завершение программы
                elif user_input.isdigit():
                    cursor.execute(get_employees, (int(user_input),))
                    result = cursor.fetchall()

                    if result:
                        print("Результат выборки:", [result[0] for result in result])
                    else:
                        print("Запись с указанным номером не найдена.")
                else:
                    print("Введите число или 'выход'.")

    except Exception as err:
        print(f'Возникла ошибка: {err}')
        raise


if __name__ == '__main__':
    main()
