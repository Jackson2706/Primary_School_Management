# Project:  Primary  School Management 
1. Getting Started :
- A big project in Software Engineering and Applications in HUST - Hanoi University of Science and Technology.
- An app for small and medium school, is used to manage almost of activities in a school, with framework Django (Python), PostGresQL supported.
- ADMIN (Head of department) can create and manager user account(other admin account, student account, staff or teacher account).

2. Installation Steps :
- Clone this repository, you should use a virtual environment to store your Django project’s
```shell
$ git clone https://github.com/Jackson2706/Primary_School_Management.git
$ cd Primary_School_Management
```
- Install the Django code with Pip:
```shell
$ python -m pip install Django
```
- Database: PostGresQL and change information about DATABASE in setting.py. You can use SQLite or other Database. Read docs: https://docs.djangoproject.com/en/4.1/ref/databases/ to get more informations.
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<database name>',
        'USER': '<username>',
        'PASSWORD': '<password>',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

- Using PostGresQL:
```shell
$ pip install Django psycopg2
```
- Install other dependencies:
```shell
$ pip install dj-database-url gunicorn whitenoise requests
```
3. Database :
<img src="Database.png"/>