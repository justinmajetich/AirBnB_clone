# AirBnB clone - MySQL


Welcome to the continuation of the [AirBnB clone project!](https://github.com/Mohabdo21/AirBnB_clone) In this phase, our main objective is to delve into the realm of object-relational mapping (ORM) and leverage the powerful SQLAlchemy tool to integrate a robust database system into our backend design.

## Authors

This version of the project was forked from this [codebase](https://github.com/justinmajetich/AirBnB_clone.git) and got modified, enhanced and incorporated with the new features by:  

- Mohannad Babeker
- Reem Osama


## Project Overview
  
In the updated version of the AirBnB clone project, we've introduced a significant enhancement by incorporating MySQL database support alongside the existing JSON file storage. This expansion not only broadens the storage options but also utilizes object-relational mapping (ORM) to seamlessly integrate object-oriented models with relational database tables.

![hbnb-step2.png](https://i.postimg.cc/MGrzP7bN/hbnb-step2.png)

## New Features
-   The project now supports MySQL database storage alongside JSON file storage, offering scalability and robustness for larger applications.
-   Users can select their preferred storage method (JSON or MySQL) during setup or runtime for flexibility.
-   MySQL integration includes ORM support, enabling the definition of relationships between entities like users, properties, reviews, and amenities.
- Users can specify parameters using a syntax that includes key-value pairs  in the console while creating new instances enabling them to set attributes with various data types.

## Relationships
In addition to the MySQL database support and ORM integration, the updated version of the project introduces support for defining relationships between different entities using many-to-one and many-to-many relationships. These relational features enhance the data model's flexibility and enable more complex data structures within the AirBnB platform.

![daaef631636b40e0a279a8f240703e065f9d3481.jpg](https://i.postimg.cc/7ZyxR1GQ/daaef631636b40e0a279a8f240703e065f9d3481.jpg)


### One-to-Many Relationships:

1.  **User - Review - Place:**
    
    -   Each review is associated with a specific rental property and the user who submitted it. This structure allows users to provide property-specific feedback.
2.  **User - Place:**
    
    -   Users can own multiple rental properties, enabling them to manage and list multiple properties for rent.
3.  **Place - City:**
    
    -   Rental properties are located within specific cities, facilitating location-based search and filtering.
4.  **City - State:**
    
    -   Cities are grouped within specific states, establishing a geographic hierarchy for property organization.

### Many-to-Many Relationship:

1.  **Place - Amenity:**
    -   Rental properties can offer various amenities, with multiple properties associated with each amenity. An intermediate table streamlines querying for properties with specific amenities.

## Usage
To install and run the project, follow these simple steps:

**Retrieve the Project:**
Begin by cloning the project repository from its GitHub location. Execute the following command in your terminal:

    $ git clone https://github.com/Mohabdo21/AirBnB_clone_v2.git

**Enter Project Directory:**
Navigate into the project directory by executing the following command:

    $ cd AirBnB_clone_v2
    
**Configure Environment and Dependencies:**
Execute the  `set_env_db.sh`  script to establish the environment and install necessary dependencies:

    $ ./set_env_db.sh

**#Note:** The script `set_env_db.sh`  prompts you to select the storage type (file or database) and the environment (development or test).
For database storage, provide MySQL admin credentials, and choose between development and test environments.
The script then creates a virtual environment, installs necessary packages, sets up the MySQL database based on the selected environment, and exports environment variables.

**Launch the Console:**

You can run the console in non-interactive mode without using the script by specifying the environment variables during piping the command. For example:

```
 $ echo 'create State name="California"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
```
Alternatively, you can launch the interactive console as follows but with running the above script first or without specifying the environment variables to store data using File Storage:

    $ ./console

## Additional Resources
For more information about the console and the class hierarchy in the AirBnB Backend System, please refer to the documentation available at [AirBnB_clone](https://github.com/Mohabdo21/AirBnB_clone/tree/824b17f030aa8a129e69de9dfff4c9f8f260e551/#).
