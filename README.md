# Set up

1) install `make`;
2) install node.js;
3) install yarn

The easiest way to install packets on Windows is to use choco packet manager:

1) install choco: `Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))`
2) `choco install make`
3) `choco install -y nodejs`
4) `choco install yarn`

# Run

To start an app you need to open two terminals and run `make run_backend` and `make run_frontend` in each of those.

# Dependencies

You would need to install `pip3 install django djangorestframework django-cors-headers`

# Use

Run command starts two server for server and for frontend. Admin panel is available at `localhost:8080` while main app user interface is available at `localhost:3000` (frontend). Any AJAX requests made from localhost:3000 will be automatically redirected to `localhost:8000`.

# Purpose

TG2WEB is a web app. It works as a read-only gateway to public Telegram channels or groups. This web service might be very useful for accessing Telegram in contries where it is banned. It also makes content indexable for search engines.

# Design

Whole system consists of three parts:

 * *frontend*. Executed on client side, in browser. Implemented using React.js.
 * *web server*. Executed on back end, handles requests of the frontend. Implemented using Python, Django.
 * *sync worker*. Works in background, communicates with Telegram API, keeps messages in database up to date. Implemented using Python.

Codebase of web server and sync worker are completely separate, they exchange data through database.