# OriAwwwards

## A Description of the WebApplication.

## Table of Content

+ [Description](#description)
+ [Behaviour Driven Development](#behaviour-driven-development)
+ [Installation Requirement](#Installation)
+ [Technology Used](#technology-used)
+ [Reference](#reference)
+ [Licence](#licence)
+ [Authors Info](#authors-info)
+ [Live Link](#live-link)

## Description

<p>This is an awwwards clone like website where users can view,search and rate projects and their details posted by other users.</p>

## Behaviour Driven Development

<p>

* A user can View posted projects and their details.
* A user can post a project to be rated/reviewed.
* As user can Rate/ review other users' projects.
* A user can search for projects.
* A user can View projects overall score
* A user can view my profile page.

</p>

***
## Installation

* Open Terminal `ctrl+Alt+T`

* Git clone https://github.com/RichieOrito/OriAwwwards.git

or

* Git fork - Enter into your own repository and search-https://github.com/RichieOrito/OriAwwwards then click on fork to add
it on your own repository.

 Navigate into the cloned project. 
`cd oriawwwards`


* Create and activate the vitual Environment and install the from requirements.txt
`$ python3.8 -m virtualenv virtual`
`$ source virtual/bin/activate`
`$ pip install -r requirements.txt`

* Setting up environment variables

Create an `.env` and add the following.
```
SECRET_KEY='<Secret_key>'
DBNAME='<DbName>'
USER='<Username>'
PASSWORD='<password>'
DEBUG=True
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS='.localhost','.herokuapp.com','127.0.0.1'
DISABLE_COLLECTSTATIC=1

```

requirements from 
---
```
$ python3 -m venv env
$ . env/bin/activate
$ pip install -r requirements.txt

```
Perform a migration
```
python3 manage.py migrate

```


* Start the Server to run the app
* `$ python3 manage.py runserver`

* Open [localhost:8000](#)
***


### Requirements

* Either a computer,phone,tablet or an Ipad

* An access to the Internet

* Python3

* Postgres

* virtualenv

*Pip

[Go Back to the top](#OriAwwwards)

## Technology Used

* HTML 5 - which was used to build the structure of the pages.

* CSS - which was used to style the pages incuding the left aside navigation bar.

* Figma-which was used to design the prototype of the UI.

* Python/Flask - Which was used to build the web-applications and interactivity

* Postgresql - For the database

* Heroku - For deployment

## Reference

* LMS
* W3schools
* stackOverFlow

[Go Back to the top](#OriAwwwards)

## Licence

MIT License

Copyright (c) [2022](#licence) [Richard Orito](#licence)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Go Back to the top](#OriAwwwards)

## Authors Info

Slack Profile - [Richard Omondi](https://app.slack.com/client/T0101L740P4/C010GLANY3A/user_profile/U02EZFHEJUA)

Linked - [Richard Orito](https://www.linkedin.com/in/richie-orito/)

Gmail - [richard.omondi@student.moringaschool.com]()

Github - [RICHIE ORITO](https://github.com/RichieOrito)

## Live Link

LiveLink- [Gh-pages](https://origram.herokuapp.com/)

[Go Back to the top](#OriAwwwards)