# AirBnB Clone (V2)

For the original AirBNB clone project, visit [this repository](https://github.com/justinmajetich/AirBnB_clone).

This version (created by [Ryan](https://github.com/donaldrs01) and [Luke](https://github.com/lukeschula)) has expanded on this original project by implementing a more advanced console as well as creating a new database storage engine utilizing MYSQL and SQLAlchemy. 

The finalized product can toggle between a file storage engine and a database storage engine depending on the user's needs. 

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
### *Creating* a 'Place' object from the console with no other attributes
Usage : create <class_name>
```
./console.py
(hbnb) create Place
db1a66c3-84af-4006-96db-f8257d3bf84f
(hbnb)
```
### *Creating* a named 'State' object from the console
Usage : create <class_name> <name="..."> 
(*note that the space in the name is represented with _*)
```
(hbnb) create State name="New_Testico"
03049433-44d0-4485-ac48-88531a06f7d9
```
### *Show* description of 'Place' object from the console
Usage : show <class_name> < id>
```
./console.py
(hbnb) show Place db1a66c3-84af-4006-96db-f8257d3bf84f
[Place] (db1a66c3-84af-4006-96db-f8257d3bf84f) {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x7f60d0ea29b0>, 
'id': 'db1a66c3-84af-4006-96db-f8257d3bf84f', 'created_at': datetime.datetime(2024, 2, 27, 16, 22, 58, 886623),
'updated_at': datetime.datetime(2024, 2, 27, 16, 22, 58, 886633)}
```
### Display *all* objects of specific class in storage
Usage: all <class_name>
```
./console.py
(hbnb) all State 
["[State] (59e71503-fd84-4e33-a0cf-6f05af11b78b) {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x7f89550ce9b0>, 'id': '59e71503-fd84-4e33-a0cf-6f05af11b78b', 'created_at': datetime.datetime(2024, 2, 27, 16, 44, 25, 647616), 'updated_at': datetime.datetime(2024, 2, 27, 16, 44, 25, 647642), 'name': 'Testlahoma'}", 
"[State] (03049433-44d0-4485-ac48-88531a06f7d9) {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x7f89531ad4e0>, 'id': '03049433-44d0-4485-ac48-88531a06f7d9', 'created_at': datetime.datetime(2024, 2, 27, 16, 49, 30, 426291), 'updated_at': datetime.datetime(2024, 2, 27, 16, 49, 30, 426300), 'name': 'New Testico'}"]
```