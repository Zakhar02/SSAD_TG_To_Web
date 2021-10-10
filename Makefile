PYTHON = python3

migrate_db:
	$(PYTHON) manage.py makemigrations
	$(PYTHON) manage.py migrate

install_all_deps:
	sudo apt install python3 python3-pip
	pip3 install django djangorestframework python-telegram psycopg2-binary
	cd frontend && yarn install

run_bot: migrate_db
	$(PYTHON) manage.py runbot

run_backend: migrate_db
	$(PYTHON) manage.py runserver 8000

run_frontend:
	cd frontend && yarn start

run_database:
	docker run -p 5432:5432 --name db_container --rm -d -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -e POSTGRES_DB=tg_to_web_db postgres

kill_database:
	docker stop $(docker ps -qa) && docker rm $(docker ps -qa)

rebuild:
	cd frontend && npm run build && python3 ../manage.py collectstatic
