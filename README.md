# AirBnB Clone (V2)

For the original AirBNB clone project, visit [this repository](https://github.com/justinmajetich/AirBnB_clone).

This version (created by [Ryan](https://github.com/donaldrs01) and [Luke](https://github.com/lukeschula)) has expanded on this original project by implementing a more advanced console as well as creating a new database storage engine utilizing MYSQL and SQLAlchemy. 

The finalized product can toggle between a file storage engine and a database storage engine depending on the user's needs. This is done through the verification of **environmental variables**.

When an instance of any class is created, the console will check to see if the variable HBNB_TYPE_STORAGE is set to *"db"* (database) or *"file"* (file storage). 

If the variable is set to 'db', all objects will be stored and retrieved from a connected database accessed through SQLAlchemy. If the variable is set to 'file', a file storage system will be used that serialzies an object as a JSON file when it is ready to be stored and deserializes it when it is ready to be retrieved. 

## Usage
To begin, the console can be called by running a basic Python command in the terminal:
```python
>>> ./console.py
```
You know you have successfully opened the console when you are greeted with the following prompt: 
```
(hbnb)
```
Upon opening the console, the user has a number of different commands that can be run directly from the CLI. A list of available commands is below:
### Console Commands
- **create()** --> creates an object of any class with specified parameters

- **show()** --> shows a printout of object-specific information
    (including its class name, its UUID, and its time of creation / last updated)

- **destroy()** --> removes an object from storage based on its class and UUID

- **all()** --> shows all objects of a specified class 
    (shows all objects in storage if no class is specified)

- **count()** --> prints the current number of class instances

- **update()** --> allows user to update a certain object with new information based on object's class name and UUID

- **quit() / EOF** --> exits out of console interface

## Examples
### Creating a 'Place' object with no other attributes
Usage : *create <class_name>*
```
(hbnb) create Place

db1a66c3-84af-4006-96db-f8257d3bf84f
```
### Creating a 'State' object with a name attribute
Usage: *create <class_name> <name="...">*<br>
Note that: 
1. If the attribute is a string, it must be inserted with double quotes from the command line.
2. Any spaces in the string are represented with  __ 
```
(hbnb) create State name="New_Testico"

03049433-44d0-4485-ac48-88531a06f7d9
```
### Show description of 'Place' object
Usage: *show <class_name> < id>*
```
(hbnb) show Place db1a66c3-84af-4006-96db-f8257d3bf84f

[Place] (db1a66c3-84af-4006-96db-f8257d3bf84f) {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x7f60d0ea29b0>, 
'id': 'db1a66c3-84af-4006-96db-f8257d3bf84f', 'created_at': datetime.datetime(2024, 2, 27, 16, 22, 58, 886623),
'updated_at': datetime.datetime(2024, 2, 27, 16, 22, 58, 886633)}
```
### Display all objects of specific class in storage
Usage:  *all <class_name>*
```
(hbnb) all State

["[State] (59e71503-fd84-4e33-a0cf-6f05af11b78b) {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x7f89550ce9b0>, 'id': '59e71503-fd84-4e33-a0cf-6f05af11b78b', 'created_at': datetime.datetime(2024, 2, 27, 16, 44, 25, 647616), 'updated_at': datetime.datetime(2024, 2, 27, 16, 44, 25, 647642), 'name': 'Testlahoma'}",

"[State] (03049433-44d0-4485-ac48-88531a06f7d9) {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x7f89531ad4e0>, 'id': '03049433-44d0-4485-ac48-88531a06f7d9', 'created_at': datetime.datetime(2024, 2, 27, 16, 49, 30, 426291), 'updated_at': datetime.datetime(2024, 2, 27, 16, 49, 30, 426300), 'name': 'New Testico'}"]
```
### Display all objects in storage
Usage:  *all* (with no class name provided)
```
(hbnb) all

["[User] (8efafb1e-d473-4042-bcd1-064d052a64e2) {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x7fd8eaf949d0>, 'id': '8efafb1e-d473-4042-bcd1-064d052a64e2', 'created_at': datetime.datetime(2024, 2, 27, 16, 4, 54, 257599), 'updated_at': datetime.datetime(2024, 2, 27, 16, 4, 54, 257633)}",

"[User] (7e9919c1-5396-4f81-a3bc-aea3541849b4) {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x7fd8eaf25510>, 'id': '7e9919c1-5396-4f81-a3bc-aea3541849b4', 'created_at': datetime.datetime(2024, 2, 27, 16, 8, 13, 798403), 'updated_at': datetime.datetime(2024, 2, 27, 16, 8, 13, 798411)}",

"[Place] (9ed60a26-3f67-4549-8bb5-ce52ae4a8c77) {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x7fd8eaf27d00>, 'id': '9ed60a26-3f67-4549-8bb5-ce52ae4a8c77', 'created_at': datetime.datetime(2024, 2, 27, 16, 8, 23, 207165), 'updated_at': datetime.datetime(2024, 2, 27, 16, 8, 23, 207175)}", 

"[Place] (db1a66c3-84af-4006-96db-f8257d3bf84f) {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x7fd8eaf27f70>, 'id': 'db1a66c3-84af-4006-96db-f8257d3bf84f', 'created_at': datetime.datetime(2024, 2, 27, 16, 22, 58, 886623), 'updated_at': datetime.datetime(2024, 2, 27, 16, 22, 58, 886633)}", 

"[State] (59e71503-fd84-4e33-a0cf-6f05af11b78b) {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x7fd8eaf26230>, 'id': '59e71503-fd84-4e33-a0cf-6f05af11b78b', 'created_at': datetime.datetime(2024, 2, 27, 16, 44, 25, 647616), 'updated_at': datetime.datetime(2024, 2, 27, 16, 44, 25, 647642), 'name': 'Testlahoma'}", 

"[State] (be79504c-7419-400d-b06c-38ccf862800c) {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x7fd8eaf94670>, 'id': 'be79504c-7419-400d-b06c-38ccf862800c', 'created_at': datetime.datetime(2024, 2, 27, 16, 49, 6, 847556), 'updated_at': datetime.datetime(2024, 2, 27, 16, 49, 6, 847570)}", 

"[State] (03049433-44d0-4485-ac48-88531a06f7d9) {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x7fd8eaf94a30>, 'id': '03049433-44d0-4485-ac48-88531a06f7d9', 'created_at': datetime.datetime(2024, 2, 27, 16, 49, 30, 426291), 'updated_at': datetime.datetime(2024, 2, 27, 16, 49, 30, 426300), 'name': 'New Testico'}"]
```
### Update the attributes of an object
Usage:   *update <class_name> < id> <attribute_name>=<attribute_value>...*<br>
Note that: 
1. If the attribute is a string, it must be inserted with double quotes from the command line.
2. Any spaces in the string are represented with  __ 
```
(hbnb) create User

12999f2c-0dca-4945-9142-00106678b34a

(hbnb) update User 12999f2c-0dca-4945-9142-00106678b34a first_name="Pierre", last_name="DuBois"

(hbnb) show User 12999f2c-0dca-4945-9142-00106678b34a

[User] (12999f2c-0dca-4945-9142-00106678b34a) {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x7fbf5cfb2e00>, 'id': '12999f2c-0dca-4945-9142-00106678b34a', 'created_at': datetime.datetime(2024, 2, 27, 17, 29, 0, 9011), 'updated_at': datetime.datetime(2024, 2, 27, 17, 29, 43, 835523), 'first_name="Pierre",': 'last_name="DuBois"'}
```
### Delete an object from storage
Usage:   *destroy <class_name> < id>*
```
(hbnb) create User

f9431502-8a48-46b8-91a1-6588cf0acfc2

(hbnb) all User

["[User] (f9431502-8a48-46b8-91a1-6588cf0acfc2) {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x7fb82899ee00>, 'id': 'f9431502-8a48-46b8-91a1-6588cf0acfc2', 'created_at': datetime.datetime(2024, 2, 27, 17, 3, 55, 133211), 'updated_at': datetime.datetime(2024, 2, 27, 17, 3, 55, 133229)}"]

(hbnb) destroy User f9431502-8a48-46b8-91a1-6588cf0acfc2

(hbnb) all User

[]
```