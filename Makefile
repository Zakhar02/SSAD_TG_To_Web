
migrate_db:
	python3 manage.py migrate

run_backend:  migrate_db
	python3 manage.py runserver

install_frontend_deps:
	cd frontend && yarn

prepare_frontend: install_frontend_deps

run_frontend: prepare_frontend
	# run frontend dev server in background
	cd frontend && BROWSER=none yarn start
