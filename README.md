---
<h1 align="center">0x02. AirBnB clone</h1>
<p align="center">MySQL.</p>

![N|Solid](https://github.com/jdrestre/pictures-holberton-projects/blob/master/AirBnB_clone_v2_MySQL/hbnb_logo.png)

---
## Description Project

![N|Solid](https://github.com/jdrestre/pictures-holberton-projects/blob/master/AirBnB_clone_v2_MySQL/mapping_project_mysql_airbnb-hbnb_step2.png)

---
## General
- What is Unit testing and how to implement it in a large project
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function
- How to create a MySQL database
- How to create a MySQL user and grant it privileges
- What ORM means
- How to map a Python Class to a MySQL table
- How to handle 2 different storage engines with the same codebase
- How to use environment variables

---
## Diagram Class
This diagram shows the relationship between all the classes created:

![N|Solid](https://github.com/jdrestre/pictures-holberton-projects/blob/master/AirBnB_clone_v2_MySQL/AirBnb_DB_diagrammclasses.jpg)


---
## How to start it
### FileStorage

The default mode.

In `FileStorage` mode, every time the backend is initialized, HolbertonBnB
instantiates an instance of `FileStorage` called `storage`. The `storage`
object is loaded/re-loaded from any class instances stored in the JSON file
`file.json`. As class instances are created, updated, or deleted, the
`storage` object is used to register corresponding changes in the `file.json`.

### DBStorage

Run by setting the environmental variables `HBNB_TYPE_STORAGE=db`.

In `DBStorage` mode, every time the backend is initialized, HolbertonBnB
instantiates an instance of `DBStorage` called `storage`. The `storage` object
is loaded/re-loaded from the MySQL database specified in the environmental variable
`HBNB_MYSQL_DB`, using the user `HBNB_MYSQL_USER`, password `HBNB_MYSQL_PWD`, and
host `HBNB_MYSQL_HOST`. As class instances are created, updated, or deleted, the
`storage` object is used to register changes in the corresponding MySQL database.
Connection and querying is achieved using SQLAlchemy.

Note that the databases specified for `DBStorage` to connect to must already be
defined on the MySQL server. This repository includes scripts
[setup_mysql_dev.sql](./setup_mysql_dev.sql) and [setup_mysql_test.sql](./setup_mysql_test.sql)
to set up `hbnb_dev_db` and `hbnb_test_db` databases in a MySQL server,
respectively.


### Console
The console is a command line interpreter that permits management of the backend
of HolbertonBnB. It can be used to handle and manipulate all classes utilized by
the application (achieved by calls on the `storage` object defined above).

---
## How to use it

### Using the Console

The HolbertonBnB console can be run both interactively and non-interactively.
To run the console in non-interactive mode, pipe any command(s) into an execution of the file `console.py` at the command line.

```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
$
```

Alternatively, to use the HolbertonBnB console in interactive mode, run the file `console.py` by itself:

```
$ ./console.py
```

While running in interactive mode, the console displays a prompt for input:

```
$ ./console.py
(hbnb)
```

To quit the console, enter the command `quit`, or input an EOF signal
(`ctrl-D`).

```
$ ./console.py
(hbnb) quit
$
```

```
$ ./console.py
(hbnb) EOF
$
```
---
## Examples
The HolbertonBnB console supports the following commands:

#### create
* Usage: `create <class> <param 1 name>=<param 1 value> <param 2 name>=<param 2 value> ...`
```
$ ./console.py
(hbnb) create BaseModel
119be863-6fe5-437e-a180-b9892e8746b8
(hbnb)
(hbnb) create State name="California"
(hbnb) quit
$ cat file.json ; echo ""
{"BaseModel.119be863-6fe5-437e-a180-b9892e8746b8": {"updated_at": "2019-02-17T2
1:30:42.215277", "created_at": "2019-02-17T21:30:42.215277", "__class__": "Base
Model", "id": "119be863-6fe5-437e-a180-b9892e8746b8"}, {'id': 'd80e0344-63eb-43
4a-b1e0-07783522124e', 'created_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 
842160), 'updated_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 842235), 'name
': 'California'}}
```
#### show
* Usage: `show <class> <id>` or `<class>.show(<id>)`

Prints the string representation of a class instance based on a given id.

```
$ ./console.py
(hbnb) create User
1e32232d-5a63-4d92-8092-ac3240b29f46
(hbnb)
(hbnb) show User 1e32232d-5a63-4d92-8092-ac3240b29f46
[User] (1e32232d-5a63-4d92-8092-ac3240b29f46) {'id': '1e32232d-5a63-4d92-8092-a
c3240b29f46', 'created_at': datetime.datetime(2019, 2, 17, 21, 34, 3, 635828), 
'updated_at': datetime.datetime(2019, 2, 17, 21, 34, 3, 635828)}
(hbnb)
(hbnb) User.show(1e32232d-5a63-4d92-8092-ac3240b29f46)
[User] (1e32232d-5a63-4d92-8092-ac3240b29f46) {'id': '1e32232d-5a63-4d92-8092-a
c3240b29f46', 'created_at': datetime.datetime(2019, 2, 17, 21, 34, 3, 635828), 
'updated_at': datetime.datetime(2019, 2, 17, 21, 34, 3, 635828)}
(hbnb)
```
#### all
* Usage: `all` or `all <class>` or `<class>.all()`

Prints the string representations of all instances of a given class. If no
class name is provided, the command prints all instances of every class.

```
$ ./console.py
(hbnb) create BaseModel
fce2124c-8537-489b-956e-22da455cbee8
(hbnb) create BaseModel
450490fd-344e-47cf-8342-126244c2ba99
(hbnb) create User
b742dbc3-f4bf-425e-b1d4-165f52c6ff81
(hbnb) create User
8f2d75c8-fb82-48e1-8ae5-2544c909a9fe
(hbnb)
(hbnb) all BaseModel
["[BaseModel] (450490fd-344e-47cf-8342-126244c2ba99) {'updated_at': datetime.da
tetime(2019, 2, 17, 21, 45, 5, 963516), 'created_at': datetime.datetime(2019, 2
, 17, 21, 45, 5, 963516), 'id': '450490fd-344e-47cf-8342-126244c2ba99'}", "[Bas
eModel] (fce2124c-8537-489b-956e-22da455cbee8) {'updated_at': datetime.datetime
(2019, 2, 17, 21, 43, 56, 899348), 'created_at': datetime.datetime(2019, 2, 17,
21, 43, 56, 899348), 'id': 'fce2124c-8537-489b-956e-22da455cbee8'}"]
(hbnb)
(hbnb) User.all()
["[User] (8f2d75c8-fb82-48e1-8ae5-2544c909a9fe) {'updated_at': datetime.datetim
e(2019, 2, 17, 21, 44, 44, 428413), 'created_at': datetime.datetime(2019, 2, 17
, 21, 44, 44, 428413), 'id': '8f2d75c8-fb82-48e1-8ae5-2544c909a9fe'}", "[User] 
(b742dbc3-f4bf-425e-b1d4-165f52c6ff81) {'updated_at': datetime.datetime(2019, 2
, 17, 21, 44, 15, 974608), 'created_at': datetime.datetime(2019, 2, 17, 21, 44,
15, 974608), 'id': 'b742dbc3-f4bf-425e-b1d4-165f52c6ff81'}"]
(hbnb)
(hbnb) all
["[User] (8f2d75c8-fb82-48e1-8ae5-2544c909a9fe) {'updated_at': datetime.datetim
e(2019, 2, 17, 21, 44, 44, 428413), 'created_at': datetime.datetime(2019, 2, 17
, 21, 44, 44, 428413), 'id': '8f2d75c8-fb82-48e1-8ae5-2544c909a9fe'}", "[BaseMo
del] (450490fd-344e-47cf-8342-126244c2ba99) {'updated_at': datetime.datetime(20
19, 2, 17, 21, 45, 5, 963516), 'created_at': datetime.datetime(2019, 2, 17, 21,
45, 5, 963516), 'id': '450490fd-344e-47cf-8342-126244c2ba99'}", "[User] (b742db
c3-f4bf-425e-b1d4-165f52c6ff81) {'updated_at': datetime.datetime(2019, 2, 17, 2
1, 44, 15, 974608), 'created_at': datetime.datetime(2019, 2, 17, 21, 44, 15, 97
4608), 'id': 'b742dbc3-f4bf-425e-b1d4-165f52c6ff81'}", "[BaseModel] (fce2124c-8
537-489b-956e-22da455cbee8) {'updated_at': datetime.datetime(2019, 2, 17, 21, 4
3, 56, 899348), 'created_at': datetime.datetime(2019, 2, 17, 21, 43, 56, 899348
), 'id': 'fce2124c-8537-489b-956e-22da455cbee8'}"]
(hbnb)
```
---
## Testing :straight_ruler:
Command used for unittest:

```
$ python3 unittest -m discover tests
```

Or you can specify a single test file:

```
$ python3 unittest -m tests/test_console.py
```


---
## Task Project
---
File Name|Task Name|Task Description
---|---|---
[AirBnB_clone_v2](https://github.com/monoprosito/AirBnB_clone_v2)|0. Fork me if you can!|Repository for project AirBnB-clone MySQL
[AirBnB_clone_v2](https://github.com/monoprosito/AirBnB_clone_v2/tree/master/tests)|1. Bug free!|unittest files
[console.py](https://github.com/monoprosito/AirBnB_clone_v2/blob/master/console.py), [models/](https://github.com/monoprosito/AirBnB_clone_v2/tree/master/models), [tests/](https://github.com/monoprosito/AirBnB_clone_v2/tree/master/tests)|2. Console improvements|Update the def do_create(self, arg): function of your command interpreter (console.py) to allow for object creation with given parameters
[setup_mysql_dev.sql](https://github.com/monoprosito/AirBnB_clone_v2/blob/master/setup_mysql_dev.sql)|3. MySQL setup development|Write a script that prepares a MySQL server for the project
[setup_mysql_test.sql](https://github.com/monoprosito/AirBnB_clone_v2/blob/master/setup_mysql_test.sql)|4. MySQL setup test|Write a script that prepares a MySQL server for the project
[models/engine/file_storage.py](https://github.com/monoprosito/AirBnB_clone_v2/blob/master/models/engine/file_storage.py)|5. Delete object|Update FileStorage: (models/engine/file_storage.py)
[models/base_model.py](https://github.com/monoprosito/AirBnB_clone_v2/blob/master/models/base_model.py), [models/city.py](https://github.com/monoprosito/AirBnB_clone_v2/blob/master/models/city.py), [models/state.py](https://github.com/monoprosito/AirBnB_clone_v2/blob/master/models/state.py), [models/engine/db_storage.py](https://github.com/monoprosito/AirBnB_clone_v2/blob/master/models/engine/db_storage.py), [models/__init__.py](https://github.com/monoprosito/AirBnB_clone_v2/blob/master/models/__init__.py)|6. DBStorage - States and Cities|It’s time to change your storage engine and use SQLAlchemy
[models/user.py](https://github.com/monoprosito/AirBnB_clone_v2/blob/master/models/user.py)|7. DBStorage - User|Update User: (models/user.py)
[models/place.py](https://github.com/monoprosito/AirBnB_clone_v2/blob/master/models/place.py), [models/user.py](https://github.com/monoprosito/AirBnB_clone_v2/blob/master/models/user.py), [models/city.py](https://github.com/monoprosito/AirBnB_clone_v2/blob/master/models/city.py)|8. DBStorage - Place|Update Place: (models/place.py)
[models/review.py](https://github.com/monoprosito/AirBnB_clone_v2/blob/master/models/review.py), [models/user.py](https://github.com/monoprosito/AirBnB_clone_v2/blob/master/models/user.py), [models/place.py](https://github.com/monoprosito/AirBnB_clone_v2/blob/master/models/place.py)|9. DBStorage - Review|Update Review: (models/review.py)
[models/amenity.py](https://github.com/monoprosito/AirBnB_clone_v2/blob/master/models/amenity.py), [models/place.py](https://github.com/monoprosito/AirBnB_clone_v2/blob/master/models/place.py)|10. DBStorage - Amenity... and BOOM!|Update Amenity: (models/amenity.py)


---
## Authors

- Santiago Arboleda L. [@msarboledal](https://twitter.com/msarboledal)
- Juan David Restrepo Z. [@jdrestre](https://twitter.com/jdrestre)
- Miranda Evans miranda.r.evans@gmail.com
- Kevin Yook kevin.yook@holbertonschool.com



![N|Solid](https://www.holbertonschool.com/holberton-logo.png) ![N|Solid](https://intranet.hbtn.io/assets/holberton-logo-coral-27055cb2f875eb10bf3b3942e52a24581bc0667695bdc856d4f08b469b678000.png)
