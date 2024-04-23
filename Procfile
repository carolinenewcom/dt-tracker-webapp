release: python manage.py migrate
web: gunicorn dttrackerapp.wsgi:application --log-file=-