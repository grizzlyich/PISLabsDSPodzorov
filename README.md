# Лабораторные работы 1–9 (Python 3.14 + Django 6)

Каждая лабораторная лежит в отдельной папке.

## Запуск любого Django-проекта
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
