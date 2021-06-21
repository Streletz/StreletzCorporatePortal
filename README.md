# StreletzCorporatePortal

The corporate portal powered by Python Django.

## SYSTEM REQUIREMENTS

 - Python 3.8 or higher;
 - PostgreSQL 10 or higher.

## TO INSTALL

 - In the StreletzCorporatePortal/settings.py in the lines below, specify the data to connect to your database

```DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'corporate_portal_db',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '',
 }
}
```

 - Execute console commands:

```
cd myManagePyPath
python manage.py migrate
   ```
## HISTORY

### 1.0.0

First stable version.