FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY ./app /app/
RUN yum -y install ssh openssh-server passwd
RUN pip install --upgrade pip
RUN pip install -r /app/pip-requirements.txt
COPY ./lib_fix/django_registration/validators.py /usr/local/lib/python3.7/site-packages/django_registration/validators.py
RUN python /app/manage.py migrate

EXPOSE 22