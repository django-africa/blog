release: python manage.py makemigrations blogApi
release: python manage.py migrate blogApi
release: python manage.py makemigrations
release: python manage.py migrate
release: python manage.py collectstatic

web: gunicorn blogApiProject.wsgi