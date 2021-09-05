PYTHON= python

migrate_db:
	$(PYTHON) manage.py migrate

run_backend:  migrate_db
	$(PYTHON) manage.py runserver

install_frontend_deps:
	cd frontend && yarn

prepare_frontend: install_frontend_deps

run_frontend: prepare_frontend
	cd frontend && yarn start
