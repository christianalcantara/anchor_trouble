# Anchon Loans selective process

### Introduction to the problems

* The resolution must be a web application.
* There must be a way to supply the application with the input data via text file that will be uploaded.
* The application must run.
* The code needs to be hosted in your GitHub account.
* You need to host the application in a server of your choice and give us a link to access and use the application.
* You should provide sufficient evidence that your solution is complete by, as a minimum, indicating that it works correctly against the supplied.

### Demonstration

* Download [data.txt](https://raw.githubusercontent.com/christianalcantara/anchor_trouble/master/data.txt).
* [Click here](http://146.148.56.51/anchorloans#problem) to acces site demonstration.
* Select data.txt file and click in submit button.

### VPS

```
**Performs**           in Google Compute Engine
**Operational System** Debian 8
**Package Contents**   Django 1.10.1
                       Git 2.7.4
                       Apache 2.4.23
                       MySQL 5.5.51
                       Nodejs 6.5.0
                       OpenSSL 1.0.2h
                       PostgreSQL 9.5.4
                       Python 2.7.12
                       SQLite 3.7.15.1
                       Subversion 1.9.4
```

### Download project

**Option 01** Clone repository

If git is not installed

```
$ sudo apt-get install git
```

after installing git

```
$ git clone https://github.com/christianalcantara/anchor_trouble.git
```

**Option 02** Download zip file

```
$ wget https://github.com/christianalcantara/anchor_trouble/archive/master.zip
$ unzip master.zip
```

### The development server

Install Django

```
$ sudo pip install django
```

Let’s verify your Django project works. Change into the outer **project directory**, if you haven’t already, and run the following commands:

```sh
$ python manage.py runserver
```

You’ll see the following output on the command line:

```sh
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

September 17, 2016 - 15:50:53
Django version 1.10, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```