# Dataset based API 📊
Simple API based on provided dataset.
___
## Technologies ⚙️⚙️⚙️
Python 3.10, Django, Django REST Framework, Docker
___
## Prerequisites
Python 3.10 + 🐍 should be installed.  
Docker 🐳 should be installed.
___
## How to run 🏃🏻

Clone repo to the desired directory:

```bash
git clone https://github.com/nsdNite/dataset_based_api.git
```

Get your django secret key here: https://djecrety.ir/  

Copy .env-sample -> .env and populate with all required data:
```text
DJANGO_SECRET_KEY=***
POSTGRES_HOST=***
POSTGRES_DB=***
POSTGRES_USER=***
POSTGRES_PASSWORD=***
```
### Example of ready .env file for test task purposes:
```text
DJANGO_SECRET_KEY="w3s)jalbit@&(fx017gccde(5vaq_8v^0fbc$en@gd2fv4xg9z"
POSTGRES_HOST=db
POSTGRES_DB=app
POSTGRES_USER=postgres_user
POSTGRES_PASSWORD=1234
```
After setup, run:
```bash
docker-compose up --build
````
Note: superuser is created automatically with .env info if no users exist in database.  
Note: data imports automatically from dataset.csv provided, it may take some time.  
Note: no credentials needed to access this API.
___
## Features ✨
- Filtering by client's favourite category, by gender, birthdate, age, age range.
- No additional modules for filtering used.
- Swagger documentation:
```html
/api/doc/swagger
```
- Importing dataset from csv via management command:
```python
python manage.py  import_dataset
```
- Auto run script to create admin user on database start:
```python
python manage.py  init_admin
```
- Auto run script to wait for  database creation in Docker
```python
python manage.py  wait_for_db
```
- Export filtered results to csv through endpoint:
```html
/api/clients/export-csv/?gender=female&category=toys
```
___
