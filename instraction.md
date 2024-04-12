создание проекта:

    django-admin startproject <project_name>

запуск сервера:

    python manage.py runserver

создание приложения:

    python manage.py startapp <app_name>

    сделать приложение частью проекта:
    в settings.py => INSTALLED_APPS дописываем <app_name>app

создание миграции для приложения:

    python manage.py makemigrations <app_name>

применение миграций:

    python manage.py migrate
