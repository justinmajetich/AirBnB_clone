# Web Flask

**Install Flask**

`pip3 install Flask`


## Task0,1

[What is a web flask route?](https://stackoverflow.com/questions/49915758/what-is-flask-route):

Running Flask means, basically, that you are running a webserver, also known as an HTTP server.

The Flask server will respond if a request is made for the URL defined in the route. This happens either when you visit the URL in your browser, or when some other HTTP client tries to access that URL.

The argument to`app.route()` is the *path* component of the URL. If you run a Flask server, the hostname of the machine it runs on will be the host component. The port it listens on will be the *port*. The *scheme* will be `http`. So if you ran the above example on a machine located at 52.12.34.56, listening on port 8088, you could reach the endpoint by going to`http://52.12.34.56:8088/`. You could also add a query-string or a fragment-id - the latter would be ignored, the former would be seen by the Flask server. So you could change the Python code in the function `hello_world` so that it returns different output depending on the query-string.

If you were using Flask in a formal production setting, you could have other servers doing things like proxying or load balancing involved in your setup. So potentially your users might visit a URL with a hostname which points to your load balancer, and that would pass on the request to Flask, possibly changing the URL in various ways. At the moment, you shouldn't worry about that. Just try and see if you can run a server and load the right page to see the text 'Hello World!' in your browser.

[**How to set the port and host**](https://stackoverflow.com/questions/49332853/how-set-the-host-and-the-port-of-a-flask-app-in-config-module)

* example: `app.run (host = "10.100.100.10", port = 9566)`
