# Project: 0x04. AirBnB clone - Web framework


0. Write a script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
    You must use the option strict_slashes=False in your route definition

1. Write a script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
    You must use the option strict_slashes=False in your route definition

2. Write a script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )
    You must use the option strict_slashes=False in your route definition

3. Write a script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
        /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
            The default value of text is “is cool”
    You must use the option strict_slashes=False in your route definition

4. Write a script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
        /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
            The default value of text is “is cool”
        /number/<n>: display “n is a number” only if n is an integer
    You must use the option strict_slashes=False in your route definition

5. Write a script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
        /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
            The default value of text is “is cool”
        /number/<n>: display “n is a number” only if n is an integer
        /number_template/<n>: display a HTML page only if n is an integer:
            h1 tag: “Number: n” inside the tag body
    You must use the option strict_slashes=False in your route definition

6. Write a script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
        /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
            The default value of text is “is cool”
        /number/<n>: display “n is a number” only if n is an integer
        /number_template/<n>: display a HTML page only if n is an integer:
            H1 tag: “Number: n” inside the tag BODY
        /number_odd_or_even/<n>: display a HTML page only if n is an integer:
            H1 tag: “Number: n is even|odd” inside the tag BODY
    You must use the option strict_slashes=False in your route definition

7. Before using Flask to display our HBNB data, you will need to update some part of our engine:

Update FileStorage: (models/engine/file_storage.py)

    Add a public method def close(self):: call reload() method for deserializing the JSON file to objects

Update DBStorage: (models/engine/db_storage.py)

    Add a public method def close(self):: call remove() method on the private session attribute (self.__session) tips or close() on the class Session tips

Update State: (models/state.py) - If it’s not already present

    If your storage engine is not DBStorage, add a public getter method cities to return the list of City objects from storage linked to the current State

8. Write a script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    You must use storage for fetching data from the storage engine (FileStorage or DBStorage) => from models import storage and storage.all(...)
    After each request you must remove the current SQLAlchemy Session:
        Declare a method to handle @app.teardown_appcontext
        Call in this method storage.close()
    Routes:
        /states_list: display a HTML page: (inside the tag BODY)
            H1 tag: “States”
            UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z) tip
                LI tag: description of one State: <state.id>: <B><state.name></B>

9. Write a script that starts a Flask web application:

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
                LI tag: description of one State: <state.id>: <B><state.name></B> + UL tag: with the list of City objects linked to the State sorted by name (A->Z)
                    LI tag: description of one City: <city.id>: <B><city.name></B>

10. Write a script that starts a Flask web application:

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
                LI tag: description of one State: <state.id>: <B><state.name></B>
        /states/<id>: display a HTML page: (inside the tag BODY)
            If a State object is found with this id:
                H1 tag: “State: ”
                H3 tag: “Cities:”
                UL tag: with the list of City objects linked to the State sorted by name (A->Z)
                    LI tag: description of one City: <city.id>: <B><city.name></B>
            Otherwise:
                H1 tag: “Not found!”

11. Write a script that starts a Flask web application:

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
                Replace the content of the H4 tag under each filter title (H3 States and H3 Amenities) by &nbsp;
            State, City and Amenity objects must be loaded from DBStorage and sorted by name (A->Z)
    You must use the option strict_slashes=False in your route definition

