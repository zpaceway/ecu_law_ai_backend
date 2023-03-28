migrate:
	python3.11 manage.py migrate

makemigrations:
	python3.11 manage.py makemigrations

create_default_superuser:
	python3.11 manage.py one_time_create_default_superuser

run:
	python3.11 manage.py runserver 0.0.0.0:9000
