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
### **Creating** a 'Place' object from the console
```
./console.py
(hbnb) create Place
db1a66c3-84af-4006-96db-f8257d3bf84f
(hbnb)
```
### **Show** description of 'Place' object from the console
Usage - show <class_name> <id>
```
./console.py
(hbnb) show Place db1a66c3-84af-4006-96db-f8257d3bf84f
[Place] (db1a66c3-84af-4006-96db-f8257d3bf84f) {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x7f60d0ea29b0>, 'id': 'db1a66c3-84af-4006-96db-f8257d3bf84f', 'created_at': datetime.datetime(2024, 2, 27, 16, 22, 58, 886623), 'updated_at': datetime.datetime(2024, 2, 27, 16, 22, 58, 886633)}
```
