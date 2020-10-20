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
---

1. l - for layout creation.
---
  1.1 s - create the layout for study.
  1.2 r - create the layout for the production.
  1.3 a - create the layout for the application.

2. d - for database setting.
---
  2.1 dbms - type the database management system. (mysql, psql, ...)
  2.2 host - type the host number. (localhost, 127.0.0.1, ...)
  2.3 port - number in which the database service is listening. (3306, 5432, ...)
  2.4 database  - the database name for the connection. (dvdrental)
  2.5 username - the role name for the connection.
  2.6 password  - the role password.
