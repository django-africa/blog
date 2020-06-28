run: python manage.py makemigrations blogApi
run: python manage.py migrate blogApi
release: python manage.py makemigrations
release: python manage.py migrate

web: gunicorn blogApiProject.wsgi