# tortoise_test
Этот репозиторий — небольшая песочница для изучения работы с Tortoise ORM и инструментом миграций Aerich в асинхронных Python-приложениях.

### Цели репозитория:
- Разобраться, как подключать Tortoise ORM и описывать модели
- Научиться работать с Aerich: инициализация, миграции, обновления схемы
- Показать простые CRUD-операции на асинхронном Python
- Дать ясные пошаговые инструкции для начинающих

### Используемые технологии:
- Python 3.11+
- Tortoise ORM
- Aerich
- Poetry
- PostgreSQL
- pgAdmin

### 🚀 Первые шаги

1. Создание виртуального окружения и установка зависимостей
```
python3 -m venv .venv
source .venv/bin/activate  
.venv\Scripts\activate # Windows
```

*У меня всегда какие-то фокусы с окружением, поэтому потом в Python Interpreter указываю путь к .venv*

2. Установка зависимостей через Poetry
```
pip install poetry
```
3. Инициализация проекта:
```
poetry init
```
4. Добавление необходимых пакетов:
```
poetry add fastapi "tortoise-orm[asyncpg]" aerich
```
*[asyncpg] — это дополнительный пакет для поддержки PostgreSQL.*

5. Установка dev-зависимостей (по желанию):
```
poetry add --group dev uvicorn
```

*Рекомендация: 
если используете PyCharm в левой вкладке Commit 
во View Options всегда ставьте Group By Directory,
в .gitignore раскоментируйте .idea/ на GitHub 
эта папка не должна уходить*


### 🧃 Пишем CRUD для лавки с соком

##### 1. Описываем модель

Папка app в ней models и в файлах по логике распределяем классы для моделек.
Обратная связь и related_name как в Django.

##### 2. Настройка Tortoise
Пока что всё в файле main.py, 
как с этим работать, пока не ясно.

##### 3. Инициализация Tortoise
```
poetry run aerich init -t app.main.TORTOISE_ORM
```
Появилась папка migrations
```
poetry run aerich init-db
```
В папке migrations создалась папка models с первой миграцией

##### 4. Команды с Aerich
Создание миграций на основе моделей:
```
poetry run aerich migrate
```
Применить миграции к БД:
```
poetry run aerich upgrade
```

##### 5. Запуск FastAPI
```
poetry run uvicorn app.main:app --reload
```
Переходим в /docs и тестируем CRUD над соками.

*Для работы с соками надо создать 
хотя бы одного поставщика для FK*