# *AirBnB clone - The console*

![img](https://camo.githubusercontent.com/a0c52a69dc410e983b8c63fa4aa57e83cb4157cd/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3236332f4842544e2d68626e622d46696e616c2e706e67)

### ***First step**: Write a command interpreter to manage your AirBnB objects.*

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

*Each task is linked and will help you to:*

- put in place a parent class (called **`BaseModel`**) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (**`User, State, City, Place…`**) that inherit from **`BaseModel`**
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

*Create your **Console***:

- Create your data model
- Manage (create, update, destroy, etc) objects via a console / command interpreter
- Store and persist objects to a file (JSON file) The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine.

![Flowchart](https://imgur.com/3rCP5Fx.png)

### *Execution*:

shell in mode interactif:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project in C):

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## **Files and Directories**:

- **`models`** directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
- **`tests`** directory will contain all unit tests.
- **`console.py`** file is the entry point of our command interpreter.
- models/base_model.py file is the base class of all our models. It contains common elements:
   - attributes: **`id, created_at`** and **`updated_at`**
   - methods: **`save()`** and **`to_json()`**
- **`models/engine`** directory will contain all storage classes (using the same prototype). For the moment you will have only one: **`file_storage.py`**.

## **Data diagram**:

![data_diagram](https://i.imgur.com/I7VURNR.jpg)

## [Contributors](AUTHORS)

- Ezra Nobrega <ezra.nobrega@outlook.com>
- Justin Majetich <justinmajetich@gmail.com>
- Kyllian Terrasson <kyllian.terrasson@holbertonstudents.com>
- Valentin Melia <valentin.melia@holbertonstudents.com>
- Hugo Chilemme <huogo.chilemme@holbertonstudents.com>
- Pauline Parmigiani <pauline.parmigiani@holbertonstudents.com>