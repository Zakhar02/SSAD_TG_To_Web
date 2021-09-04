
install_frontend_deps:
	cd frontend && yarn

build_frontend:
	cd frontend && yarn build

prepare_frontend: install_frontend_deps build_frontend

migrate_db:
	python3 manage.py migrate

run: prepare_frontend migrate_db
	python3 manage.py runserver
