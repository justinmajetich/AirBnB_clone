<h1 align="center"><b>0x02. AIRBNB CLONE - MYSQL</b></h1>
<div align="center"><code>Group project</code> <code>Python</code> <code>OOP</code> <code>Back-end</code> <code>SQL</code> <code>MySQL</code> <code>ORM</code> <code>SQLAlchemy
</code></div>

## Background Context
Environment variables will be your best friend for this project!

- `HBNB_ENV`: running environment. It can be “dev” or “test” for the moment (“production” soon!)
- `HBNB_MYSQL_USER`: the username of your MySQL
- `HBNB_MYSQL_PWD`: the password of your MySQL
- `HBNB_MYSQL_HOST`: the hostname of your MySQL
- `HBNB_MYSQL_DB`: the database name of your MySQL
- `HBNB_TYPE_STORAGE`: the type of storage used. It can be “file” (using `FileStorage`) or `db` (using `DBStorage`)


## Resources
<details>
<summary><b><a href="https://docs.python.org/3/library/cmd.html">cmd module</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>packages</b> concept page</summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://docs.python.org/3/library/unittest.html#module-unittest">unittest module</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/">args/kwargs</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://docs.sqlalchemy.org/en/13/orm/tutorial.html">SQLAlchemy tutorial</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql">How To Create a New User and Grant Permissions in MySQL</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://docs.python.org/3/library/os.html?highlight=env#os.getenv">Python3 and environment variables</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://docs.sqlalchemy.org/en/13/">SQLAlchemy</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html">MySQL 8.0 SQL Statement Syntax</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<!-- **man or help:**
- `` -->

## Learning Objectives
<details>
<summary><b><a href=" "> </a>What is Unit testing and how to implement it in a large project</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is <code>*args</code> and how to use it</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is <code>**kwargs</code> and how to use it</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to handle named arguments in a function</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to create a MySQL database</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to create a MySQL user and grant it privileges</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What ORM means</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to map a Python Class to a MySQL table</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to handle 2 different storage engines with the same codebase</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to use environment variables</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


## Requirements
<details>
<summary><b><a href=" "> </a>Python Scripts</b></summary><br>

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version `2.8.*`)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>

<details>
<summary><b><a href=" "> </a>Python Unit Tests</b></summary><br>

- Allowed editors: `vi`, `vim`, `emacs`
- All your files should end with a new line
- All your test files should be inside a folder `tests`
- You have to use the [unittest module](https://docs.python.org/3/library/unittest.html#module-unittest)
- All your test files should be python files (extension: `.py`)
- All your test files and folders should start by `test_`
- Your file organization in the tests folder should be the same as your project: ex: for `models/base_model.py`, unit tests must be in: `tests/test_models/test_base_model.py`
- All your tests should be executed by using this command: `python3 -m unittest discover tests`
- You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base_model.py`
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge cases

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>

<details>
<summary><b><a href=" "> </a>SQL Scripts</b></summary><br>

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be executed on Ubuntu 20.04 LTS using `MySQL 8.0`
- Your files will be executed with `SQLAlchemy` version `1.4.x`
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (`SELECT`, `WHERE`…)
- A `README.md` file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using `wc`

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>

<details>
<summary><b><a href=" "> </a>GitHub</b></summary><br>

There should be one project repository per group. If you clone/fork/whatever a partner’s project repository with the same name before the second deadline, you risk a 0% score.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>

## More Info
<img src="https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step2.png">

<details>
<summary><b><a href=" "> </a>Comments for your SQL file:</b></summary><br>

```
$ cat my_script.sql
-- first 3 students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>
<br>

## Tasks
<details>
<summary>

### 0. Fork me if you can!
`mandatory`
</summary>


</details>

<details>
<summary>

### 1. Bug free!
`mandatory`
</summary>


</details>

<details>
<summary>

### 2. Console improvements
`mandatory`

File: [console.py](), [models/](), [tests/]()
</summary>


</details>

<details>
<summary>

### 3. MySQL setup development
`mandatory`

File: [setup_mysql_dev.sql]()
</summary>


</details>

<details>
<summary>

### 4. MySQL setup test
`mandatory`

File: [setup_mysql_test.sql]()
</summary>


</details>

<details>
<summary>

### 5. Delete object
`mandatory`

File: [models/engine/file_storage.py]()
</summary>


</details>

<details>
<summary>

### 6. DBStorage - States and Cities
`mandatory`

File: [models/base_model.py](), [models/city.py](), [models/state.py](), [models/engine/db_storage.py](), [models/__init__.py]()
</summary>


</details>

<details>
<summary>

### 7. DBStorage - User
`mandatory`

File: [models/user.py]()
</summary>


</details>

<details>
<summary>

### 8. DBStorage - Place
`mandatory`

File: [models/place.py](), [models/user.py](), [models/city.py]()
</summary>


</details>

<details>
<summary>

### 9. DBStorage - Review
`mandatory`

File: [models/review.py](), [models/user.py](), [models/place.py]()
</summary>


</details>

<details>
<summary>

### 10. DBStorage - Amenity... and BOOM!
`mandatory`

File: [models/amenity.py](), [models/place.py]()
</summary>


</details>

