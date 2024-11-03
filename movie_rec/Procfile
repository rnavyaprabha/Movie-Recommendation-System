release: python manage.py migrate
web: gunicorn movie_rec.wsgi --log-file -
worker: python manage.py collectstatic --noinput