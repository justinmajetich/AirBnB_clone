## AirBnB: The Console:
![DALL·E 2024-02-03 17 55 33 - Create an image featuring a console with the Python programming language logo and the Airbnb logo placed next to a serene river  The entire scene shou](https://github.com/natewood2/atlas-AirBnB_clone/assets/143881431/68f5e27e-a72c-4dc3-9331-688aa96630b8)



We are tasked with making the console for our AirBnB clone. The console is what will manage the modules utilized by our webpage through the use of a JSON-formatted database. Basically a interactive command-line interface for the AirBnB clone project.


## Main Parts of the Console:

#### BaseModel.py:

The BaseModel class, a foundational component for an AirBnB clone project focused on the console application. This is where we dynamically set attributes from keyword arguments or generates a unique ID and timestamps for new instances. Regarding string representation we implement a method to return a string representation of instance attributes, aiding in debugging and logging. Then we save updates the 'updated_at' timestamp to the current time, indicating when the object was last modified. Then finally we converts instance attributes to a dictionary, facilitating serialization, especially for storing data in a JSON format.

#### FileStorage.py:

This section of code introduces the FileStorage class, designed to manage the serialization and deserialization of instances of classes like 'BaseModel', 'User', 'State', 'Review', 'Place', 'City', and 'Amenity' to and from a JSON file. It acts as a simple file-based database system for the AirBnB clone project, allowing for persistent storage of application data across sessions. Key functionalities include:
- Object Caching: Maintains a dictionary (__objects) that maps unique object identifiers to the actual object instances, facilitating quick access to any stored object.
- Data Persistence: Utilizes a JSON file (specified by __file_path) as the storage medium. This choice leverages JSON's readable format and compatibility with web technologies.
- CRUD : Implements methods to add new objects to storage (new), retrieve all objects (all), save all objects to the file (save), and reload objects from the file (reload).

#### Console.py:

This script defines the HBNBCommand class, which serves as an interactive command-line interface for the AirBnB clone project. It inherits from Python's cmd.Cmd class, providing a framework for executing predefined commands. The HBNBCommand class is designed to manage instances of various models (like BaseModel, User, State, Review, Place, City, Amenity) through a series of command methods. Key aspects of the HBNBCommand class include:
- Command Prompt: Sets a custom prompt (hbnb) to signal readiness for user input.
- Instance Management: Implements methods to create, show, destroy, update and list instances of models. These tools make it easier to handle and look up stuff saved in the app's file storage system.
- Input Validation: Contains a method 'validate_args' to ensure valid input for operations that require class names and instance IDs, improving error handling and user feedback.
- Quit and EOF Handling: Provides do_quit and do_EOF methods to easily exit the command loop in response to "quit" commands or an End-of-File (EOF) signal.

#### Command Format:

```python
(command) <Class Name> <Instance ID> <Attribute> "<New Value>"
```

- `(command)`: The command prompt, is set to (hbnb).
- `<Class Name>`: Name of the class for the instance.
- `<Instance ID>`: ID of the instance to be manipulated.
- `<Attribute>`: Attribute to be updated or shown.
- `"<New Value>"`: New value for the attribute (for the update command).

#### Available Commands:

| Command Description        | Command Format                                      | Explanation                                      |
|-----------------------------|-----------------------------------------------------|--------------------------------------------------|
| Create a new instance       | `create <Class Name>`                        | Create a new instance of the specified class and print its ID. |
| Show instance details       | `show <Class Name> <Instance ID>`            | Show the dictionary representation of the specified instance. |
| Delete an instance           | `destroy <Class Name> <Instance ID>`         | Delete the specified instance.                   |
| List all instances           | `all [optional: <Class Name>]`               | Print a list of all instances or instances of a specific class. |
| Update an attribute          | `update <Class Name> <Instance ID> <Attribute> "<New Value>"` | Update the specified attribute of an instance.   |
| End the program              | `quit`                                       | End the program and exit the console.            |
| End the program at EOF       | `[Press Ctrl-D]`                             | End the program when the end of the file is reached. |


## Demo of The Console:



### Starting up console:

![](https://media.giphy.com/media/2GcPP91sIuYKIRUXwU/giphy.gif)

### Creating BaseModel:

![](https://media.giphy.com/media/td4vBL6fKjW5JZ25ln/giphy.gif)

### Looking up BaseModel with Unique ID:

![](https://media.giphy.com/media/VRGGoyoNOOgBOlNrKW/giphy.gif)

#### Authors
This is a list of all who contributed to this project. 

- [Nathan Wood](https://github.com/natewood2)
- [David Alsabrook](https://github.com/DAlsabrook)
