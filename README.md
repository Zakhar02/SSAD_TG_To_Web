# Run

To start an app you need to open two terminals and run `make run_backend` and `make run_frontend` in each of those.

# Dependecies

You would need to install `pip3 install django djangorestframework django-cors-headers`

# Use

Run command starts two server for server and for frontend. Admin panel is available at `localhost:8080` while main app user interface is available at `localhost:3000` (frontend). Any AJAX requests made from localhost:3000 will be automatically redirected to `localhost:8000`.
