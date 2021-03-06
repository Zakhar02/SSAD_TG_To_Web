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
 * *sync worker*. Works in background, communicates with Telegram API. Implemented using Python.<br />
## Web application behavior<br />
https://github.com/Zakhar02/SSAD_TG_To_Web/blob/master/mermaid-diagram-20210925232147.png
## Crawler(worker) behavior<br />
https://github.com/Zakhar02/SSAD_TG_To_Web/blob/master/mermaid-diagram-20210925232941.png

## Preview<br />
![front](https://github.com/Zakhar02/SSAD_TG_To_Web/blob/master/photo_2021-09-25_23-43-32.jpg)

# Software Architecture 

* Django - MVC framework, backend, has powerful patterns such as models and views.
* Crawler - deamon that checks new messages and stores them in DB, implements observer pattern.

## More info in RUP: 
https://docs.google.com/document/d/1PvOoFsXBvledLdbXJhHEOobCbEGda6ax/edit?usp=sharing&ouid=112203852966083452669&rtpof=true&sd=true

## Project structure
A typical Django project that consists of "Tg_To_Web" folder that stores configuration settings, "backend" that is basically source code and a "frontend".

## Installation (Ubuntu)
For now, the only way to use our App - you need to install Linux. Then:
1. Install required packages using makefile
```shell
make install_all_deps
```
2. Install Docker on your machine:
```shell
sudo snap install docker
```

## Running
Run Docker container with PostgreSQL in it:
```shell
make run_database
```
Running server: 
```shell
make run_backend
```
Running frontend: 
```shell
make run_frontend
```
Running sync worker requires to provide Telegram App Id and hash. Sync worker users Telegram accounts to access the API, thus it is necessary to provide account info, such as phone number and password (asked via prompt):
```shell
export TELEGRAM_APP_ID='your app id'
export TELEGRAM_API_HASH='your api hash'
export TELEGRAM_PHONE='+80000000000'
export TELEGRAM_DATA_CRYPT_KEY='Any data, used as cryptographic seed'
make run_sync
```
Killing Docker container (in case of troubles/restarts).
```shell
make kill_database
```
If getting an error *'listen tcp4 0.0.0.0:5432: bind: address already in use'*
get the list of processes acquiring this port and kill them
```shell
sudo ss -lptn 'sport = :5432'
sudo kill {process id}
```
If any change was applied to models.py files, run the following:
```shell
make migrate_db
```
## Rebuilding
When rebuilt frontend part, you should rebuild static files:
```shell
make rebuild
```
