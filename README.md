# Set up

1) install `make`;
2) install node.js;
3) install yarn

The easiest way is using choco packet manager:

1) install choco: `Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))`
2) `choco install make`
3) `choco install -y nodejs`
4) `choco install yarn`

# Run

To start an app you need to open two terminals and run `make run_backend` and `make run_frontend` in each of those.

# Dependecies

You would need to install `pip3 install django djangorestframework django-cors-headers`

# Use

Run command starts two server for server and for frontend. Admin panel is available at `localhost:8080` while main app user interface is available at `localhost:3000` (frontend). Any AJAX requests made from localhost:3000 will be automatically redirected to `localhost:8000`.
