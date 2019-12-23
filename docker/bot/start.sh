service ssh start

pip install --pre -U -r /app/src/.meta/packages

gunicorn bot:app -c gunicorn.conf.py --reload