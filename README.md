### Django form with Ajax

To create virtual environment
```
python3 -m venv venv
```

Activate venv
```
source venv/bin/activate
```

Install requirements.txt
```
pip install -r requirements.txt
```

Run docker container for Postgresql
```
docker-compose up -d
```

Migrate
```
python3 manage.py makemigrations
python3 manage.py migrate
```
Create super user and enter your credentials
```
python3 manage.py createsuperuser
```

Run server
```
python3 manage.py runserver
```
