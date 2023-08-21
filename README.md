AIRBNB_V2
-------------
This README provides an overview of the updates and changes made to the project. Please read this document to understand the modifications and improvements introduced in the codebase.

Console Improvements
do_create Command
The do_create command in the command interpreter (console.py) has been updated to allow for object creation with given parameters. The syntax for creating an object with specific parameters is as follows:
create <Class name> <param 1> <param 2> <param 3>...
<key name>=<value>

String values should be enclosed in double quotes, and any double quotes within the value should be escaped with a backslash.
Underscores (_) in keys should be replaced with spaces.
Floats are represented as <unit>.<decimal>.
Integers are standard number values.
If a parameter doesn't fit these requirements or can't be recognized, it will be skipped.

MySQL Setup Development
A script has been provided to prepare a MySQL server for the project's development environment:

Creates a database named hbnb_dev_db.
Creates a new user named hbnb_dev with the password hbnb_dev_pwd.
Grants hbnb_dev all privileges on the hbnb_dev_db database.
Grants hbnb_dev SELECT privilege on the performance_schema database.
MySQL Setup Test
Another script has been provided to prepare a MySQL server for the project's testing environment:

Creates a database named hbnb_test_db.
Creates a new user named hbnb_test with the password hbnb_test_pwd.
Grants hbnb_test all privileges on the hbnb_test_db database.
Grants hbnb_test SELECT privilege on the performance_schema database.
Delete Object
The FileStorage class in models/engine/file_storage.py has been updated:

A new public instance method delete(self, obj=None) has been added to delete an object from the __objects dictionary. If obj is None, the method does nothing.
The prototype of the all method has been updated to optionally accept a cls parameter, allowing for filtering objects of a specific class.
DBStorage - States and Cities
The storage engine has been transitioned from FileStorage to DBStorage using SQLAlchemy:

The Base class has been defined using SQLAlchemy's declarative_base().
The BaseModel class has been updated to use SQLAlchemy attributes and methods.
The to_dict method of the BaseModel class no longer includes the _sa_instance_state key in the returned dictionary.
A new public instance method delete(self) has been added to the BaseModel class to delete instances from the storage.
The City and State classes have been updated to use SQLAlchemy attributes and relationships.
Update User, Place, City, and Review
The User, Place, City, and Review classes have been updated to include or replace class attributes and relationships to fit the new SQLAlchemy structure.

Update Amenity and Place (Many-To-Many Relationship)
The Amenity and Place classes have been updated to establish a Many-To-Many relationship using a third table named place_amenity. This relationship enables linking multiple amenities to multiple places without duplication.

place_amenity Table
Metadata: Base.metadata
Columns:
place_id: Foreign key to places.id (primary key, string of 60 characters, never null)
amenity_id: Foreign key to amenities.id (primary key, string of 60 characters, never null)
For DBStorage:

The Place class includes a new SQLAlchemy Table instance called place_amenity.
The class attribute amenities is updated to represent a relationship with the Amenity class through the place_amenity table.
For FileStorage:

The getter attribute amenities in the Place class returns a list of Amenity instances based on the amenity_ids attribute.
The setter attribute amenities handles the append method for adding an Amenity.id to the amenity_ids attribute.
Usage
To switch between DBStorage and FileStorage, set the HBNB_TYPE_STORAGE environment variable:

If HBNB_TYPE_STORAGE equals "db", an instance of DBStorage will be created.
If not, an instance of FileStorage will be created.
Remember to execute storage.reload() after creating the storage instance to load data if needed.

Conclusion
With these updates and changes, the project's storage engine has been transitioned to use SQLAlchemy and supports advanced features like creating objects with given parameters and establishing many-to-many relationships between objects. Make sure to read the provided instructions and adapt the codebase accordingly to benefit from these improvements.
