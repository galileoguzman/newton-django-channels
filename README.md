# Newton real time

## System Requirements

- Python 3.6
- Django 2.2.1
- MySql

## Dependencies

- Python 3.6
- virtualenv

### Django

    pip install -r requirements.txt

### Environment variables

	ADMIN_NAME=YOUR NAME
	ADMIN_EMAIL=name@email.com
	DATABASE_URL=mysql://USER:PASSWORD@HOST:PORT/NAME
	DEBUG=True
	SECRET_KEY=A_SUPER_SECRET_KEY
	ADD_YOUR_NEW_ENV=WITH_ITS_VALUE

## Database 

To setup database the very first time just in development:
	
	GRANT ALL PRIVILEGES ON *.* TO 'newton_development_user'@'localhost' IDENTIFIED BY 'password';
	CREATE DATABASE newton_development;


### Running migrations

To run migrations use the following command:

    ./manage migrate

## Tests

You can run the unit tests with the following command:

    ./manage test

## Linting

## Security

## Deployment Instructions

Deployment instructions can be found in `README-AWS.md` file.

## Useful Information

### Admin Panel

The Admin Panel is mounted at:

    localhost:8000/admin

### Generating Super Admin Users

There is a handy task that creates Super Admin Users, you can invoke it with:

    ./manage.py createsuperuser