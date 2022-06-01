FROM python:3.9

WORKDIR /opt/webapp 

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y \ 
    iptables=1.8.7-1 \
    openssh-server=1:8.4p1-5 \
    nano \
    vim \
    iputils-ping
RUN echo 'root:root' | chpasswd
RUN sed -i'' -e's/^#PermitRootLogin prohibit-password$/PermitRootLogin yes/' /etc/ssh/sshd_config \
        && sed -i'' -e's/^#PasswordAuthentication yes$/PasswordAuthentication yes/' /etc/ssh/sshd_config \
        && sed -i'' -e's/^#PermitEmptyPasswords no$/PermitEmptyPasswords yes/' /etc/ssh/sshd_config \
        && sed -i'' -e's/^UsePAM yes/UsePAM no/' /etc/ssh/sshd_config
RUN update-alternatives --set iptables /usr/sbin/iptables-legacy

CMD service ssh start && /usr/local/bin/python app.py

COPY ./app.py app.py