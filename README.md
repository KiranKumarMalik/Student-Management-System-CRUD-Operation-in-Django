# Student Management System

This is a student management system built using **Django 4**, **HTML 5**, **CSS 3**, and **Bootstrap 5** with a **Bootswatch** theme.

# 1. Home Page (All Student Records)
![home](https://github.com/KiranKumarMalik/Student-Management-System-CRUD-Operation-in-Django/blob/49896ea91a48d986081515eb9997b37d14403767/ss/home.png)

# 2. Add Student
![add](https://github.com/KiranKumarMalik/Student-Management-System-CRUD-Operation-in-Django/blob/3e57c1d328d4bf946d6173f524399d76ea8c7c42/ss/Screenshot%202025-04-01%20120019.png)

![confirmation](https://github.com/KiranKumarMalik/Student-Management-System-CRUD-Operation-in-Django/blob/3e57c1d328d4bf946d6173f524399d76ea8c7c42/ss/Screenshot%202025-04-01%20120029.png)

# 3. View Student details
![check](https://github.com/KiranKumarMalik/Student-Management-System-CRUD-Operation-in-Django/blob/3e57c1d328d4bf946d6173f524399d76ea8c7c42/ss/Screenshot%202025-04-01%20120045.png)

![viewdetails](https://github.com/KiranKumarMalik/Student-Management-System-CRUD-Operation-in-Django/blob/3e57c1d328d4bf946d6173f524399d76ea8c7c42/ss/Screenshot%202025-04-01%20120055.png)

# 4. Update Student details
![update](https://github.com/KiranKumarMalik/Student-Management-System-CRUD-Operation-in-Django/blob/f286d41a576a3f5b1c88f214d93bf0523e97849a/ss/Screenshot%202025-04-01%20120133.png)

![confirmation](https://github.com/KiranKumarMalik/Student-Management-System-CRUD-Operation-in-Django/blob/f286d41a576a3f5b1c88f214d93bf0523e97849a/ss/Screenshot%202025-04-01%20120140.png)

# 5. Check updated details
![checkupdated](https://github.com/KiranKumarMalik/Student-Management-System-CRUD-Operation-in-Django/blob/ecff906eb307f6a337aa0289882fc4bde8d72977/ss/Screenshot%202025-04-01%20120206.png)

# 6. Delete a student record
![delete](https://github.com/KiranKumarMalik/Student-Management-System-CRUD-Operation-in-Django/blob/ecff906eb307f6a337aa0289882fc4bde8d72977/ss/Screenshot%202025-04-01%20120229.png)

# 7. Check student table
![checkstudent](https://github.com/KiranKumarMalik/Student-Management-System-CRUD-Operation-in-Django/blob/ecff906eb307f6a337aa0289882fc4bde8d72977/ss/Screenshot%202025-04-01%20120242.png)

# 8. Filter the data
![filter](https://github.com/KiranKumarMalik/Student-Management-System-CRUD-Operation-in-Django/blob/317054dcc7ff4d058f14e21ec9003ce8bfc5fc4e/ss/Screenshot%202025-04-01%20114941.png)


## Table of Contents 
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Run the application](#run-the-application)
- [Run the tests](#run-the-tests)
- [View the application](#view-the-application)
- [Copyright and License](#copyright-and-license)

## Prerequisites

Install the following prerequisites:

1. [Python 3.8-3.11](https://www.python.org/downloads/)
<br> This project uses **Django v4.2.4**. For Django to work, you must install a correct version of Python on your machine. More information [here](https://django.readthedocs.io/en/stable/faq/install.html).
2. [Visual Studio Code](https://code.visualstudio.com/download)

## Installation

### 1. Create a virtual environment

From the **root** directory, run:

```bash
python -m virtualenv virtualenv_name
```

### 2. Activate the virtual environment

From the **root** directory, run:

On macOS:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\scripts\activate
```

### 3. Install required dependencies

From the **root** directory, run:

```bash
pip install -r requirements.txt
```

### 4. Run migrations

From the **root** directory, run:

```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

### 5. Create an admin user to access the Django Admin interface

From the **root** directory, run:

```bash
python manage.py createsuperuser
```

When prompted, enter a username, email, and password.

## Run the application

From the **root** directory, run:

```bash
python manage.py runserver
```

## Run the tests

From the **root** directory, run:

```bash
python manage.py test --pattern="tests.py"

```

## View the application

Go to http://127.0.0.1:8000/ to view the application.

## Copyright and License

Copyright © 2025 Kiran Kumar Malik. Code released under the MIT license.
