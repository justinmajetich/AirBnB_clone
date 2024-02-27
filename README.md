# AirBnB Clone (V2)

For the original AirBNB clone project, visit [this repository](https://github.com/justinmajetich/AirBnB_clone)

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
### Commands
```
- **create()** --> creates an object of any class with specified parameters

- **show()** --> shows a printout of object-specific information
    (including its class name, its UUID, and its time of creation / last updated)

- **destroy()** --> removes an object from storage 

- **all()** --> shows all objects of a specified class 
    (shows all objects in storage if no class is specified)

- **count()** --> prints the current number of class instances

- **update()** --> allows user to update a certain object with new information based on object's class name and UUID

- **quit() / EOF** --> exits out of console interface
```
