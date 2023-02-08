# Event Manager

Event Manager is an API which provides functionality to make your own app.

# About and Technologies
Event Manager based on Django, using Django REST Framework. 
API provides user registration, token based authentication, and event creation Endpoints. 

# API Endpoints
Swagger endpoint:
```api/v1/swagger/```

Redoc endpoint:
```api/v1/redoc```

App using [Djoser](https://djoser.readthedocs.io/en/latest/getting_started.html) as authentication API.


## Installation

Clone the repository:
```git clone https://github.com/hahan18/event_manager.git```

Event Manager requires [Python 3.10](https://www.python.org/downloads/release/python-3100/) to run.

Make virtual environment using venv in project root:
```python -m venv venv```

Activate venv:
```venv\Scripts\Activate```

Update the Pip, install the requirements, make migrations and start the server.
```python -m pip install --upgrade pip```

```python -m pip install -r requirements.txt```

In project root where is manage.py file execute:
```python manage.py makemigrations``` 
then
```python manage.py migrate```

Run the server using:
```python manage.py runserver```

# Tests
To run tests in project root use:
```python manage.py test```

# Improves
Swagger/Redoc docs endpoints.
Djoser to make opportunity to create user using API.


## Docker
Will be soon...
   
   
   
