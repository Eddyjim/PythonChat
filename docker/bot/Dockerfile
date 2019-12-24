FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY ./bot /app/

RUN pip install --upgrade pip
RUN pip install -r /app/pip-requirements.txt
#RUN yum -y install ssh openssh-server passw
#ENTRYPOINT ["/entry.sh"]
#EXPOSE 22
#CMD ["/usr/sbin/sshd", "-D", "-f", "/etc/ssh/sshd_config"]