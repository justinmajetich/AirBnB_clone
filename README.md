## AirBnB Clone - MySQL

# Overview

This project involves creating an AirBnB clone with a MySQL database backend. The implementation is to be done in Python using Object-Oriented Programming (OOP) principles and SQLAlchemy for Object-Relational Mapping (ORM). The project aims to cover various aspects, including unit testing, handling environment variables, and working with different storage engines.

## Team Members
- Guillaume
- Onsongo Onditi
- Simo Khanyi

## Learning Objectives
By the end of this project, the team is expected to understand and implement the following concepts:
- Unit testing in a large project
- Use of *args and **kwargs
- Handling named arguments in functions
- MySQL database creation, user management, and privilege granting
- Understanding ORM and mapping Python classes to MySQL tables
- Managing two different storage engines with a single codebase
- Effective use of environment variables

## Fork Me if You Can!

In the industry, working with existing code is common. Before making changes, consider:

- Who wrote this code?
- How does it work?
- Where are the unittests?
- Where is this?
- Why was it implemented like this?
- Avoid the temptation to refactor everything.

**Project Instructions:**

1. Fork the existing codebase.
2. Update the repository name to AirBnB_clone_v2.
3. In the README.md, add your information without deleting the initial authors.
4. If you own the repository, create a new one named AirBnB_clone_v2 with the same content.

## Unit Testing and PEP8 Compliance

### Unittest Module

This codebase includes various test cases, covering basic functionality. Ensure all unittests pass without errors for each storage engine.


# Run all unittests
python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1

## Console Improvements

### Updated Command Format

Enhancements have been made to the `create` command in the console:

- Now you can create objects with specific details using the following syntax:
  - `create <Class name> <param 1> <param 2> <param 3>...`
- Parameters are specified as `<key name>=<value>`.
- Value types:
  - String: Enclose values in double quotes. If the value contains double quotes, use a backslash before them. Also, replace underscores (_) with spaces.
    - Example: `name="My_little_house"`
  - Float: Use the format `<unit>.<decimal>`.
  - Integer: Use the default format `<number>`.

If a parameter doesn’t meet these rules or is not recognized correctly, it will be skipped.

### Testing the Changes

To ensure these improvements work as intended, run tests specifically for the FileStorage engine. Confirm that creating objects with different parameters behaves as expected.

Feel free to let me know if there's anything else or if you have additional instructions!

## MySQL Development Setup

Prepare MySQL server for the project with:

- Database: hbnb_dev_db
- New user: hbnb_dev (in localhost) with password hbnb_dev_pwd
- User privileges: All on hbnb_dev_db, SELECT on performance_schema (only this database)

Ensure the script doesn't fail if hbnb_dev_db or hbnb_dev already exists.


## MySQL Test Setup

Create a script named `setup_mysql_test.sql` with the following instructions:

1. Ensure the existence of the database `hbnb_test_db`.
2. Create or update the user `hbnb_test` in localhost with the password 'hbnb_test_pwd'.
3. Grant all privileges on `hbnb_test_db` to the user `hbnb_test` in localhost.
4. Grant SELECT privilege on `performance_schema` to the user `hbnb_test` in localhost.

Execute the script using the following command:


cat setup_mysql_test.sql | mysql -hlocalhost -uroot -p

## Object Deletion and FileStorage Update

### FileStorage Update

In `models/engine/file_storage.py`, make the following updates:

1. Add a new public instance method: `def delete(self, obj=None)`: 
   - Deletes `obj` from `__objects` if it exists. If `obj` is `None`, the method does nothing.

2. Update the prototype of `def all(self)` to `def all(self, cls=None)`: 
   - Returns a list of objects of a specific class if `cls` is provided. 
   - Example with State: This is an optional filtering.

## Transition to SQLAlchemy

In this step, you'll transition from FileStorage to DBStorage using SQLAlchemy. Follow these changes:

### BaseModel Update (models/base_model.py)

1. Create `Base = declarative_base()` before the class definition of BaseModel.
2. Update class attributes in BaseModel:
   - `id`: Represents a unique string (60 characters), cannot be null, primary key.
   - `created_at`: Represents a datetime, cannot be null, default value is the current datetime (use `datetime.utcnow()`).
   - `updated_at`: Represents a datetime, cannot be null, default value is the current datetime (use `datetime.utcnow()`).
3. Move `models.storage.new(self)` from `def __init__(self, *args, **kwargs):` to `def save(self):` and call it just before `models.storage.save()`.
4. In `def __init__(self, *args, **kwargs):`, manage kwargs to create instance attribute from this dictionary. 
   - Example: `kwargs={ 'name': "California" } => self.name = "California"` if it’s not already the case.
5. Update `to_dict()` method, remove the key `_sa_instance_state` from the dictionary returned if it exists.
6. Add a new public instance method: `def delete(self):` to delete the current instance from the storage (`models.storage`) by calling the method delete.

### City Update (models/city.py)

1. Inherit from BaseModel and Base (respect the order).
2. Add or replace class attributes:
   - `__tablename__`: Represents the table name, set it to "cities".
   - `name`: Represents a column containing a string (128 characters), cannot be null.
   - `state_id`: Represents a column containing a string (60 characters), cannot be null, is a foreign key to `states.id`.

### State Update (models/state.py)

1. Inherit from BaseModel and Base (respect the order).
2. Add or replace class attributes:
   - `__tablename__`: Represents the table name, set it to "states".
   - `name`: Represents a column containing a string (128 characters), cannot be null.
   - For DBStorage: 
      - `cities`: Represents a relationship with the class City. If the State object is deleted, all linked City objects must be automatically deleted. The reference from a City object to its State should be named `state`.
   - For FileStorage: 
      - Add getter attribute `cities` that returns the list of City instances with `state_id` equals to the current `State.id`.

### DBStorage (models/engine/db_storage.py)

1. Private class attributes:
   - `__engine`: Set to None.
   - `__session`: Set to None.
2. Public instance methods:
   - `__init__(self)`: Create the engine (`self.__engine`) linked to the MySQL database.
   - `all(self, cls=None)`: Query all objects depending on the class name (`cls`) and return a dictionary.
   - `new(self, obj)`: Add the object to the current database session (`self.__session`).
   - `save(self)`: Commit all changes of the current database session (`self.__session`).
   - `delete(self, obj=None)`: Delete from the current database session `obj` if not None.
   - `reload(self)`: Create all tables in the database and the current database session from the engine.

### __init__.py (models/__init__.py)

1. Add a conditional depending on the value of the environment variable `HBNB_TYPE_STORAGE`:
   - If equal to `db`: 
      - Import `DBStorage` class in this file.
      - Create an instance of `DBStorage` and store it in the variable `storage` (execute `storage.reload()` after instantiation).
   - Else: 
      - Import `FileStorage` class in this file.
      - Create an instance of `FileStorage` and store it in the variable `storage` (execute `storage.reload()` after instantiation).
   
This “switch” allows you to change storage type directly by using an environment variable (`HBNB_TYPE_STORAGE`).


## DBStorage - User Update (models/user.py)

In this step, update the User model to work with DBStorage:

1. User inherits from BaseModel and Base (respect the order).
2. Add or replace class attributes:
   - `__tablename__`: Represents the table name, set it to "users".
   - `email`: Represents a column containing a string (128 characters), cannot be null.
   - `password`: Represents a column containing a string (128 characters), cannot be null.
   - `first_name`: Represents a column containing a string (128 characters), can be null.
   - `last_name`: Represents a column containing a string (128 characters), can be null.

## DBStorage - Place Update (models/place.py)

In this step, update the Place model to work with DBStorage:

1. Place inherits from BaseModel and Base (respect the order).
2. Add or replace class attributes:
   - `__tablename__`: Represents the table name, set it to "places".
   - `city_id`: Represents a column containing a string (60 characters), cannot be null, is a foreign key to cities.id.
   - `user_id`: Represents a column containing a string (60 characters), cannot be null, is a foreign key to users.id.
   - `name`: Represents a column containing a string (128 characters), cannot be null.
   - `description`: Represents a column containing a string (1024 characters), can be null.
   - `number_rooms`: Represents a column containing an integer, cannot be null, default value: 0.
   - `number_bathrooms`: Represents a column containing an integer, cannot be null, default value: 0.
   - `max_guest`: Represents a column containing an integer, cannot be null, default value: 0.
   - `price_by_night`: Represents a column containing an integer, cannot be null, default value: 0.
   - `latitude`: Represents a column containing a float, can be null.
   - `longitude`: Represents a column containing a float, can be null.

## User Update (models/user.py)

Add or replace in the class User:
   - `places`: Represents a relationship with the class Place. If the User object is deleted, all linked Place objects are automatically deleted. The reference from a Place object to its User is named user.

## City Update (models/city.py)

Add or replace in the class City:
   - `places`: Represents a relationship with the class Place. If the City object is deleted, all linked Place objects are automatically deleted. The reference from a Place object to its City is named cities.


## DBStorage - Review Update (models/review.py)

In this step, update the Review model to work with DBStorage:

1. Review inherits from BaseModel and Base (respect the order).
2. Add or replace class attributes:
   - `__tablename__`: Represents the table name, set it to "reviews".
   - `text`: Represents a column containing a string (1024 characters), cannot be null.
   - `place_id`: Represents a column containing a string (60 characters), cannot be null, is a foreign key to places.id.
   - `user_id`: Represents a column containing a string (60 characters), cannot be null, is a foreign key to users.id.

## User Update (models/user.py)

Add or replace in the class User:
   - `reviews`: Represents a relationship with the class Review. If the User object is deleted, all linked Review objects are automatically deleted. The reference from a Review object to its User is named user.

## Place Update (models/place.py)

For DBStorage:
   - `reviews`: Represents a relationship with the class Review. If the Place object is deleted, all linked Review objects are automatically deleted. The reference from a Review object to its Place is named place.


## DBStorage - Amenity Update (models/amenity.py)

In this step, update the Amenity model to work with DBStorage:

1. Amenity inherits from BaseModel and Base (respect the order).
2. Add or replace class attributes:
   - `__tablename__`: Represents the table name, set it to "amenities".
   - `name`: Represents a column containing a string (128 characters), cannot be null.

## Place Update (models/place.py)

In this update, we establish a Many-To-Many relationship between the class Place and Amenity using a separate table place_amenity:

1. Add an instance of SQLAlchemy Table called place_amenity with columns place_id and amenity_id.
2. For DBStorage:
   - `amenities`: Represents a relationship with the class Amenity but also as secondary to place_amenity with the option viewonly=False.
3. For FileStorage:
   - Getter attribute `amenities` that returns the list of Amenity instances based on the attribute amenity_ids that contains all Amenity.id linked to the Place.
   - Setter attribute `amenities` that handles the append method for adding an Amenity.id to the attribute amenity_ids. This method should accept only Amenity objects; otherwise, do nothing.

What's a Many-to-Many relationship?
In our system, amenities are unique, and at least 2 places can have the same amenity. This creates a Many-To-Many relationship, and to manage it, we create a third table called place_amenity that establishes the links between places and amenities.
