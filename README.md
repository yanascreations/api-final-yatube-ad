# API Final Yatube

API для социальной сети Yatube. Позволяет работать с публикациями, группами, комментариями и подписками.

## Запуск проекта

```bash
git clone 
cd api-final-yatube-ad
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd yatube_api
python manage.py migrate
python manage.py runserver
