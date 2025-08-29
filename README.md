To-Do List Web Application
Описание
To-Do List Web Application — это веб-приложение для управления задачами, разработанное с использованием Django и Django REST Framework. Пользователи могут регистрироваться, 
входить в систему, создавать, редактировать, удалять задачи и отмечать их как выполненные. Интерфейс реализован с помощью Django templates и стилизован с использованием Tailwind CSS.
REST API сохранён для потенциальной интеграции с другими клиентами (например, мобильным приложением).
Проект демонстрирует навыки backend-разработки, включая работу с Django, аутентификацией, базами данных и API, а также базовую стилизацию frontend'а.
Функционал

Регистрация и аутентификация пользователей (вход, выход).
Полный CRUD для задач: создание, просмотр, редактирование, удаление.
Переключение статуса задачи (выполнено/не выполнено) через чекбокс.
Адаптивный интерфейс с Tailwind CSS.
REST API для задач (/api/tasks/) с поддержкой аутентификации.
Код размещён на GitHub с использованием Git для контроля версий.

Технологии

Backend: Python, Django, Django REST Framework, SQLite
Frontend: Django templates, Tailwind CSS (via CDN)
Инструменты: Git, GitHub

Установка

Клонируйте репозиторий:
git clone https://github.com/твой_юзернейм/practiceproject.git
cd practiceproject


Создайте и активируйте виртуальное окружение:
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\Activate.ps1  # Windows (PowerShell)


Установите зависимости:
pip install django djangorestframework django-cors-headers


Примените миграции:
python manage.py migrate


Создайте суперпользователя (для админки):
python manage.py createsuperuser


Запустите сервер:
python manage.py runserver


Откройте приложение в браузере: http://127.0.0.1:8000/.

API доступен по /api/tasks/ (требуется аутентификация).

Структура проекта

todoproject/: Настройки Django.
todo/: Приложение с моделями, views, шаблонами и API.
templates/: Django templates с Tailwind CSS.
.gitignore: Игнорирует venv/, __pycache__/, и другие ненужные файлы
