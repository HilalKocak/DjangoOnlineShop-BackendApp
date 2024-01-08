# Order Management API
## Overview
Online Shop API enables users to add, delete, and update orders. Developed using Django REST Framework and tested with Postman.

## Setup
### Clone the project to your local machine:
```git clone https://github.com/HilalKocak/DjangoOnlineShop-BackendApp```

### Create your virtual environment
`virtualenv venv`

### Install dependencies
`pip install -r requirements.txt`

### Create superuser
`python manage.py createsuperuser`

### Make migration
`python manage.py makemigrations`
`python manage.py migrate`

### Run the application
`python manage.py runserver`

### Enter the admin panel with your superuser account
http://127.0.0.1:8000/admin

### Check API with Swagger
http://127.0.0.1:8000/swagger/schema/

### Check file in assets in project root to see POSTMAN collection 
assets/backend.json

