import os
from typing import List, Tuple

from database import PostgresDB
from download_data import download_data

from queryies import create_table_employees, get_employees

Postgres = PostgresDB(
    user=os.getenv('POSTGRES_USER', default='postgres'),
    password=os.getenv('POSTGRES_PASSWORD', default='postgres'),
    host=os.getenv('DB_HOST', default='localhost'),
    port=os.getenv('DB_PORT', default=5432),
    database=os.getenv('DB_NAME', default='postgres')
)


def conversion_to_response(employee_data: List[Tuple[int, str]]):
    """Преобразует список в строку."""
    office_name = ""
    employee_names = []

    for row in employee_data:
        office, name = row

        if office is None:
            office_name = name
        else:
            employee_names.append(name)

    return f"{office_name}: {', '.join(employee_names)}."


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
                        print(conversion_to_response(result))
                    else:
                        print("Запись с указанным номером не найдена.")
                else:
                    print("Введите число или 'выход'.")

    except Exception as err:
        print(f'Возникла ошибка: {err}')
        raise


if __name__ == '__main__':
    main()
