# Purpose

TG2WEB is an educational project, the main purpose of which is to pass the SSAD course and
learn something new about Software Design. However, it can be used as a web-proxy for
Telegram channels. This might be extremely useful since in many countries Telegram is banned.
Another possible use case for this project is history indexation by search engines, since by
default content in Telegram is not searchable by Google. If a content owner publishes his
channels via our project it may attract more visitors through search engines, and as a result
increase the number of visitors and possible revenue.

# Requirements

* Display and load new messages
* Make messages indexible
* Save history of searches and allow to sort them
* Inform user if content is loading
* Use REST-like URLs
* Must be convinient for mobile browsers
* Respond quickly
* Promptly load new messages
* Avoid authentification
* Be user friendly and do not require a lot installation details 

# Design

Whole system consists of three parts:

 * *frontend*. Implemented using React.js.
 * *web server*. Implemented using Django framework (Python).
 * *sync worker (bot)*. Works in background, communicates with Telegram API. Implemented using Python.<br />
## Web application behavior<br />
![Web app diagram](https://github.com/Zakhar02/SSAD_TG_To_Web/blob/master/mermaid-diagram-20210925232147.png)<br />
## Crawler(worker) behavior<br />
![Crawler diagram](https://github.com/Zakhar02/SSAD_TG_To_Web/blob/master/mermaid-diagram-20210925232941.png)

# Software Architecture 

* Django - MVC framework, backend, has powerful patterns such as models and views.
* Crawler - deamon that checks new messages and stores them in DB, implements observer pattern.

## Installation (Ubuntu)
1. Install python, pip and required packages
```shell
sudo apt install python3 python3-pip
pip3 install django djangorestframework PyTelegramBotAPI psycopg2-binary
```
2. Install Docker on your machine:
```shell
sudo snap install docker
```
## Installation (Windows)

1) install `make`;
2) install node.js;
3) install yarn
4) install Docker

The easiest way to install packets on Windows is to use choco packet manager:

1) install choco: `Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))`
2) `choco install make`
3) `choco install -y nodejs`
4) `choco install yarn`


## Running
Run Docker container with PostgreSQL in it:
```shell
docker run -p 5432:5432 --name db_container --rm -d -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -e POSTGRES_DB=tg_to_web_db postgres
```
Running server: 
```shell
python3 manage.py runserver 8000
```
Running bot:
```shell
python3 manage.py runbot
```
Killing Docker container (in case of troubles/restarts). Getting a message
*"docker rm" requires at least 1 argument* is OK.
```shell
docker stop $(docker ps -qa) && docker rm $(docker ps -qa)
```
If getting an error *'listen tcp4 0.0.0.0:5432: bind: address already in use'*
get the list of processes acquiring this port and kill them
```shell
sudo ss -lptn 'sport = :5432'
sudo kill {process id}
```
If any change was applied to models.py files, run the following:
```shell
python3 manage.py makemigrations
python3 manage.py migrate
```
## Rebuilding
When rebuilt frontend part, you should rebuild static files:
```shell
cd frontend && npm run build && python3 ../manage.py collectstatic
```

## API
```
GET /api/channels/
    Returns 10 any channels
    [{ id, title }, ...]

GET /api/channels/?autocomplete-query=text
    Returns 10 channels matching the query
    [{ id, title }, ...]

GET /api/channels/:channelId/messages?limit=N
    Return last N messages for given channelId
    [{ id, message }, ...]

GET /api/channels/:channelId/messages?limit=N&before-id=messageId
    Return N messages before given messageId
    [{ id, message }, ...]

```
