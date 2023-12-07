Overview
========

This repository is for the 'AirBnB clone - The console' project. The goal of 
the project is to deploy on our server a simple copy of the AirBnB website.
Not all the features of the AirBnb website is deploid here, rather features 
that are fundamental in understanding the working of higher-level programing 
are present.
This project can be considerd as part one of a series of parts to come that 
are all focused on deploying our on clone of the AirBnB website.
	* part one: A command interpreter to manipulate data without a visual 
interface, like in a Shell (perfect for development and debugging)
	* part two: A website (the front-end) that shows the final product 
	to everybody: static and dynamic
	* part three: A database or files that store data (data = objects)
	* part four: An API that provides a communication interface between 
the front-end and your data (retrieve, create, delete, update them)

	The console
	===========

	From our console we are able to perform the following features
	* create our data model
	* manage (create, update, destroy, etc) objects via a console / command 
	interpreter
* store and persist objects to a file (JSON file)

	The command interpreter
	=======================

	This is the main feature of our console and the project in general.
	The command interpreter here is similar with shell, but limited to a specific 
	use-case. In our case, we want to be able to manage the objects of our project:

* Create a new object (ex: a new User or a new Place)
	* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
	* Update attributes of an object
	* Destroy an object

	All the above will be handled with our command interpreter.


	How to use the command interpreter?
	===================================


	* To start the command interpreter we can run ./console.py on our terminal
	* Running './console.py' will give as a prompt (hbnb)
	* After getting the prompt, we can use the help command in the interpreter 
	to see the list of commands available.
	* From the list we can use any command with the appropriate arguments
	* To close the command interpreter we can use the EOF command.

	Examples:

	$ ./console.py
	(hbnb) help

	Documented commands (type help <topic>):
		EOF  help  quit

	(hbnb)
	(hbnb)
	(hbnb) quit
	$
