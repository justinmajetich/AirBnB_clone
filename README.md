# AirBnB clone - MySQL

The main aim of this project is to integrate MySQL database into the AirBnB clone application. This helps the backend engineer switch between file storage and database storage.


## What is MySQL?

MySQL is the world’s most popular open source database. According to DB-Engines, MySQL ranks as the second-most-popular database, behind Oracle Database. MySQL powers many of the most accessed applications, including Facebook, Twitter, Netflix, Uber, Airbnb, Shopify, and Booking.com.

Since MySQL is open source, it includes numerous features developed in close cooperation with users over more than 25 years. So it’s very likely that your favorite application or programming language is supported by MySQL Database.

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


<summary>Alternative Syntax: Another way of using the console commands</summary>

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

</details>


<details>
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

## Co-Authors
Members who modified original codebase
*	Ebube Gideon - <onwutaebubegideon1555@gmail.com>
	> [School](https://www.alxafrica.com)
