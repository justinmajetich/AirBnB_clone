# AirBnB Clone Project

## Project Description

Welcome to the AirBnB clone project! This project involves building a command interpreter to manage AirBnB objects. The first step is to create a Python package with a command interpreter using the `cmd` module.

## Command Interpreter

The command interpreter allows you to:

- Create a new object (e.g., User, Place).
- Retrieve an object from a file, a database, etc.
- Perform operations on objects (count, compute stats, etc.).
- Update attributes of an object.
- Destroy an object.

## Getting Started

To start the command interpreter, run the `console.py` script:

```bash
$  python3 console.py
```
And to Use non-interactively e.g :
```bash
echo "all" | ./console.py
```
## How to Use
Once the command interpreter is running, you can use the following commands:

- create: Creates a new instance of a specified class.
- show: Prints the string representation of an instance based on class name and ID.
- destroy: Deletes an instance based on class name and ID.
- all: Prints all string representations of instances based on class name.
- update: Updates an instance by adding or updating an attribute.
### Examples
```bash
$  python3 console.py
(hbnb) create ModelName
(hbnb) show ModelName 1234-5678-9101
(hbnb) destroy ModelName 1234-5678-9101
(hbnb) all
(hbnb) update ModelName 1234-5678-9101 email "newemail@example.com"
```
### Authors
- Khalfani Khalfan
- Ken Onyoni
