FROM python:3.8

# ------------------------
# SSH Server support
# ------------------------
RUN apt-get update \
    && apt-get install -y --no-install-recommends openssh-server \
    && echo "root:Docker!" | chpasswd
COPY sshd_config /etc/ssh/

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
ADD src /code/
RUN pip install -r requirements.txt
ADD . /code/

ADD dist /dist

COPY init.sh /usr/local/bin/

RUN chmod u+x /usr/local/bin/init.sh

EXPOSE 2222 5000
