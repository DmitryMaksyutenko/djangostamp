# djangostamp

djangostamp is a tool for the quick layout creation of Django projects and set up.
It can be a simple project for study the Django framework, or a project for production.
Database setting with django-environ.

## Installation

Use [git](https://git-scm.com/downloads) for downloading the copy of the repository.
```bash
git clone https://github.com/DmitryMaksyutenko/djangostamp.git
```

You can create the symbolic link for call djangostamp from anywhere in the file system.
If downloaded in home directory:
```bash
sudo ln -s ~/djangostamp/djangostamp.py /usr/local/bin/djangostamp
```

## Usage

Move to the appropriate directory or/and call the djangostamp.
```bash
cd path/to/directory
djangostamp
```

Enter from keyboard the appropriate key:

1. l - for layout creation.
* s - create the layout for study.
* r - create the layout for the production.
* a - create the layout for the application.

2. d - for database setting.
* dbms - type the database management system. (mysql, psql, ...)
* host - type the host number. (localhost, 127.0.0.1, ...)
* port - number in which the database service is listening. (3306, 5432, ...)
* database  - the database name for the connection. (dvdrental)
* username - the role name for the connection.
* password  - the role password.
