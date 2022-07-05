web: gunicorn gymManageSys.wsgi:application --log-level debug
python manage.py collectstatic --noinput
manage.py migrate
