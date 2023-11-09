***
<details>
    <summary style="font-size: 16pt; font-weight: bold">Запуск проекта</summary>

1. Скачайте на свою машину репозиторий с помощи команды:
   ```git clone https://github.com/Maxon57/Dev.git```
2. Перейдите в директорию ./infra с помощи команды:
    ```cd infra```
3. Создайте файл .env и в нем пропишите:
    ```
    DB_NAME=<Имя БД>
    POSTGRES_USER=<Имя пользователя>
    POSTGRES_PASSWORD=<Пароль>
    DB_HOST=<Хост>
    DB_PORT=<Порт>
   ```
4. Выполните команду для создания и запуска контейнера.
    ```
   docker compose up -d --build
   ```

5. Перейдите в корень проекта и выполните следующие команды:
```
    cd ..
    pip install -r requirements.txt
    python main.py
    
```
</details>

## Автор
[Максим Игнатов](https://github.com/Maxon57)