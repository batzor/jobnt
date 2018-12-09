# jobnt: Installation

1. Install PostgreSQL
2. Install Python dependencies
3. Set up database
4. Install Django Migrations
6. Run the server

## 1. Install PostgreSQL

Download and install [PostgreSQL](https://www.postgresql.org/download/).

## 2. Setting up Python (pip) dependencies

First of all, install all pip dependencies:

```
$ pip3 install -r requirements.txt
```

## 3. Set up database

We are using PostgreSQL as our database. PostgreSQL username, password and database are configured in `jobnt/jobnt/settings.py` as follows:

```
  DATABASES = {
    'default': {
      'ENGINE': 'django.db.backends.postgresql',
      'NAME': 'jobnt',
      'USER': 'admin', 
      'PASSWORD': 'admin',
      'HOST': '127.0.0.1',
    }
  }
```

We need to create:

* PostgreSQL user `'admin'` with password `'admin'`
* PostgreSQL database `'jobnt'`

**NOTE:** Following assumes you have **superuser** called `postgres`. (Change it accordingly.)

### Steps

1. Create user `admin`:

        $ createuser -U postgres admin

2. Give permission to create databases and change password to `'admin'`:

        # Run PSQL console as superuser
        $ psql -U postgres
        
        # Give createdb permission to admin
        postgres=#  alter user admin createdb;
        
        # Change password for admin to 'admin' (without single-quotes)
        postgres=#  alter user admin with password 'admin';

        # Quit PSQL console
        \q

3. Create database `jobnt`:

        $ createdb -U admin jobnt

## 4. Install Django Migrations

Run:

        # First, make migrations
        python manage.py makemigrations

        # Run migrations
        python manage.py migrate

(Optional, but recommended) Create a super user (to login to our application):

        # Create super-user
        python manage.py createsuperuser
        # ... enter username, password and optionally email

## 5. Seed the database (with random data)

Instead of manually entering database information, use our seeder to populate the database with fake data:

        # Seed
        python manage.py seed

## 6. Run the server

Run the server:

        python manage.py runserver

Now, go to the address shown in the output for above (usually, [localhost:8000](http://localhost:8000)) in your browser.