Создание веб-сайта Пиццерии на Django

Логин и пароль суперпользователя (Административной панели): 
Логин: admin
Пароль: 123

Для создания проекта неоходимо:
1. Создайте виртуальное окружение: ``` py -m venv venv ```
2. Активация виртуального окружения: ``` .\venv\Scripts\activate ```
4. Установите Django и все необходимые библиотеки: ``` pip install Django ```
5. Создайте проект: ``` django-admin startproject mysite . ``` 
6. Создайте приложение : ``` py manage.py startapp pizzaApp ```
7. Создайте необходимые миграции и примените их: ``` py manage.py makemigrations | py manage.py migrate ``` 
8. Создайте суперпользователя: ``` py manage.py createsuperuser ```
9. Запуск серверва: ``` py manage.py runserver ```

Все использованные биюлиотеки находятся в файле req.txt


Для запуска проекта необходимо:
Создать и активировать виртуальное окружение

Установить зависимости:
pip install -r req.txt

Выполнить следующие команды:

Команда для создания миграций приложения для базы данных
python manage.py migrate

Команда для запуска приложения:
python manage.py runserver

При создании моделей или их изменении необходимо выполнить следующие команды:
python manage.py makemigrations
python manage.py migrate




