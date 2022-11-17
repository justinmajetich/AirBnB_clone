# PROJECT: 0x03. AirBnB clone - Web framework
### AUTHOR: Matthew Allen

## TASKS:
### 0. Hello Flask! - `0-hello_route.py`, `__init__.py`
Script that starts a Flask web application:
* Must be listening on `0.0.0.0`, port `5000`.
* Routes:
    - `/`: display "Hello HBNB!"
* Use option `strict_slashes=False` in the root definition

### 1. HBNB - `1-hbnb_route.py`
Script that starts a Flask web application:
* Must be listening on `0.0.0.0`, port `5000`
* Routes:
    - `/`: display "Hello HBNB!"
    - `/hbnb`: display "HBNB"
* Use the option `strict_slashes=False` in the root definition

### 2. C is fun! - `2-c_route.py`
Script that starts a Flask web application:
* Must be listening on `0.0.0.0`, port `5000`
* Routes:
    - `/`: display "Hello HBNB!"
    - `/hbnb`: display "HBNB"
    - `/c/<text>`: display "C " followed by the value of the `text` variable (replace underscore `_` symbols with a space ` `)
* Use the option `strict_slashes=False` in the root definition

### 3. Python is cool! - `3-python_route.py`
* Must be listening on `0.0.0.0`, port `5000`
* Routes:
    - `/`: display "Hello HBNB!"
    - `/hbnb`: display "HBNB"
    - `/c/<text>`: display "C " followed by the value of the `text` variable (replace underscore `_` symbols with a space ` `)
    - `/python/(<text>)`: display "Python ", followed by the value of the `text` variable (replace `_` symbols with a space ` `)
        - The default value of `text` is "is cool"
* Use the option `strict_slashes=False` in the root definition

### 4. Is it a number? - `4-number_route.py`
* Must be listening on `0.0.0.0`, port `5000`
* Routes:
    - `/`: display "Hello HBNB!"
    - `/hbnb`: display "HBNB"
    - `/c/<text>`: display "C " followed by the value of the `text` variable (replace underscore `_` symbols with a space ` `)
    - `/python/(<text>)`: display "Python ", followed by the value of the `text` variable (replace `_` symbols with a space ` `)
        - The default value of `text` is "is cool"
    - `/number/<n>`: display "`n` is a number" only if `n` is an integer.
* Use the option `strict_slashes=False` in the root definition

### 5. Number template - `5-number_template.py`, `templates/5-number.html`
* Must be listening on `0.0.0.0`, port `5000`
* Routes:
    - `/`: display "Hello HBNB!"
    - `/hbnb`: display "HBNB"
    - `/c/<text>`: display "C " followed by the value of the `text` variable (replace underscore `_` symbols with a space ` `)
    - `/python/(<text>)`: display "Python ", followed by the value of the `text` variable (replace `_` symbols with a space ` `)
        - The default value of `text` is "is cool"
    - `/number/<n>`: display "`n` is a number" only if `n` is an integer.
    - `/number_template/<n>`: display a HTML page only if `n` is an integer:
        - `H1` tag: "Number: `n`" inside the tag `BODY`
* Use the option `strict_slashes=False` in the root definition

### 6. Odd or even? - `6-number_odd_or_even.py`, `templates/6-number_odd_or_even.html`
* Must be listening on `0.0.0.0`, port `5000`
* Routes:
    - `/`: display "Hello HBNB!"
    - `/hbnb`: display "HBNB"
    - `/c/<text>`: display "C " followed by the value of the `text` variable (replace underscore `_` symbols with a space ` `)
    - `/python/(<text>)`: display "Python ", followed by the value of the `text` variable (replace `_` symbols with a space ` `)
        - The default value of `text` is "is cool"
    - `/number/<n>`: display "`n` is a number" only if `n` is an integer.
    - `/number_template/<n>`: display a HTML page only if `n` is an integer:
        - `H1` tag: "Number: `n`" inside the tag `BODY`
    - `/number_odd_or_even/<n>`: display a HTML page only if `n` is an integer:
        - `H1` tag: "Number: `n` is `even|odd`" inside the tag `BODY`
* Use the option `strict_slashes=False` in the root definition

### 7. Improve engines - `models/engine/file_storage.py`, `models/engine/db_storage.py`, `models/state.py`
Before using Flask to display our HBNB data, we need to pudate some part of the engine:
Update `FileStorage`: (`models/engine/file_storage.py`)
* Add a public method `def close(self):`: call `reload()` method for deserializing the JSON file to objects.
Update `DBStorage`: (`models/engine/db_storage.py`)
* Add a public method `def close(self):`: call `remove()` method on the private session attribute (`self.__session`) or `close()` on the class `Session`.
Update `State`: (`models/state.py`) - if it's not already present
* If your storage engine is not `DBStorage`, add a public getter method `cities` to return the list of `City` objects from `storage` linked to the current `State`.

### 8. List of states - `web_flask/7-states_list.py`, `web_flask/templates/7-states_list.html`
Script that starts a Flask web application:
* Must be listening on `0.0.0.0`, port `5000`
* You must use `storage` for fetching data from the storage engine (`FileStorage` or `DBStorage`) => `from models import storage` and `storage.all(...)`
* After each request you must remove the current SQLAlchemy Session:
    - Declare a method to handle `@app.teardown_appcontext`
    - Call in this method `storage.close()`
* Routes:
    - `/states_list`: display a HTML page: (inside the tag `BODY`)
        - `H1` tag: "States"
        - `UL` tag: with the list of all `State` objects present in `DBStorage` sorted by `name` (A->Z)
            - `LI` tag: description of one `State`: `<state.id>: <B><state.name></B>`
* Import this 7-dump to have some data
* You must use the option `strict_slashes=False` in your route definition

### 9. Cities by states - `web_flask/8-cities_by_states.py`, `web_flask/templates/8-cities_by_states.html`
Script that starts a Flask web application:
* Must be listening on `0.0.0.0`, port `5000`
* You must use `storage` for fetching data from the storage engine (`FileStorage` or `DBStorage`) => `from models import storage` and `storage.all(...)`
* To load all cities of a `State`:
    - If your storage engine is `DBStorage`, you must use `cities` relationship
    - Otherwise, use the public getter method `cities`
* After each request you must remove the current SQLAlchemy Session:
    - Declare a method to handle `@app.teardown_appcontext`
    - Call in this method `storage.close()`
* Routes:
    - `/cities_by_states`: display a HTML page: (inside the tag `BODY`)
        - `H1` tag: "States"
        - `UL` tag: with the list of all `State` objects present in `DBStorage` sorted by `name` (A->Z)
            - `LI` tag: description of one `State`: `<state.id>: <B><state.name></B> + `UL tag: with the list of `City` objects linked to the `State` stored by `name` (A->Z)
                - `LI` tag: description of one `City`: `<city.id>: <B><city.name></B>`
* Import this 7-dump to have some data
* You must use the option `strict_slashes=False` in your route definition

### 10. States and State - `web_flask/9-states.py`, `web_flask/templates/9-states.html`
Script that starts a Flask web application:
* Must be listening on `0.0.0.0`, port `5000`
* You must use `storage` for fetching data from the storage engine (`FileStorage` or `DBStorage`) => `from models import storage` and `storage.all(...)`
* To load all cities of a `State`:
    - If your storage engine is `DBStorage`, you must use `cities` relationship
    - Otherwise, use the public getter method `cities`
* After each request you must remove the current SQLAlchemy Session:
    - Declare a method to handle `@app.teardown_appcontext`
    - Call in this method `storage.close()`
* Routes:
    - `/states`: display a HTML page: (inside the tag `BODY`)
        - `H1` tag: "States"
        - `UL` tag: with the list of all `State` objects present in `DBStorage` sorted by `name` (A->B)
    - `/states/<id>`: display a HTML page: (inside the tag `BODY`)
        - If a `State` object is found with this `id`:
            - `H1` tag: "State: "
            - `H3` tag: "Cities: "
            - `UL` tag: with the list of `City` objects linked to the `State` sorted by `name` (A->Z)
                - `LI` tag: description of one `City`: `<city.id>: <B><city.name></B>`
        - Otherwise:
            - `H1` tag: "Not found!"
* Import this 7-dump to have some data
* You must use the option `strict_slashes=False` in your route definition

### 11. HBNB filters - `web_flask/10-hbnb_filters.py`, `web_flask/templates/10-hbnb_filters.html`, `web_flask/static/`
Script that starts a Flask web application:
* Must be listening on `0.0.0.0`, port `5000`
* You must use `storage` for fetching data from the storage engine (`FileStorage` or `DBStorage`) => `from models import storage` and `storage.all(...)`
* To load all cities of a `State`:
    - If your storage engine is `DBStorage`, you must use `cities` relationship
    - Otherwise, use the public getter method `cities`
* After each request you must remove the current SQLAlchemy Session:
    - Declare a method to handle `@app.teardown_appcontext`
    - Call in this method `storage.close()`
* Routes:
    - `/hbnb_filters`: display a HTML page like `6-index.html`, which was done during the 0x01. AirBnB clone - Web static project
        - Copy files `3-footer.css`, `3-header.css`, `4-common.css`, and `6-filters.css` from `web_static/styles/` to the folder `web_flask/static/styles`
        - Copy files `icon.png` and `logo.png` from `web_static/images/` to the folder `web_flask/static/images`
        - Update `.popover` class in `6-filters.css` to allow scrolling in the popover and a max height of 300 pixels.
        - Use `6-index.html` content as source code for the template `10-hbnb_filters.html`:
            - Replace the content of the `H4` tag under each filter title (`H3` States and `H3` Amenities) by `&nbsp;`
        - `State`, `City`, and `Amenity` objects must be loaded from `DBStorage` and sorted by name (A->Z)
* You must use the option `strict_slashes=False` in your route definition
* Import this 10-dump to have some data
