AirBnB clone - Web framework

# GENERAL TOPICS

1. What is a Web Framework:
   A web framework is a software framework designed to aid the development of web applications including web services, web resources, and web APIs. It provides a structured way to build, organize, and maintain web applications by offering reusable code, enforcing best practices, and simplifying common tasks.

2. How to build a web framework with Flask:
   Flask is a lightweight web framework for Python. To build a web framework with Flask, you need to:

- Install Flask: pip install flask
- Create a Python script (e.g., app.py)
- Import Flask and create an instance:

  from flask import Flask
  app = Flask(**name**)

3.  How to define routes in Flask:
    In Flask, routes are defined using the @app.route() decorator. For example:

        @app.route('/')
        def home():
        return 'Hello, World!'

4.  What is a route:
    A route is a URL pattern mapped to a function that should be executed when the pattern is matched. It defines how the application responds to a specific HTTP request.

5.  How to handle variables in a route:
    You can include variable parts in a route URL by enclosing them in < >. For example:

        @app.route('/user/<username>')
        def show_user_profile(username):
        return 'User %s' % username

6.  What is a template:
    In the context of web development, a template is a file that contains a mix of HTML, variables, and control structures (e.g., loops, conditions). Templates are used to dynamically generate HTML pages with data from the server.

7.  How to create an HTML response in Flask by using a template:
    You can use the render_template function to render an HTML template. First, create a templates folder in your project and add HTML files. Then, use the templates in your routes:

        from flask import render_template

        @app.route('/hello/<name>')
        def hello(name=None):
        return render_template('hello.html', name=name)

8.  How to create a dynamic template (loops, conditions…):
    Inside your HTML template, you can use Jinja2 syntax, which Flask uses for templating. For example, using a loop:

        <ul>
            {% for item in items %}
                <li>{{ item }}</li>
            {% endfor %}
        </ul>

9.  How to display in HTML data from a MySQL database:
    To display data from a MySQL database, you need to connect Flask to the database (e.g., using Flask-SQLAlchemy). Fetch data from the database in your route and pass it to the template:

        from flask import render_template
        from flask_sqlalchemy import SQLAlchemy

        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/db_name'
        db = SQLAlchemy(app)

        @app.route('/users')
        def show_users():
            users = User.query.all()
            return render_template('users.html', users=users)

In the template (users.html), you can then use a loop to display user data.
