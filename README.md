```python
export FLASK_APP=project/__init__.py
python manage.py run
```

```s
docker-compose up -d --build
docker-compose logs
```

find which version of pip package installed.

```s
pip3 show psycopg2-binary
```

docker-machine create --driver amazonec2 \
--amazonec2-iam-instance-profile sls-admin \
--amazonec2-region us-east-1 \
--amazonec2-vpc-id vpc-01cbdb55a8dc02317 \
--amazonec2-instance-type t2.micro \
testdriven-prod

docker-machine create --driver amazonec2 \
--amazonec2-region us-east-1 \
--amazonec2-vpc-id vpc-0e05fef56372e3e1b \
--amazonec2-instance-type t2.micro \
testdriven-prod

# Microservices with Docker, Flask, and React

[![Build Status](https://travis-ci.org/moz5691/testdriven-app.svg?branch=master)](https://travis-ci.org/moz5691/testdriven-app)
