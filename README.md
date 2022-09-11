<center> <h1>AirBnB Clone - The Console</h1> </center>

## Project Description

The Airbnb clone is one of the main projects at Holberton School, it's a long term project that we need to accomplish by building up trough a series of small modules or pieces. This project is thinking as a whole for a software developer, to learn and become a full-stack developer, gluing alltogether the infrastructure of the Airbnb from back to front, including databases, static and dynamic content, web frameworks, APIs, and web infrastructure.
The first step that we need to build is "the console" or the command interpreter, this is meant to be a tool to validate or manipulate the storage system, through the console we are gonna be able of:
* Create our data model.
* Manage (create, update, destroy, etc) objects.
* Store and persist objects to a file (JSON file)

This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”.

For the second part of the project we should build the database connection through SQLAlchemy, the ORM of Python.

Using a MySQL storage we replace the file storage (JSON file) by a Database storage and we map your models to a table in database by using an O.R.M.

---

<center><h3>Repository Contents by Project Task</h3> </center>

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0: Authors/README File | [AUTHORS](https://github.com/justinmajetich/AirBnB_clone/blob/dev/AUTHORS) | Project authors |
| 1: Pep8 | N/A | All code is pep8 compliant|
| 2: Unit Testing | [/tests](https://github.com/justinmajetich/AirBnB_clone/tree/dev/tests) | All class-defining modules are unittested |
| 3. Make BaseModel | [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Defines a parent class to be inherited by all model classes|
| 4. Update BaseModel w/ kwargs | [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Add functionality to recreate an instance of a class from a dictionary representation|
| 5. Create FileStorage class | [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) [/models/_ _init_ _.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/__init__.py) [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Defines a class to manage persistent file storage system|
| 6. Console 0.0.1 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) | Add basic functionality to console program, allowing it to quit, handle empty lines and ^D |
| 7. Console 0.1 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) | Update the console with methods allowing the user to create, destroy, show, and update stored data |
| 8. Create User class | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) [/models/user.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/user.py) | Dynamically implements a user class |
| 9. More Classes | [/models/user.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/user.py) [/models/place.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/place.py) [/models/city.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/city.py) [/models/amenity.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/amenity.py) [/models/state.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/state.py) [/models/review.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/review.py) | Dynamically implements more classes |
| 10. Console 1.0 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) | Update the console and file storage system to work dynamically with all  classes update file storage |
<br>

<center> <h2>General Use</h2> </center>

1. First clone this repository.

3. Once the repository is cloned locate the "console.py" file and run it as follows:
```
/AirBnB_clone$ ./console.py
```
4. When this command is run the following prompt should appear:
```
(hbnb)
```
5. This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.

##### Commands
    * create - Creates an instance based on given class

    * destroy - Destroys an object based on class and UUID

    * show - Shows an object based on class and UUID

    * all - Shows all objects the program has access to, or all objects of a given class

    * update - Updates existing attributes an object based on class name and UUID

    * quit - Exits the program (EOF will as well)


##### Alternative Syntax
Users are able to issue a number of console command using an alternative syntax:

	Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])
Advanced syntax is implemented for the following commands:

    * all - Shows all objects the program has access to, or all objects of a given class

	* count - Return number of object instances by class

    * show - Shows an object based on class and UUID

	* destroy - Destroys an object based on class and UUID

    * update - Updates existing attributes an object based on class name and UUID

<br>

## Console :computer:

The console is a command line interpreter that permits management of the backend
of AirBnB. It can be used to handle and manipulate all classes utilized by
the application.

### Using the Console

The AirBnB console can be run both interactively and non-interactively.
To run the console in non-interactive mode, pipe any command(s) into an execution
of the file `console.py` at the command line.
#### create
* Usage: `create <class> <param 1 name>=<param 1 value> <param 2 name>=<param 2 value> ...`

Creates a new instance of a given class. The class' ID is printed and
the instance is saved to the file `file.json`. When passing parameter key/value
pairs, any underscores contained in value strings are replaced by spaces.

```
$ ./console.py
(hbnb) create BaseModel
488ddf60-e921-4c6f-9e0a-675e22fc9ca6
(hbnb) create State name="Arizona"
6ce453a9-6e6c-4db6-9827-82eb9e0096aa
(hbnb) quit
$ cat file.json ; echo ""
{"BaseModel.488ddf60-e921-4c6f-9e0a-675e22fc9ca6": {"id": "488ddf60-e921-4c6f-
9e0a-675e22fc9ca6", "created_at": "2022-09-11T02:39:47.332511", "updated_at":
"2022-09-11T02:39:47.332577", "__class__": "BaseModel"}, "State.6ce453a9-6e6c-
4db6-9827-82eb9e0096aa": {"name": "Arizona", "created_at": "2022-09-11T02:40:
06.407700", "updated_at": "2022-09-11T02:40:06.407949", "id": "6ce453a9-6e6c-
4db6-9827-82eb9e0096aa", "__class__": "State"}}
```

#### show
* Usage: `show <class> <id>` or `<class>.show(<id>)`

Prints the string representation of a class instance based on a given id.

```
$ ./console.py
(hbnb) create User
bc060cbe-51cf-4b4e-af41-1fce7936bb50
(hbnb)  show User bc060cbe-51cf-4b4e-af41-1fce7936bb50
[User] (bc060cbe-51cf-4b4e-af41-1fce7936bb50) {'id': 'bc060cbe-51cf-4b4e-af41-1
fce7936bb50', 'created_at': datetime.datetime(2022, 9, 11, 2, 56, 49, 459184),
'updated_at': datetime.datetime(2022, 9, 11, 2, 56, 49, 459256)}
(hbnb)
```

#### destroy
* Usage: `destroy <class> <id>` or `<class>.destroy(<id>)`

Deletes a class instance based on a given id.

```
$ ./console.py
(hbnb) create State
bc4bd654-44ef-4354-b8ba-7ecf206d6dd5
(hbnb) create Place
fb9e026d-b9fb-46cb-8f6f-1f4167881bfb
(hbnb) destroy State bc4bd654-44ef-4354-b8ba-7ecf206d6dd5
(hbnb) Place destroy fb9e026d-b9fb-46cb-8f6f-1f4167881bfb
(hbnb)
(hbnb) quit
$ cat file.json ; echo ""
{}
```

#### update
* Usage: `update <class> <id> <attribute name> "<attribute value>"`

Updates a class instance based on a given id with a given key/value attribute
pair or dictionary of attribute pairs. If `update` is called with a single
key/value attribute pair, only "simple" attributes can be updated (ie. not
`id`, `created_at`, and `updated_at`).

```
$ ./console.py
(hbnb) create User
05387d4a-4160-4f40-95fd-f33153311f40
(hbnb) update User 05387d4a-4160-4f40-95fd-f33153311f40 first_name "Suraj"
(hbnb) show User 05387d4a-4160-4f40-95fd-f33153311f40
[User] (05387d4a-4160-4f40-95fd-f33153311f40) {'id': '05387d4a-4160-4f40-95fd-
f33153311f40', 'created_at': datetime.datetime(2022, 9, 11, 3, 10, 57, 979528),
'updated_at': datetime.datetime(2022, 9, 11, 3, 11, 29, 965296), 'first_name': 'Suraj'}
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
[[BaseModel] (488ddf60-e921-4c6f-9e0a-675e22fc9ca6) {'id': '488ddf60-e921-4c6f-
9e0a-675e22fc9ca6', 'created_at': datetime.datetime(2022, 9, 11, 2, 39, 47, 33
2511), 'updated_at': datetime.datetime(2022, 9, 11, 2, 39, 47, 332577)},
[BaseModel] (7b815540-54a9-4e96-a901-794a5be36bee) {'id': '7b815540-54a9-4e96-
a901-794a5be36bee', 'created_at': datetime.datetime(2022, 9, 11, 2, 43, 17,
51024), 'updated_at': datetime.datetime(2022, 9, 11, 2, 43, 17, 51087)},
[BaseModel] (8c803f8d-db39-4708-ba74-cc6c9b4a9af5) {'id': '8c803f8d-db39-4708-
ba74-cc6c9b4a9af5', 'created_at': datetime.datetime(2022, 9, 11, 2, 44, 1,
534380), 'updated_at': datetime.datetime(2022, 9, 11, 2, 44, 1, 534462)},
[BaseModel] (f2775208-56e8-4244-805f-dd575a7784e3) {'id': 'f2775208-56e8-4244-
805f-dd575a7784e3', 'created_at': datetime.datetime(2022, 9, 11, 2, 44, 19,
13274), 'updated_at': datetime.datetime(2022, 9, 11, 2, 44, 19, 13333)}]
(hbnb)
(hbnb) all
[[BaseModel] (488ddf60-e921-4c6f-9e0a-675e22fc9ca6) {'id': '488ddf60-e921-4c6f-
9e0a-675e22fc9ca6', 'created_at': datetime.datetime(2022, 9, 11, 2, 39, 47,
332511), 'updated_at': datetime.datetime(2022, 9, 11, 2, 39, 47, 332577)},
[State] (6ce453a9-6e6c-4db6-9827-82eb9e0096aa) {'name': 'Arizona', 'created_at'
: datetime.datetime(2022, 9, 11, 2, 40, 6, 407700), 'updated_at': datetime.
datetime(2022, 9, 11, 2, 40, 6, 407949), 'id': '6ce453a9-6e6c-4db6-9827-82eb9
e0096aa'}, [BaseModel] (7b815540-54a9-4e96-a901-794a5be36bee) {'id': '7b815540-
54a9-4e96-a901-794a5be36bee', 'created_at': datetime.datetime(2022, 9, 11, 2,
43, 17, 51024), 'updated_at': datetime.datetime(2022, 9, 11, 2, 43, 17, 51087)},
 [BaseModel] (8c803f8d-db39-4708-ba74-cc6c9b4a9af5) {'id': '8c803f8d-db39-4708-
 ba74-cc6c9b4a9af5', 'created_at': datetime.datetime(2022, 9, 11, 2, 44, 1, 534
 380), 'updated_at': datetime.datetime(2022, 9, 11, 2, 44, 1, 534462)}, [State]
  (7654164f-81b6-4bf5-92e8-75b89c88a55f) {'name': 'Arizona', 'created_at':
  datetime.datetime(2022, 9, 11, 2, 44, 10, 872940), 'updated_at':
  datetime.datetime(2022, 9, 11, 2, 44, 10, 873084), 'id': '7654164f-81b6-4bf5-
  92e8-75b89c88a55f'}, [BaseModel] (f2775208-56e8-4244-805f-dd575a7784e3) {'id':
   'f2775208-56e8-4244-805f-dd575a7784e3', 'created_at': datetime.datetime(2022,
   9, 11, 2, 44, 19, 13274), 'updated_at': datetime.datetime(2022, 9, 11, 2, 44,
    19, 13333)}, [State] (33e84116-9f36-4f77-a4a1-86abc5c3862c) {'id': '33e84116-
    9f36-4f77-a4a1-86abc5c3862c', 'created_at': datetime.datetime(2022, 9, 11, 2,
    44, 32, 974528), 'updated_at': datetime.datetime(2022, 9, 11, 2, 44, 32,
    974575)}, [User] (bc060cbe-51cf-4b4e-af41-1fce7936bb50) {'id': 'bc060cbe-
    51cf-4b4e-af41-1fce7936bb50', 'created_at': datetime.datetime(2022, 9, 11,
     2, 56, 49, 459184), 'updated_at': datetime.datetime(2022, 9, 11, 2, 56, 49,
      459256)}, [Place] (fb9e026d-b9fb-46cb-8f6f-1f4167881bfb) {'id': 'fb9e026d-
      b9fb-46cb-8f6f-1f4167881bfb', 'created_at': datetime.datetime(2022, 9, 11,
       3, 1, 28, 522295), 'updated_at': datetime.datetime(2022, 9, 11, 3, 1, 28,
       522343)}]
(hbnb)
```


## Testing :straight_ruler:

Unittests for the HolbertonBnB project are defined in the [tests](./tests)
folder. To run the entire test suite simultaneously, execute the following command:

```
$ python3 unittest -m discover tests
```

Alternatively, you can specify a single test file to run at a time:

```
$ python3 unittest -m tests/test_console.py
```

## Authors :black_nib:
* **Opeyemi Odebode** <[Surahj](https://github.com/surahj)>
* **Idris Zakariyau** <[Ade3146](https://github.com/Ade3164)>

