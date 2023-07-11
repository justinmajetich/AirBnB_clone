0x02. AirBnB clone - MySQL
This repository contains the initial stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

---




Tasks
0. Fork me if you can!
mandatory
In the industry, you will work on an existing codebase 90% of the time. Your first thoughts upon looking at it might include:

“Who did this code?”
“How it works?”
“Where are unittests?”
“Where is this?”
“Why did they do that like this?”
“I don’t understand anything.”
“… I will refactor everything…”
But the worst thing you could possibly do is to redo everything. Please don’t do that! Note: the existing codebase might be perfect, or it might have errors. Don’t always trust the existing codebase!

For this project you will fork this codebase:

update the repository name to AirBnB_clone_v2
update the README.md with your information but don’t delete the initial authors
If you are the owner of this repository, please create a new repository named AirBnB_clone_v2 with the same content of AirBnB_clone
1. Bug free!
Do you remember the unittest module?

This codebase contains many test cases. Some are missing, but the ones included cover the basic functionality of the program.

2. Console improvements
Update the def do_create(self, arg): function of your command interpreter (console.py) to allow for object creation with given parameters:

Command syntax: create <Class name> <param 1> <param 2> <param 3>...
Param syntax: <key name>=<value>
Value syntax:
String: "<value>" => starts with a double quote
any double quote inside the value must be escaped with a backslash \
all underscores _ must be replace by spaces . Example: You want to set the string My little house to the attribute name, your command line must be name="My_little_house"
Float: <unit>.<decimal> => contains a dot .
Integer: <number> => default case
If any parameter doesn’t fit with these requirements or can’t be recognized correctly by your program, it must be skipped
Don’t forget to add tests for this new feature!

Also, this new feature will be tested here only with FileStorage engine.

3. MySQL setup development
Write a script that prepares a MySQL server for the project:

A database hbnb_dev_db
A new user hbnb_dev (in localhost)
The password of hbnb_dev should be set to hbnb_dev_pwd
hbnb_dev should have all privileges on the database hbnb_dev_db (and only this database)
hbnb_dev should have SELECT privilege on the database performance_schema (and only this database)
If the database hbnb_dev_db or the user hbnb_dev already exists, your script should not fail

4. MySQL setup test
Write a script that prepares a MySQL server for the project:

A database hbnb_test_db
A new user hbnb_test (in localhost)
The password of hbnb_test should be set to hbnb_test_pwd
hbnb_test should have all privileges on the database hbnb_test_db (and only this database)
hbnb_test should have SELECT privilege on the database performance_schema (and only this database)
If the database hbnb_test_db or the user hbnb_test already exists, your script should not fail

5. Delete object
Update FileStorage: (models/engine/file_storage.py)

Add a new public instance method: def delete(self, obj=None): to delete obj from __objects if it’s inside - if obj is equal to None, the method should not do anything
Update the prototype of def all(self) to def all(self, cls=None) - that returns the list of objects of one type of class. Example below with State - it’s an optional filtering

6. DBStorage - States and Cities
SQLAlchemy will be your best friend!

It’s time to change your storage engine and use SQLAlchemy



In the following steps, you will make multiple changes:

the biggest one is the transition between FileStorage and DBStorage: In the industry, you will never find a system who can work with both in the same time - but you will find a lot of services who can manage multiple storage systems. (for example, logs service: in memory, in disk, in database, in ElasticSearch etc…) - The main concept behind is the abstraction: Make your code running without knowing how it’s stored.
add attributes for SQLAlchemy: they will be class attributes, like previously, with a “weird” value. Don’t worry, these values are for description and mapping to the database. If you change one of these values, or add/remove one attribute of the a model, you will have to delete the database and recreate it in SQL. (Yes it’s not optimal, but for development purposes, it’s ok. In production, we will add “migration mechanism” - for the moment, don’t spend time on it.)
Please follow all these steps:

Update BaseModel: (models/base_model.py)

Create Base = declarative_base() before the class definition of BaseModel
Note! BaseModel does /not/ inherit from Base. All other classes will inherit from BaseModel to get common values (id, created_at, updated_at), where inheriting from Base will actually cause SQLAlchemy to attempt to map it to a table.
Add or replace in the class BaseModel:
class attribute id
represents a column containing a unique string (60 characters)
can’t be null
primary key
class attribute created_at
represents a column containing a datetime
can’t be null
default value is the current datetime (use datetime.utcnow())
class attribute updated_at
represents a column containing a datetime
can’t be null
default value is the current datetime (use datetime.utcnow())
Move the models.storage.new(self) from def __init__(self, *args, **kwargs): to def save(self): and call it just before models.storage.save()
In def __init__(self, *args, **kwargs):, manage kwargs to create instance attribute from this dictionary. Ex: kwargs={ 'name': "California" } => self.name = "California" if it’s not already the case
Update the to_dict() method of the class BaseModel:
remove the key _sa_instance_state from the dictionary returned by this method only if this key exists
Add a new public instance method: def delete(self): to delete the current instance from the storage (models.storage) by calling the method delete
Update City: (models/city.py)

City inherits from BaseModel and Base (respect the order)
Add or replace in the class City:
class attribute __tablename__ -
represents the table name, cities
class attribute name
represents a column containing a string (128 characters)
can’t be null
class attribute state_id
represents a column containing a string (60 characters)
can’t be null
is a foreign key to states.id
Update State: (models/state.py)

State inherits from BaseModel and Base (respect the order)
Add or replace in the class State:
class attribute __tablename__
represents the table name, states
class attribute name
represents a column containing a string (128 characters)
can’t be null
for DBStorage: class attribute cities must represent a relationship with the class City. If the State object is deleted, all linked City objects must be automatically deleted. Also, the reference from a City object to his State should be named state
for FileStorage: getter attribute cities that returns the list of City instances with state_id equals to the current State.id => It will be the FileStorage relationship between State and City
New engine DBStorage: (models/engine/db_storage.py)

Private class attributes:
__engine: set to None
__session: set to None
Public instance methods:
__init__(self):
create the engine (self.__engine)
the engine must be linked to the MySQL database and user created before (hbnb_dev and hbnb_dev_db):
dialect: mysql
driver: mysqldb
all of the following values must be retrieved via environment variables:
MySQL user: HBNB_MYSQL_USER
MySQL password: HBNB_MYSQL_PWD
MySQL host: HBNB_MYSQL_HOST (here = localhost)
MySQL database: HBNB_MYSQL_DB
don’t forget the option pool_pre_ping=True when you call create_engine
drop all tables if the environment variable HBNB_ENV is equal to test
all(self, cls=None):
query on the current database session (self.__session) all objects depending of the class name (argument cls)
if cls=None, query all types of objects (User, State, City, Amenity, Place and Review)
this method must return a dictionary: (like FileStorage)
key = <class-name>.<object-id>
value = object
new(self, obj): add the object to the current database session (self.__session)
save(self): commit all changes of the current database session (self.__session)
delete(self, obj=None): delete from the current database session obj if not None
reload(self):
create all tables in the database (feature of SQLAlchemy) (WARNING: all classes who inherit from Base must be imported before calling Base.metadata.create_all(engine))
create the current database session (self.__session) from the engine (self.__engine) by using a sessionmaker - the option expire_on_commit must be set to False ; and scoped_session - to make sure your Session is thread-safe
Update __init__.py: (models/__init__.py)

Add a conditional depending of the value of the environment variable HBNB_TYPE_STORAGE:
If equal to db:
Import DBStorage class in this file
Create an instance of DBStorage and store it in the variable storage (the line storage.reload() should be executed after this instantiation)
Else:
Import FileStorage class in this file
Create an instance of FileStorage and store it in the variable storage (the line storage.reload() should be executed after this instantiation)
This “switch” will allow you to change storage type directly by using an environment variable (example below)

7. DBStorage - User

Update User: (models/user.py)

User inherits from BaseModel and Base (respect the order)
Add or replace in the class User:
class attribute __tablename__
represents the table name, users
class attribute email
represents a column containing a string (128 characters)
can’t be null
class attribute password
represents a column containing a string (128 characters)
can’t be null
class attribute first_name
represents a column containing a string (128 characters)
can be null
class attribute last_name
represents a column containing a string (128 characters)
can be null

8. DBStorage - Place
Update Place: (models/place.py)

Place inherits from BaseModel and Base (respect the order)
Add or replace in the class Place:
class attribute __tablename__
represents the table name, places
class attribute city_id
represents a column containing a string (60 characters)
can’t be null
is a foreign key to cities.id
class attribute user_id
represents a column containing a string (60 characters)
can’t be null
is a foreign key to users.id
class attribute name
represents a column containing a string (128 characters)
can’t be null
class attribute description
represents a column containing a string (1024 characters)
can be null
class attribute number_rooms
represents a column containing an integer
can’t be null
default value: 0
class attribute number_bathrooms
represents a column containing an integer
can’t be null
default value: 0
class attribute max_guest
represents a column containing an integer
can’t be null
default value: 0
class attribute price_by_night
represents a column containing an integer
can’t be null
default value: 0
class attribute latitude
represents a column containing a float
can be null
class attribute longitude
represents a column containing a float
can be null
Update User: (models/user.py)

Add or replace in the class User:
class attribute places must represent a relationship with the class Place. If the User object is deleted, all linked Place objects must be automatically deleted. Also, the reference from a Place object to his User should be named user
Update City: (models/city.py)

Add or replace in the class City:
class attribute places must represent a relationship with the class Place. If the City object is deleted, all linked Place objects must be automatically deleted. Also, the reference from a Place object to his City should be named cities

9. DBStorage - Review
Update Review: (models/review.py)

Review inherits from BaseModel and Base (respect the order)
Add or replace in the class Review:
class attribute __tablename__
represents the table name, reviews
class attribute text
represents a column containing a string (1024 characters)
can’t be null
class attribute place_id
represents a column containing a string (60 characters)
can’t be null
is a foreign key to places.id
class attribute user_id
represents a column containing a string (60 characters)
can’t be null
is a foreign key to users.id
Update User: (models/user.py)

Add or replace in the class User:
class attribute reviews must represent a relationship with the class Review. If the User object is deleted, all linked Review objects must be automatically deleted. Also, the reference from a Review object to his User should be named user
Update Place: (models/place.py)

for DBStorage: class attribute reviews must represent a relationship with the class Review. If the Place object is deleted, all linked Review objects must be automatically deleted. Also, the reference from a Review object to his Place should be named place
for FileStorage: getter attribute reviews that returns the list of Review instances with place_id equals to the current Place.id => It will be the FileStorage relationship between Place and Review

10. DBStorage - Amenity... and BOOM!

Update Amenity: (models/amenity.py)

Amenity inherits from BaseModel and Base (respect the order)
Add or replace in the class Amenity:
class attribute __tablename__
represents the table name, amenities
class attribute name
represents a column containing a string (128 characters)
can’t be null
class attribute place_amenities must represent a relationship Many-To-Many between the class Place and Amenity. Please see below more detail: place_amenity in the Place update
Update Place: (models/place.py)

Add an instance of SQLAlchemy Table called place_amenity for creating the relationship Many-To-Many between Place and Amenity:
table name place_amenity
metadata = Base.metadata
2 columns:
place_id, a string of 60 characters foreign key of places.id, primary key in the table and never null
amenity_id, a string of 60 characters foreign key of amenities.id, primary key in the table and never null
Update Place class:
for DBStorage: class attribute amenities must represent a relationship with the class Amenity but also as secondary to place_amenity with option viewonly=False (place_amenity has been define previously)
for FileStorage:
Getter attribute amenities that returns the list of Amenity instances based on the attribute amenity_ids that contains all Amenity.id linked to the Place
Setter attribute amenities that handles append method for adding an Amenity.id to the attribute amenity_ids. This method should accept only Amenity object, otherwise, do nothing.
What’s a Many-to-Many relationship?
In our system, we don’t want to duplicate amenities (for example, having 10000 time the amenity Wifi), so they will be unique. But, at least 2 places can have the same amenity (like Wifi for example). We are in the case of:

an amenity can be linked to multiple places
a place can have multiple amenities
= Many-To-Many

To make this link working, we will create a third table called place_amenity that will create these links.

And you are good, you have a new engine!
