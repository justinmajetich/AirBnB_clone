<center> <h1>HBNB - The Console</h1> </center>

This project focuses on updating The Console to allow storage abstraction using MySQL & SQLAlchemy!!!!

---

<center><h3>Repository Contents by Project Task</h3> </center>

| Tasks | Files | Description |
| ----- | ----- | ------ |
| Authors/README File | [AUTHORS](https://github.com/GunterPearson/AirBnB_clone_v2/AUTHORS) | Project authors: Gunter Pearson, Corbin Enterline |
| 0: Fork me if you can! | N/A | Initial repo is forked successfully |
| 1: Unit Testing | [/tests](https://github.com/GunterPearson/AirBnB_clone_v2/tests) | Unittests! |
| 2. Console improvements | [console.py](https://github.com/GunterPearson/AirBnB_clone_v2/console.py) | Update `def do_create(self, arg):` to allow for object creation with given parameters. |
| 3. MySQL setup development | [setup_mysql_dev.sql](https://github.com/GunterPearson/AirBnB_clone_v2/setup_mysql_dev.sql) | Script that prepares a MySQL server for the project. |
| 4. MySQL setup test | [setup_mysql_test.sql](https://github.com/GunterPearson/AirBnB_clone_v2/setup_mysql_test.sql) | Script that prepares a test user & db for the project. |
| 5. Delete object | [models/engine/file_storage.py](https://github.com/GunterPearson/AirBnB_clone_v2/models/engine/file_storage.py) | Add `def delete(self, obj=None):` to delete `obj` from `__objects` if it's still inside. Update `def all`. |
| 6. DBStorage - States & Cities | [models/base_model.py](https://github.com/GunterPearson/AirBnB_clone_v2/models/base_model.py) | Change storage engine & use SQLAlchemy. |
| 7. DBStorage - User | [models/user.py](https://github.com/GunterPearson/AirBnB_clone_v2/models/user.py) | Update `User`. |
| 8. DBStorage - Place | [models/place.py](https://github.com/GunterPearson/AirBnB_clone_v2/models/place.py) | Update `Place`. |
| 9. DBStorage - Review | [models/review.py](https://github.com/GunterPearson/AirBnB_clone_v2/models/review.py) | Update `Review`. | 
| 10. DBSTorage - Amenity... and BOOM! | [models/amenity.py](https://github.com/GunterPearson/AirBnB_clone_v2/models/amenity.py) Update `Amenity`. |
<br>
<br>
<center> <h2>Lessons Learned</h2> </center>
* What is Unit testing & how to implement it in a large project.
* What is `*args` & how to use it.
* What is `**kwargs` & how to use it.
* How to handle named arguments in a function.
* How to create a MySQL database.
* How to create a MySQL user & grant it privileges.
* What ORM means.
* How to map a Python Class to a MySQL table.
* How to handle 2 different storage engines with the same codebase.
* How to use environment variables.


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
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)                   
```
###### Example 1: Show an object
Usage: show <class_name> <_id>

```
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)  
```
###### Example 2: Destroy an object
Usage: destroy <class_name> <_id>
```
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)   
```
###### Example 3: Update an object
Usage: update <class_name> <_id>
```
(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)
```
<h3>Alternative Syntax</h3>

###### Example 0: Show all User objects
Usage: <class_name>.all()
```
(hbnb) User.all()
["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92071), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92056)}", "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

###### Example 1: Destroy a User
Usage: <class_name>.destroy(<_id>)
```
(hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 2: Update User (by attribute)
Usage: <class_name>.update(<_id>, <attribute_name>, <attribute_value>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 3: Update User (by dictionary)
Usage: <class_name>.update(<_id>, <dictionary>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'name': 'Fred the Frog', 'age': 9, 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
<br>
