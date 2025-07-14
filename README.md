# KPA Form Data - Backend Assignment

This project implements two REST APIs as per the assignment instructions using Django REST Framework and SQLite.

## ✅ APIs Implemented

1. `POST - http://127.0.0.1:8000/api/form_data/` - Submit form data
2. `GET  - http://127.0.0.1:8000/api/form_data/<id>/` - Retrieve form data by ID

## 🛠 Tech Stack

- Django 4.x
- Django REST Framework
- SQLite (default)

## 🚀 Setup Instructions

```bash
git clone https://github.com/GitAvinash003/API-Development-Task.git
cd kpa_assignment
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
