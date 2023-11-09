import json
import os

from typing import List, Dict, Union

from queryies import insert_query, check_query


def open_file_json(file: str):
    """Открывает файл на чтение и возвращает данные."""
    path = os.path.join(os.getcwd(), file)

    try:
        with open(path, 'r', encoding='UTF-8') as f:
            return json.load(f)
    except FileNotFoundError:
        raise


def download_data(cursor):
    """Вставка данных в  таблицу."""
    try:
        data: List[Dict[Union[str, int, None]]] = open_file_json('data.json')

        cursor.execute(check_query)
        count = cursor.fetchone()[0]

        if count == 0:
            cursor.executemany(insert_query,
                               list(map(lambda x: list(x.values()), data)))

    except Exception:
        raise
