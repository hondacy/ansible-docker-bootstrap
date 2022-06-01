FROM python:3.9

WORKDIR /opt/clients

RUN apt-get update && apt-get install -y \ 
    ansible \
    sshpass \
    && chmod 774 /opt/clients
    
ENTRYPOINT ["/bin/bash"]
