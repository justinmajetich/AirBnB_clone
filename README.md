<center> <h1>HBNB - The Console</h1> </center>

This repository contains the initial stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

---

<center><h3>Repository Contents by Project Task</h3> </center>

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0: Authors/README File | [AUTHORS](https://github.com/Scaarif/AirBnB_clone_v2/blob/master/AUTHORS) | Project authors |
| 1: Pep8 | N/A | All code is pep8 compliant|
| 2: Unit Testing | [/tests](https://github.com/Scaarif/AirBnB_clone_v2/tree/master/tests) | All class-defining modules are unittested |
| 3. Make BaseModel | [/models/base_model.py](https://github.com/Scaarif/AirBnB_clone_v2/blob/master/models/base_model.py) | Defines a parent class to be inherited by all model classes|
| 4. Update BaseModel w/ kwargs | [/models/base_model.py](https://github.com/Scaarif/AirBnB_clone_v2/blob/master/models/base_model.py) | Add functionality to recreate an instance of a class from a dictionary representation|
| 5. Create FileStorage class | [/models/engine/file_storage.py](https://github.com/Scaarif/AirBnB_clone_v2/blob/master/models/engine/file_storage.py) [/models/_ _init_ _.py](https://github.com/Scaarif/AirBnB_clone_v2/blob/master/models/engine/__init__.py) [/models/base_model.py](https://github.com/Scaarif/AirBnB_clone_v2/blob/master/models/base_model.py) | Defines a class to manage persistent file storage system|
| 6. Console 0.0.1 | [console.py](https://github.com/Scaarif/AirBnB_clone_v2/blob/master/console.py) | Add basic functionality to console program, allowing it to quit, handle empty lines and ^D |
| 7. Console 0.1 | [console.py](https://github.com/Scaarif/AirBnB_clone_v2/blob/master/console.py) | Update the console with methods allowing the user to create, destroy, show, and update stored data |
| 8. Create User class | [console.py](https://github.com/Scaarif/AirBnB_clone_v2/blob/master/console.py) [/models/engine/file_storage.py](https://github.com/Scaarif/AirBnB_clone_v2/blob/master/models/engine/file_storage.py) [/models/user.py](https://github.com/Scaarif/AirBnB_clone_v2/blob/master/models/user.py) | Dynamically implements a user class |
| 9. More Classes | [/models/user.py](https://github.com/Scaarif/AirBnB_clone_v2/blob/master/models/user.py) [/models/place.py](https://github.com/Scaarif/AirBnB_clone_v2/blob/master/models/place.py) [/models/city.py](https://github.com/Scaarif/AirBnB_clone_v2/blob/master/models/city.py) [/models/amenity.py](https://github.com/Scaarif/AirBnB_clone_v2/blob/master/models/amenity.py) [/models/state.py](https://github.com/Scaarif/AirBnB_clone_v2/blob/master/models/state.py) [/models/review.py](https://github.com/Scaarif/AirBnB_clone_v2/blob/master/models/review.py) | Dynamically implements more classes |
| 10. Console 1.0 | [console.py](https://github.com/Scaarif/AirBnB_clone_v2/blob/master/console.py) [/models/engine/file_storage.py](https://github.com/Scaarif/AirBnB_clone_v2/blob/master/models/engine/file_storage.py) | Update the console and file storage system to work dynamically with all  classes update file storage |
<br>
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
<br>
<center> <h2>Examples</h2> </center>
<h3>Primary Command Syntax</h3>

###### Example 0: Create an object
Usage: create <class_name>
```
(hbnb) create BaseModel
```
```
(hbnb) create BaseModel
c5d95ffd-31ef-4d4b-8044-3587e5e8b552
(hbnb)                   
```
###### Example 1: Show an object
Usage: show <class_name> <_id>

```
(hbnb) show BaseModel c5d95ffd-31ef-4d4b-8044-3587e5e8b552
[BaseModel] (c5d95ffd-31ef-4d4b-8044-3587e5e8b552) {'id': 'c5d95ffd-31ef-4d4b-8044-3587e5e8b552', 'created_at': datetime.datetime(2023, 1, 6, 2, 40, 38, 870941), 'updated_at': datetime.datetime(2023, 1, 6, 2, 40, 38, 870947)}
(hbnb)
```
###### Example 2: Destroy an object
Usage: destroy <class_name> <_id>
```
(hbnb) destroy BaseModel c5d95ffd-31ef-4d4b-8044-3587e5e8b552
(hbnb) show BaseModel c5d95ffd-31ef-4d4b-8044-3587e5e8b552
** no instance found **
(hbnb)   
```
###### Example 3: Update an object
Usage: update <class_name> <_id>
```
(hbnb) update BaseModel b30a1c82-ba6c-4017-b9e3-6f38f5a26abd first_name "person"
(hbnb) show BaseModel b30a1c82-ba6c-4017-b9e3-6f38f5a26abd
[BaseModel] (b30a1c82-ba6c-4017-b9e3-6f38f5a26abd) {'id': 'b30a1c82-ba6c-4017-b9e3-6f38f5a26abd', 'created_at': datetime.datetime(2023, 1, 6, 2, 47, 25, 930312), 'updated_at': datetime.datetime(2023, 1, 6, 2, 48, 5, 120693), 'first_name': 'person'}
(hbnb)
```
<h3>Alternative Syntax</h3>

###### Example 0: Show all User objects
Usage: <class_name>.all()
```
(hbnb) User.all()
["[User] (5fcc1a89-261c-4069-8d9a-721e4b2ec22c) {'id': '5fcc1a89-261c-4069-8d9a-721e4b2ec22c', 'created_at': datetime.datetime(2023, 1, 6, 2, 51, 18, 529439), 'updated_at': datetime.datetime(2023, 1, 6, 2, 51, 18, 529445)}", "[User] (5355c37a-c946-46c8-a862-8e8937fedec8) {'id': '5355c37a-c946-46c8-a862-8e8937fedec8', 'created_at': datetime.datetime(2023, 1, 6, 2, 53, 27, 945586), 'updated_at': datetime.datetime(2023, 1, 6, 2, 53, 27, 945591)}"]
```

###### Example 1: Destroy a User
Usage: <class_name>.destroy(<_id>)
```
(hbnb) User.destroy("5fcc1a89-261c-4069-8d9a-721e4b2ec22c")
(hbnb) User.all()
["[User] (5355c37a-c946-46c8-a862-8e8937fedec8) {'id': '5355c37a-c946-46c8-a862-8e8937fedec8', 'created_at': datetime.datetime(2023, 1, 6, 2, 53, 27, 945586), 'updated_at': datetime.datetime(2023, 1, 6, 2, 53, 27, 945591)}"]
```
###### Example 2: Update User (by attribute)
Usage: <class_name>.update(<_id>, <attribute_name>, <attribute_value>)
```
(hbnb) User.update("5355c37a-c946-46c8-a862-8e8937fedec8", name "Todd the Toad")
(hbnb) User.all()
["[User] (5355c37a-c946-46c8-a862-8e8937fedec8) {'id': '5355c37a-c946-46c8-a862-8e8937fedec8', 'created_at': datetime.datetime(2023, 1, 6, 2, 53, 27, 945586), 'updated_at': datetime.datetime(2023, 1, 6, 2, 57, 27, 760365), 'name': 'Todd the Toad'}"]
```
###### Example 3: Update User (by dictionary)
Usage: <class_name>.update(<_id>, <dictionary>)
```
(hbnb) User.update("5355c37a-c946-46c8-a862-8e8937fedec8", {'name': 'George the Giraffe', 'age': 50})
(hbnb) User.all()
["[User] (5355c37a-c946-46c8-a862-8e8937fedec8) {'id': '5355c37a-c946-46c8-a862-8e8937fedec8', 'created_at': datetime.datetime(2023, 1, 6, 2, 53, 27, 945586), 'updated_at': datetime.datetime(2023, 1, 6, 3, 1, 33, 743401), 'name': 'George the Giraffe', 'age': 50}"]
```
<br>
