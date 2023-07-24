0x04. AirBnB clone - Web framework

![flask](https://flask.palletsprojects.com/en/2.3.x/_static/flask-vertical.png)
Learning Objectives

    What is a Web Framework
    How to build a web framework with Flask
    How to define routes in Flask
    What is a route
    How to handle variables in a route
    What is a template
    How to create a HTML response in Flask by using a template
    How to create a dynamic template (loops, conditions…)
    How to display in HTML data from a MySQL database

Requirements

    Allowed editors: vi, vim, emacs
    All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
    All your files should end with a new line
    The first line of all your files should be exactly #!/usr/bin/python3
    A README.md file, at the root of the folder of the project, is mandatory
    Your code should use the PEP 8 style (version 1.7)
    All your files must be executable
    The length of your files will be tested using wc
    All your modules should have documentation (python3 -c 'print(import("my_module").doc)')
    All your classes should have documentation (python3 -c 'print(import("my_module").MyClass.doc)')
    All your functions (inside and outside a class) should have documentati- on (python3 -c 'print(import("my_module").my_function.doc)' and python3 -c 'print(import("my_module").MyClass.my_function.doc)')
    A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

HTML/CSS Files

    Allowed editors: vi, vim, emacs
    All your files should end with a new line
    A README.md file at the root of the folder of the project is mandatory
    Your code should be W3C compliant and validate with W3C-Validator (except for jinja template)
    All your CSS files should be in the styles folder
    All your images should be in the images folder
    You are not allowed to use !important or id (#... in the CSS file)
    All tags must be in uppercase
    Current screenshots have been done on Chrome 56.0.2924.87.
    No cross browsers

Install Flask

sudo pip3 install Flask
Task Descriptions

    0-hello_route.py - script that starts a Flask web application:
        Your web application must be listening on 0.0.0.0, port 5000
        Routes:
            /: display “Hello HBNB!”
            You must use the option strict_slashes=False in your route definition

    1-hbnb_route.py - script that starts a Flask web application:
        Your web application must be listening on 0.0.0.0, port 5000
        Routes:
            /: display “Hello HBNB!”
            /hbnb: display “HBNB”
            You must use the option strict_slashes=False in your route definition

    2-c_route.py - script that starts a Flask web application:
        Your web application must be listening on 0.0.0.0, port 5000
        Routes:
            /: display “Hello HBNB!”
            /hbnb: display “HBNB”
            /c/: display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )
            You must use the option strict_slashes=False in your route definition

    3-python_route.py - script that starts a Flask web application:
        Your web application must be listening on 0.0.0.0, port 5000
        Routes:
            /: display “Hello HBNB!”
            /hbnb: display “HBNB”
            /c/: display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )
            /python/(): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
                The default value of text is “is cool”
            You must use the option strict_slashes=False in your route definition

    4-number_route.py - script that starts a Flask web application:
        Your web application must be listening on 0.0.0.0, port 5000
        Routes:
            /: display “Hello HBNB!”
            /hbnb: display “HBNB”
            /c/: display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )
            /python/(): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
                The default value of text is “is cool”
            /number/: display “n is a number” only if n is an integer
            You must use the option strict_slashes=False in your route definition

    5-number_template.py - script that starts a Flask web application:
        Your web application must be listening on 0.0.0.0, port 5000
        Routes:
            /: display “Hello HBNB!”
            /hbnb: display “HBNB”
            /c/: display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )
            /python/(): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
                The default value of text is “is cool”
            /number/: display “n is a number” only if n is an integer
            /number_template/: display a HTML page only if n is an integer:
                H1 tag: “Number: n” inside the tag BODY
            You must use the option strict_slashes=False in your route definition

    templates/5-number.html - template for task 5

    6-number_odd_or_even.py - script that starts a Flask web application:
        Your web application must be listening on 0.0.0.0, port 5000
        Routes:
            /: display “Hello HBNB!”
            /hbnb: display “HBNB”
            /c/: display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )
            /python/(): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
                The default value of text is “is cool”
            /number/: display “n is a number” only if n is an integer
            /number_template/: display a HTML page only if n is an integer:
                H1 tag: “Number: n” inside the tag BODY
            /number_odd_or_even/: display a HTML page only if n is an integer:
                H1 tag: “Number: n is even|odd” inside the tag BODY
            You must use the option strict_slashes=False in your route definition

    templates/6-number_odd_or_even.html - template for task 6

    Task 7: -Before using Flask to display our HBNB data, you will need to update some part of our engine:
        Update FileStorage: (models/engine/file_storage.py)
            Add a public method def close(self):: call reload() method for deserializing the JSON file to objects
        Update DBStorage: (models/engine/db_storage.py)
            Add a public method def close(self):: call remove() method on the private session attribute (self.__session) tips or close() on the class Session tips
        Update State: (models/state.py) - If it’s not already present
        If your storage engine is not DBStorage, add a public getter method cities to return the list of City objects from storage linked to the current State
        Files for task 7: (in AirBnB_clone_v2) - models/engine/file_storage.py, models/engine/db_storage.py, models/state.py

    7-states_list.py - Write a script that starts a Flask web application:
        Your web application must be listening on 0.0.0.0, port 5000
        You must use storage for fetching data from the storage engine (FileStorage or DBStorage) => from models import storage and storage.all(...)
        To load all cities of a State:
            If your storage engine is DBStorage, you must use cities relationship
            Otherwise, use the public getter method cities
        After each request you must remove the current SQLAlchemy Session:
            Declare a method to handle @app.teardown_appcontext
            Call in this method storage.close()
        Routes:
            /states_list: display a HTML page: (inside the tag BODY)
                H1 tag: “States”
                UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z) tip
                    LI tag: description of one State: <state.id>: <state.name>
        Import this 7-dump to have some data
        You must use the option strict_slashes=False in your route definition

    templates/7-states_list.html - template for task 8

    8-cities_by_states.py - Write a script that starts a Flask web application:
        Your web application must be listening on 0.0.0.0, port 5000
        You must use storage for fetching data from the storage engine (FileStorage or DBStorage) => from models import storage and storage.all(...)
        To load all cities of a State:
            If your storage engine is DBStorage, you must use cities relationship
            Otherwise, use the public getter method cities
        After each request you must remove the current SQLAlchemy Session:
            Declare a method to handle @app.teardown_appcontext
            Call in this method storage.close()
        Routes:
            /cities_by_states: display a HTML page: (inside the tag BODY)
                H1 tag: “States”
                UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z) tip
                    LI tag: description of one State: <state.id>: <state.name> + UL tag: with the list of City objects linked to the State sorted by name (A->Z)
                        LI tag: description of one City: <city.id>: <city.name>
        Import this 7-dump to have some data
        You must use the option strict_slashes=False in your route definition

    templates/8-cities_by_states.html - template for task 9

    9-states.py - Write a script that starts a Flask web application:
        Your web application must be listening on 0.0.0.0, port 5000
        You must use storage for fetching data from the storage engine (FileStorage or DBStorage) => from models import storage and storage.all(...)
        To load all cities of a State:
            If your storage engine is DBStorage, you must use cities relationship
            Otherwise, use the public getter method cities
        After each request you must remove the current SQLAlchemy Session:
            Declare a method to handle @app.teardown_appcontext
            Call in this method storage.close()
        Routes:
            /states: display a HTML page: (inside the tag BODY)
                H1 tag: “States”
                UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z) tip
                    LI tag: description of one State: <state.id>: <state.name>
            /states/: display a HTML page: (inside the tag BODY) - If a State object is found with this id: - H1 tag: “State: ” - H3 tag: “Cities:” - UL tag: with the list of City objects linked to the State sorted by name (A->Z) - LI tag: description of one City: <city.id>: <city.name> - Otherwise: - H1 tag: “Not found!”
        You must use the option strict_slashes=False in your route definition
        Import this 7-dump to have some data

    templates/9-states.html - template for task 10

    10-hbnb_filters.py - Write a script that starts a Flask web application:
        Your web application must be listening on 0.0.0.0, port 5000
        You must use storage for fetching data from the storage engine (FileStorage or DBStorage) => from models import storage and storage.all(...)
        To load all cities of a State:
            If your storage engine is DBStorage, you must use cities relationship
            Otherwise, use the public getter method cities
        After each request you must remove the current SQLAlchemy Session:
            Declare a method to handle @app.teardown_appcontext
            Call in this method storage.close()
        Routes:
            /hbnb_filters: display a HTML page like 6-index.html, which was done during the project 0x01. AirBnB clone - Web static
                Copy files 3-footer.css, 3-header.css, 4-common.css and 6-filters.css from web_static/styles/ to the folder web_flask/static/styles
                Copy files icon.png and logo.png from web_static/images/ to the folder web_flask/static/images
                Update .popover class in 6-filters.css to allow scrolling in the popover and a max height of 300 pixels.
                Use 6-index.html content as source code for the template 10-hbnb_filters.html:
                    Replace the content of the H4 tag under each filter title (H3 States and H3 Amenities) by  
                State, City and Amenity objects must be loaded from DBStorage and sorted by name (A->Z)
        You must use the option strict_slashes=False in your route definition
        Import this 10-dump to have some data

    templates/10-hbnb_filters.html - template for task 11

    web_flask/static/ - static files for display

(ADVANCED TASK)

    100-hbnb.py - Write a script that starts a Flask web application:
        Your web application must be listening on 0.0.0.0, port 5000
        You must use storage for fetching data from the storage engine (FileStorage or DBStorage) => from models import storage and storage.all(...)
        To load all cities of a State:
            If your storage engine is DBStorage, you must use cities relationship
            Otherwise, use the public getter method cities
        After each request you must remove the current SQLAlchemy Session:
            Declare a method to handle @app.teardown_appcontext
            Call in this method storage.close()
        Routes:
            /hbnb: display a HTML page like 8-index.html, done during the 0x01. AirBnB clone - Web static project
                Copy files 3-footer.css, 3-header.css, 4-common.css, 6-filters.css and 8-places.css from web_static/styles/ to the folder web_flask/static/styles
                Copy all files from web_static/images/ to the folder web_flask/static/images
                Update .popover class in 6-filters.css to enable scrolling in the popover and set max height to 300 pixels.
                Update 8-places.css to always have the price by night on the top right of each place element, and the name correctly aligned and visible (i.e. screenshots below)
                Use 8-index.html content as source code for the template 100-hbnb.html:
                Replace the content of the H4 tag under each filter title (H3 States and H3 Amenities) by  
                Make sure all HTML tags from objects are correctly used (example:
                must generate a new line)
                State, City, Amenity and Place objects must be loaded from DBStorage and sorted by name (A->Z)
        You must use the option strict_slashes=False in your route definition
        Import this 100-dump to have some data

    templates/100-hbnb.html - template for task 12

    web_flask/static/ - static files for display

