# AirBnb Clone - The console
This project is part of a series aimed at implementing a range of features
that collectively form a web application slated for deployment on a server.
The specific objective of this project is to develop the console feature,
functioning akin to a command interpreter capable of manipulating data without
a graphical interface, much like a shell.

## The console (command interpreter)
The console functions as a command interpreter similar to a shell but is
specifically designed for managing objects within file storage, offering
the following capabilities:
- Creating a new object (ex: a new User or a new Place)
- Retrieving an object from a file, a database, etc.
- Performing operations on objects (count, compute stats, etc.)
- Updating attributes of an object
- Destroying an object

### Starting the command interpreter
Run the Command Interpreter
./console.py

### Using the command interpreter
Creating a new user:
create User email="user@example.com" password="securepassword"

### Examples
Retrieving details of a place:
show Place 124

Updating the name of a place:
update Place 5678 name "New Place Name"

Deleting a user:
destroy User 1234