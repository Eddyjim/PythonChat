# PythonChat
Jobsity Code Challenge

## Execution:
1. Start postres DB, redis and RabbitMQ
```
docker-compose up
```
2. Start bot:
``docker-compose -f docker-compose-bot.yml up `` or  ``python bot/start_bot.py``
3. Execute ``docker-compose -f  docker-compose-chat.yml up`` or `` python app/manage.py runserver 0.0.0.0:8000 ``

## Initialization
If is running for the first time the django migrations shall be executed
```
python app/manage.py migrate
```
## Super User Creation
If an admin user is required:
```
python app/manage.py createsuperuser
```
