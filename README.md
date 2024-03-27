<center> <h1>HBNB - The Console</h1> </center>

This repository contains the initial stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

---

<center><h3>Repository Contents by Project Task</h3> </center>

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0: Authors/README File | [AUTHORS](https://github.com/justinmajetich/AirBnB_clone/blob/dev/AUTHORS) | Project authors |
| 1: Pep8 | N/A | All code is pep8 compliant|
| 2: Unit Testing | [/tests](https://github.com/justinmajetich/AirBnB_clone/tree/dev/tests) | All class-defining modules are unittested |
| 3. Make BaseModel | [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Defines a parent class to be inherited by all model classes|
| 4. Update BaseModel w/ kwargs | [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Add functionality to recreate an instance of a class from a dictionary representation|
| 5. Create FileStorage class | [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) [/models/_ _init_ _.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/__init__.py) [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Defines a class to manage persistent file storage system|
| 6. Console 0.0.1 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) | Add basic functionality to console program, allowing it to quit, handle empty lines and ^D |
| 7. Console 0.1 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) | Update the console with methods allowing the user to create, destroy, show, and update stored data |
| 8. Create User class | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) [/models/user.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/user.py) | Dynamically implements a user class |
| 9. More Classes | [/models/user.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/user.py) [/models/place.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/place.py) [/models/city.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/city.py) [/models/amenity.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/amenity.py) [/models/state.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/state.py) [/models/review.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/review.py) | Dynamically implements more classes |
| 10. Console 1.0 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) | Update the console and file storage system to work dynamically with all  classes update file storage |
<br>
<br>
<center> <h2>General Use</h2> </center>

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

##### Commands

    * create - Creates an instance based on given class

    * destroy - Destroys an object based on class and UUID

    * show - Shows an object based on class and UUID

    * all - Shows all objects the program has access to, or all objects of a given class

    * update - Updates existing attributes an object based on class name and UUID

    * quit - Exits the program (EOF will as well)

##### Alternative Syntax

Users are able to issue a number of console command using an alternative syntax:

 Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])
Advanced syntax is implemented for the following commands:

    * all - Shows all objects the program has access to, or all objects of a given class

 * count - Return number of object instances by class

    * show - Shows an object based on class and UUID

 * destroy - Destroys an object based on class and UUID

    * update - Updates existing attributes an object based on class name and UUID

<br>
<br>
<center> <h2>Examples</h2> </center>
<h3>Primary Command Syntax</h3>

###### Example 0: Create an object

Usage: create <class_name>

```
(hbnb) create BaseModel
```

```
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)                   
```

###### Example 1: Show an object

Usage: show <class_name> <_id>

```
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)  
```

###### Example 2: Destroy an object

Usage: destroy <class_name> <_id>

```
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)   
```

###### Example 3: Update an object

Usage: update <class_name> <_id>

```
(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)
```

<h3>Alternative Syntax</h3>

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

<center> <h1>AirBnB clone v2 - MySQL</h1> </center>

The AirBnB clone project embarks on an ambitious journey to replicate the functionality of the AirBnB platform, starting from the backend with a custom console for data management, evolving through data persistence with file storage and MySQL, to eventually including advanced features like user authentication and web deployment. This holistic approach not only mirrors the complexity of real-world applications but also hones software development skills through hands-on practice with databases, ORM, and front-end integration.

<center><h3>Repository Contents by Project Task</h3> </center>

To enhance the README documentation for the AirBnB clone - MySQL project, we'll include detailed information on specific tasks related to this segment of the project. The table below is refined for a professional English presentation and extends to include tasks 9 and 10.

---

| Tasks | Files | Description |
| ----- | ----- | ----------- |
| 0. Fork me if you can! | N/A | Fork the codebase for the AirBnB clone v2 project. |
| 1. Bug free! | N/A | Ensure all code is error-free and adheres to PEP8 standards. |
| 2. Console improvements | [console.py](https://github.com/justinmajetich/AirBnB_clone_v2/blob/master/console.py) | Enhance the console to support object creation with parameters. |
| 3. MySQL setup development | [setup_mysql_dev.sql](https://github.com/justinmajetich/AirBnB_clone_v2/blob/master/setup_mysql_dev.sql) | Script to prepare a MySQL server for development purposes. |
| 4. MySQL setup test | [setup_mysql_test.sql](https://github.com/justinmajetich/AirBnB_clone_v2/blob/master/setup_mysql_test.sql) | Script to prepare a MySQL server for testing. |
| 5. Delete object | [models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone_v2/blob/master/models/engine/file_storage.py) | Update FileStorage to allow for object deletion. |
| 6. DBStorage - States and Cities | [models/state.py](https://github.com/justinmajetich/AirBnB_clone_v2/blob/master/models/state.py), [models/city.py](https://github.com/justinmajetich/AirBnB_clone_v2/blob/master/models/city.py), [models/engine/db_storage.py](https://github.com/justinmajetich/AirBnB_clone_v2/blob/master/models/engine/db_storage.py) | Implement DBStorage for managing states and cities. |
| 7. DBStorage - User | [models/user.py](https://github.com/justinmajetich/AirBnB_clone_v2/blob/master/models/user.py), [models/engine/db_storage.py](https://github.com/justinmajetich/AirBnB_clone_v2/blob/master/models/engine/db_storage.py) | Update DBStorage for user management. |
| 8. DBStorage - Place | [models/place.py](https://github.com/justinmajetich/AirBnB_clone_v2/blob/master/models/place.py), [models/engine/db_storage.py](https://github.com/justinmajetich/AirBnB_clone_v2/blob/master/models/engine/db_storage.py) | Update DBStorage for place management. |
| 9. DBStorage - Amenity...and BOOM! | [models/amenity.py](https://github.com/justinmajetich/AirBnB_clone_v2/blob/master/models/amenity.py), [models/engine/db_storage.py](https://github.com/justinmajetich/AirBnB_clone_v2/blob/master/models/engine/db_storage.py) | Extend DBStorage to include amenities, showcasing advanced database operations. |
| 10. DBStorage - Review | [models/review.py](https://github.com/justinmajetich/AirBnB_clone_v2/blob/master/models/review.py), [models/engine/db_storage.py](https://github.com/justinmajetich/AirBnB_clone_v2/blob/master/models/engine/db_storage.py) | Integrate reviews into DBStorage, emphasizing relational database interactions. |

---

In crafting a professional and comprehensive README for the AirBnB clone - MySQL project, it's essential to outline the general usage of the project meticulously. This section provides a clear overview of how to interact with the project, from setup to execution, ensuring users can navigate and utilize the system efficiently.

---

<center><h2>General Use</h2></center>

The AirBnB clone - MySQL project is a comprehensive endeavor to recreate aspects of the AirBnB platform, focusing on backend development with a bespoke console for data management. This project progresses through stages, from simple data management and persistence using file storage and MySQL to advanced functionalities like user authentication and integration with a front-end interface. This multi-faceted approach aims not only to mimic the complexity found in real-world applications but also to sharpen software development skills through practical experience with databases, Object-Relational Mapping (ORM), and web development.

### Getting Started

1. **Clone the Repository**: Begin by cloning this repository to your local machine to access the project files.

2. **Launch the Console**: Navigate to the root directory of the project and start the custom console by executing:

   ```
   ./console.py
   ```

   Upon successful execution, you will be greeted with the `(hbnb)` prompt, indicating you are now within the AirBnB clone console environment.

### Console Commands

Within the console, several commands are at your disposal for managing the application's data:

- **`create`**: Creates a new instance of a given class.
- **`show`**: Displays an instance based on class name and id.
- **`destroy`**: Deletes an instance based on class name and id.
- **`all`**: Shows all instances of a class or, if no class is specified, all known instances.
- **`update`**: Updates an instance based on class name and id by adding or updating attributes.
- **`quit`** or **`EOF`**: Exits the console.

### Alternative Syntax

For convenience, an alternative syntax is supported for certain commands, allowing for more intuitive interaction:

```
<class_name>.<command>(<id>)
```

This alternative syntax provides a more direct way to interact with specific objects, streamlining commands such as `all`, `count`, `show`, `destroy`, and `update`.

### Examples

#### Creating an Object

```
(hbnb) create User
```

#### Displaying an Object

```
(hbnb) show User user_id
```

#### Updating an Object

```
(hbnb) update User user_id email "a@example.com"
```

By following these guidelines, users can effectively interact with the AirBnB clone project, managing data through the custom console and utilizing the MySQL integration for persistent storage and advanced database interactions.

---
