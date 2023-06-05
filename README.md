# AirBnB_clone - The console


This major aim of this project is to deploy on a server a simple copy of the [AirBnB website](https://www.airbnb.com). It consists of the following:

*	A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
*	A website (the front-end) that shows the final product to everybody: static and dynamic
*	A database or files that store data (data = objects)
*	An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## The Console
It is the command line interpreter that enables data model creation. Using the console, one can manage (``create``, ``update``, ``destroy``, etc) objects. The console equally facilitates the storage of objects to a JSON file and their subsequent reuse.

It equally employs the help of a powerful storage system that gives an abstraction between objects and how they are stored and persisted. This means: from the console code (the command interpreter) and from the front-end and RestAPI, one won't have to pay attention to how objects are stored anymore. This abstraction will help one to change the type of storage easily without updating all of the codebase.

The console will be a tool to validate this storage engine.

## Usage:

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



<details>

<summary>Execution: How to use the console</summary>

The console could work like this in the interactive mode:

	$ ./console.py
	(hbnb) help

	Documented commands (type help <topic>):
	========================================
	EOF help quit

	(hbnb)
	(hbnb)
	(hbnb) quit
	$

But also in non-interactive mode:

	$ echo "help" | ./console.py
	(hbnb)

	Documented commands (type help <topics>):
	=========================================
	EOF help quit
	(hbnb)
	$
	$ cat test_help
	help
	$
	$ cat test_help | ./console.py
	(hbnb)

	Documented commands (type help <topics>):
	=========================================
	EOF help quit
	(hbnb)
	$

</details>

<details>

<summary>Commands: Available commands for manipulating objects</summary>

* **create** - create an object
```
Usage: create <class name>
```

* **show** - display an object based on class name and id
```
Usage: show <class name> <id>
```

* **destroy** - destroy an object and totally remove it from storage
```
Usage: destroy <class name> <id>
```

* **all** - display all objects based on class name or not
```
Usage(0): all
Usage(1): all <class name>
```

* **update** - update an object based on class name and id
```
Usage: update <class name> <id> <attribute> "<attribute value>"
```

* **reset** - Delete all objects and clear the storage
```
Usage: reset
```

* **quit/EOF** - exit the console
```
Usage(0): quit
Usage(1): <CTRL + D>
```

* **help** - see description of commands
```
Usage: help
```

</details>

<details>


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

<summary>Supported classes: The classes for objects</summary>

* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

</details>

## Web Static
This houses the HTML application and template of each object

## MySQL storage
The MySQL storage will replace the file storage by a Database storage. It will map the models to a table in database using O.R.M.

## Web framework - templating
This is were we create the web server in Python. We will make static HTML file dynamic by using objects in a file or database

## RESTful API
This goal of this sub-project is to expose all the objects stored via a JSON web interface and manipulate these objects via a RESTful API

## Web dynamic
With knowledge in JQuery, we will load objects from the client side using our own RESTful API

## Authors
*	Ebube Gideon - [@holbertonschool.com](onwutaebubegideon1555@gmail.com)
*	Lukman Asinmi - @holbertonschool.com
