web: gunicorn gymManageSys:application --preload -b 0.0.0.0:5000 
python manage.py collectstatic --noinput
python manage.py migrate
