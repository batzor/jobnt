# jobnt
Job wiki

# PostgreSQL database setup

Use following information:

	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': 'jobnt',
		'USER': 'admin', 
		'PASSWORD': 'admin',
		'HOST': '127.0.0.1',
	    }
	}

## Step by step instructions

**NOTE:** Following assumes you have superuser called `postgres`. Change it accordingly.

1. Create user `admin`:

		createuser -U postgres admin

2. Give permission to create databases and change password to `'admin'`:

		# Run psql as superuser
		psql -U postgres

		# Give createdb permission to admin
		alter user admin createdb;

		# Change password for admin to 'admin' (without single-quotes)
		alter user admin with password 'admin';

3. Create database `jobnt`:

		createdb -U admin jobnt