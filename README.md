# AirBnB Clone - MySQL
---
## Project Description
This project is a continuation of the previous AirBnB Clone project, developed for ALX Africa as part of its software engineering program. In this iteration we use MySQL database as a storage engine and provides new functionalities like console improvements, database setup scripts, and the transition from file storage to database storage.
### Features
- Bug-free and extensive test cases using unittest module.
- Console improvements allowing object creation with given parameters.
- MySQL setup development and test scripts.
- Delete object functionality to delete obj from __objects if it’s inside.
- DBStorage using SQLAlchemy, with the transition from file storage to database storage.
- The ability to filter and search for objects using various parameters.
---
## Usage
**Clone the repository**
```
git clone https://github.com/Astro175/AirBnB_clone_v2
```
**Install MySQL database**

**Run the MySQL setup scripts to create the required databases and users**

```./setup_mysql_dev.sql``` to prepare a MySQL server for the project in development mode

```./setup_mysql_test.sql``` to prepare a MySQL server for the project in test mode

**Run the console to interact with the application**
```
./console.py
```
---
### Using the Console

**Available commands:**
- create: Creates a new object of the given class and stores it in the database
- show: Shows the string representation of an object with the given class and id
- destroy: Deletes an object with the given class and id
- all: Shows all objects in the database, or all objects of a given class
- update: Updates an attribute of an object with the given class and id

| Commands  | Description |
| ------------- | ------------- |
| ```quit```  | Quits the console  |
| ```Ctrl+D```  | Quits the console  |
| ```help``` or ```help <command>```  | Displays all commands or Displays instructions for a specific command
| ```create <class>```  | Creates a new object of the given class and stores it in the database
| ```show <class> <ID>```  | Shows the string representation of an object with the given class and id
| ```destroy <class> <ID>```  | Deletes an object with the given class and id
| ```all or all <class>```  | Shows all objects in the database, or all objects of a given class
| ```update <class> <id> <attribute name> "<attribute value>"```  | Updates an attribute of an object with the given class and id
| ```<class>.all()```  | Same as all ```<class>```
| ```<class>.count()```  | Retrieves the number of objects of a certain class
| ```<class>.show(<ID>)```  | Same as show ```<class> <ID>```
| ```<class>.destroy(<ID>)```  | Same as destroy ```<class> <ID>```
| ```<class>.update(<ID>, <attribute name>, <attribute value>```  | Same as update ```<class> <ID> <attribute name> <attribute value>```
| ```<class>.update(<ID>, <dictionary representation>)```  | Updates an objects based on a dictionary representation of attribute names and values
| ```create <Class name> <param 1> <param 2> <param 3>...```| Parameters must have the format `"<key name>= <value>"`, where the value can be a string, float or integer. This feature is only available with FileStorage engine.
 ---
## Running Tests
Run the following command to execute the tests:
```
python3 -m unittest discover tests
```
---
## Dependencies
- Python3
- MySQL
- SQLAlchemy
- Unittest
---
## Authors
**This project is a continuation of AirBnB Clone project, which was a collaborative project of students:**
- Ezra Nobrega
- Justin Majetich

**The MySQL version and DBStorage implementation was done by:**
- Jonathan Boomni
  - [GitHub](https://github.com/boomni)
  - [Email](mailto:rejoiceoye1@gmail.com)

- Astro David
  - []()
  - []()
---
## Acknowledgements
This project was developed as part of the Full-Stack Software Engineering program at [Alx School](https://www.alxafrica.com/).
