<<<<<<< HEAD
## AirBnB clone - Web framework

### Learning Objectives
- [What is a Web Framework](https://intelegain-technologies.medium.com/what-are-web-frameworks-and-why-you-need-them-c4e8806bd0fb)

- How to build a web framework with Flask
    * `HTTP Server Integration`
    * `Routing`
    * `Request and Response Handling`
    * `Middleware: allow for the insertion of intermediate processing steps into the request-response cycle`
    * `Templating`
    * `Error Handling`
    * `Extension and Customization:  allowing developers to add their own functionality through plugins, extensions, or custom middleware`

- How to define routes in Flask
`from flask import Flask

app = Flask(__name__)

@app.route('/user/<username>')  # Route pattern with a variable part <username>
def show_user_profile(username):
    # This function will receive the value of the variable part (<username>) as an argument
    return f'User: {username}'

@app.route('/post/<int:post_id>')  # Route pattern with a variable part <post_id> which is restricted to integers
def show_post(post_id):
    # This function will receive the value of the variable part (<post_id>) as an integer argument
    return f'Post ID: {post_id}'

if __name__ == '__main__':
    app.run(debug=True)
`
- [What is a route](https://flask.palletsprojects.com/en/2.3.x/quickstart/#routing)

- How to handle variables in a route
 
- [What is a template](https://flask.palletsprojects.com/en/2.3.x/quickstart/#rendering-templates)

- How to create a HTML response in Flask by using a template
   - To create an HTML response in Flask using a template, you need to follow these steps:

	1. Create an HTML template file.
	2. Render the template in your Flask route function.
- How to create a dynamic template (loops, conditions…)
   * Can use the Jinja2 templating engine

- How to display in HTML data from a MySQL database
Follow this steps:
	1. Set up a connection to your MySQL database.
	2. Write a Flask route to fetch data from the database.
	3. Pass the fetched data to an HTML template for rendering.
=======
web_flask
>>>>>>> 13bd557badf43ae4a715ced2f930b9825a0454b5
