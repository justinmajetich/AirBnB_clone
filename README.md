# AirBnB Clone - MySQL

![Python](https://img.shields.io/badge/Python-3.8.5-blue)
![PyCodeStyle](https://img.shields.io/badge/PyCodeStyle-2.8.*-brightgreen)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4.x-red)

## Table of Contents

- [Introduction](#introduction)
- [Background Context](#background-context)
- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
  - [Python Scripts](#python-scripts)
  - [Python Unit Tests](#python-unit-tests)
  - [SQL Scripts](#sql-scripts)
  - [GitHub](#github)
- [Tasks](#tasks)
  - [0. Fork me if you can!](#0-fork-me-if-you-can)
  - [1. Bug free!](#1-bug-free)
  - [2. Console improvements](#2-console-improvements)
  - [3. MySQL setup development](#3-mysql-setup-development)
  - [4. MySQL setup test](#4-mysql-setup-test)
  - [5. Delete object](#5-delete-object)
  - [6. DBStorage - States and Cities](#6-DBStorage-\--States and Cities)
  - [7. DBStorage - User](#7-DBStorage-\--User)
  - [8. DBStorage - Place](#8-DBStorage-\--Place)
  - [9. DBStorage - Review](#9-DBStorage-\--Review)
  - [10. DBStorage - Amenity... and BOOM!](#DBStorage-\--Amenity...-and-BOOM!)

## Introduction

Welcome to the AirBnB Clone project! This is a group project written in Python, focusing on Object-Oriented Programming (OOP), back-end development, and using MySQL as a database with SQLAlchemy as the Object-Relational Mapping (ORM) tool.

### Authors
- Mohamed Ezghoudi <mohamedezghoudi@gmail.com>
- El mahdi Mouline <elmahdi.mouline@live.fr>
- Ezra Nobrega <ezra.nobrega@outlook.com>
- Justin Majetich <justinmajetich@gmail.com>

### Project Timeline
- Project Start Date: September 15, 2023, 4:00 AM
- Project End Date: September 21, 2023, 4:00 AM
- Checker Release Date: September 16, 2023, 4:00 PM
- Auto Review Launch: At the project deadline

### Important Note
Environment variables will be your best friend for this project! Make sure to set the following variables according to your development environment:

- HBNB_ENV: running environment ("dev" or "test" for now, "production" soon)
- HBNB_MYSQL_USER: MySQL username
- HBNB_MYSQL_PWD: MySQL password
- HBNB_MYSQL_HOST: MySQL hostname
- HBNB_MYSQL_DB: MySQL database name
- HBNB_TYPE_STORAGE: Type of storage used ("file" for FileStorage or "db" for DBStorage)

## Background Context

In this project, you will learn and implement various aspects of software development, including unit testing, function arguments, MySQL database creation and user management, ORM, environment variable usage, and more.

## Resources

To successfully complete this project, it's recommended to review the following resources:

- [cmd module](https://docs.python.org/3/library/cmd.html)
- [Python Packages Concept]
- [unittest module](https://docs.python.org/3/library/unittest.html)
- [*args and **kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
- [SQLAlchemy Tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
- [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
- [Python3 and Environment Variables](https://docs.python.org/3/library/os.html?highlight=env#os.getenv)
- [SQLAlchemy](https://docs.sqlalchemy.org/en/13/)
- [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)

## Learning Objectives

By the end of this project, you will be able to explain the following concepts without external help:

### General
- What is Unit testing and how to implement it in a large project
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function
- How to create a MySQL database
- How to create a MySQL user and grant it privileges
- What ORM means
- How to map a Python Class to a MySQL table
- How to handle two different storage engines with the same codebase
- How to use environment variables

### Copyright - Plagiarism
- Avoid plagiarism
- Task solutions should be original
- Do not publish any content of this project

## Requirements

### Python Scripts
- Allowed Editors: vi, vim, emacs
- Interpretation/Compilation: Ubuntu 20.04 LTS using Python 3.8.5
- File Ending: All files should end with a new line
- Shebang: The first line of all files should be exactly `#!/usr/bin/python3`
- README.md: A README.md file at the root of the project folder is mandatory
- Code Style: Use pycodestyle (version 2.8.*)
- Executability: All files must be executable
- Code Length: Code length will be tested using `wc`
- Documentation: All modules, classes, and functions should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
- Documentation Format: Documentation should be in the form of real sentences explaining the purpose of the module, class, or method

### Python Unit Tests
- Allowed Editors: vi, vim, emacs
- File Ending: All test files should end with a new line
- Test Folder: All test files should be inside a folder named "tests"
- Testing Module: Use the unittest module
- Test File Extension: All test files should be Python files with the extension .py
- Test File and Folder Naming: Test files and folders should start with "test_"
- Test File Organization: Organize test files in the same folder structure as the project
- Test Execution: Run tests using `python3 -m unittest discover tests` or test file by file using `python3 -m unittest tests/test_models/test_base_model.py`

### SQL Scripts
- Allowed Editors: vi, vim, emacs
- Execution Environment: Execute on Ubuntu 20.04 LTS using MySQL 8.0
- SQLAlchemy Version: Use SQLAlchemy version 1.4.x
- File Ending: All files should end with a new line
- SQL Query Comments: Add comments just before SQL queries
- Commented Task: Start each SQL file with a comment describing the task
- Uppercase Keywords: Use uppercase for SQL keywords (e.g., SELECT, WHERE)

### GitHub
- Repository Name: Update the repository name to "AirBnB_clone_v2"
- README.md: Update the README.md with your information but don't delete the initial authors

## Tasks

### 0. Fork me if you can! (Mandatory)

For this project you will fork this [codebase](https://github.com/justinmajetich/AirBnB_clone.git):

update the repository name to AirBnB_clone_v2
update the README.md with your information but don’t delete the initial authors
If you are the owner of this repository, please create a new repository named AirBnB_clone_v2 with the same content of AirBnB_clone

### 1. Bug free! (Mandatory)

### 2. Console improvements (Mandatory)

### 3. MySQL setup development (Mandatory)

### 4. MySQL setup test (Mandatory)

### 5. Delete object (Mandatory)

### 6. DBStorage - States and Cities (Mandatory)

### 7. DBStorage - User (Mandatory)

### 8. DBStorage - Place (Mandatory)

### 9. DBStorage - Review (Mandatory)

### 10. DBStorage - Amenity... and BOOM! (Mandatory)
