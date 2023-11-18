# AirBnB_clone_v2

AirBnB clone built using the python language and Flask framework as part of the ALX projects

---

### Repository Contents

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 1: Unit Testing | [/tests](https://github.com/AllisonOge/AirBnB_clone_v2/tree/master/tests) | All class-defining modules are unittested |
| 2. BaseModel | [/models/base_model.py](https://github.com/AllisonOge/AirBnB_clone_v2/blob/master/models/base_model.py) | Defines a parent class to be inherited by all model classes|
| 3. Models (User, State, City, Amenity, Place, and Reviews) | [/models/*.py](https://github.com/AllisonOge/AirBnB_clone_v2/tree/master/models) | Data models for the AirBnB clone project. See [AirBnB_clone#sec.data-model](https://github.com/AllisonOge/AirBnB_clone/tree/main#data-model) for more details |
| 4. FileStorage | [/models/engine/file_storage.py](https://github.com/AllisonOge/AirBnB_clone_v2/blob/master/models/engine/file_storage.py) | Defines a class to manage persistent file storage system. It is instantiated in the `/models/__init__.py` file |
| 5. Console | [console.py](https://github.com/AllisonOge/AirBnB_clone_v2/blob/master/console.py) | Handles console commands for CRUD operations |

## Project design stages

1. The console project (completed - 7 days sprint)
2. Web static project (completed - 2 days sprint)
3. MySQL storage project (active - 6 days sprint)

## Console CRUD operations

Below, there is a demonstration of some commands possible with the console program. Once the user initiates the command-line interface with the prompt "(hbnb)." They explore available commands using the `help` command, which lists options like `all`, `create`, and `update`. After checking all instances (resulting in an empty list), they create a new User instance with a unique ID using the `create` command. Subsequently, they view all instances, including the newly created User. Using the `update` command, the user modifies the User instance's name attribute. Another `all` command is then used to confirm the update. Finally, the user gracefully exits the command line with the `quit` command.

```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) help all
Prints all string representation of all instances based or not on the class name

Usage: all <class name> or all

data models are: BaseModel, User, State, City, Amenity, Place, Review
(hbnb) all
[]
(hbnb) help create
Create a new instance of data models, save it (to the JSON file) and print the id

Usage: create <class name>

data models are: BaseModel, User, State, City, Amenity, Place, Review
(hbnb) create User
60b0bba8-e9af-4da0-83e3-ab0e479a5285
(hbnb) all
["[User] (60b0bba8-e9af-4da0-83e3-ab0e479a5285) {'id': '60b0bba8-e9af-4da0-83e3-ab0e479a5285', 'created_at': datetime.datetime(2023, 8, 20, 9, 12, 59, 700603), 'updated_at': datetime.datetime(2023, 8, 20, 9, 12, 59, 700623)}"]
(hbnb) help update
Updates data model based on the class name and id by adding or updating attribute

Usage: update <class name> <id> <attribute name> 

data models are: BaseModel, User, State, City, Amenity, Place, Review
(hbnb) update User 60b0bba8-e9af-4da0-83e3-ab0e479a5285 name Betty
(hbnb) all User
["[User] (60b0bba8-e9af-4da0-83e3-ab0e479a5285) {'id': '60b0bba8-e9af-4da0-83e3-ab0e479a5285', 'created_at': datetime.datetime(2023, 8, 20, 9, 12, 59, 700603), 'updated_at': datetime.datetime(2023, 8, 20, 9, 12, 59, 700623), 'name': 'Betty'}"]
(hbnb) quit
```