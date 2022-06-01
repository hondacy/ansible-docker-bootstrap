## Welcome to ADB (Ansible Docker Bootstrap)

To use:
1. Clone this repository
2. run:
```shell
docker compose build
docker compose up
OR: docker compose up --build
```
**note that on older systems you need to run:**
```shell
docker-compose build
docker-compose up
```
3. Check that you have 3 containers running:
- webapp
- master
- enemy


For debuging the app container, you can run:
```shell
docker run --rm -it  --entrypoint /bin/bash webservice
```

For accessing the webapp, you can run:
```
curl webservice:8080
```