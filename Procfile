release: python manage.py makemigrations blogApi
release: python manage.py migrate blogApi
release: python manage.py makemigrations
release: python manage.py migrate
release: python manage.py collectstatic
 --noinput

web: gunicorn blogApiProject.wsgi