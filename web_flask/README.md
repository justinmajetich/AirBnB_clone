# Web Flask

This was a sub-project within AirBnB in which I began working with Flask
and Jinja2. In this project, I began integrating the back-end storage engine
with the web static HTML/CSS pages written earlier.

Files 0 - 6 were introductory tasks familiarizing myself with
using Flask. Files 7 forward involved gradually putting together more and more
complex Jinja templates based on the HBnB HTML pages.

The most complete Flask/Jinja app-template combo in this directory is defined
in Flask module [100-hbnb.py](./100-hbnb.py) and Jinja template
[100-hbnb.html](./100-hbnb.html).

To run the Flask app, execute the following command from the root directory
of the project:

```
~ $ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost
HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.100-hbnb
```

The app can be accessed at `0.0.0.0:5000/hbnb`.

Screenshots:
<p align="center">
  <img src="https://github.com/anteneh2121/AirBnB_clone_v2/blob/main/web_flask/static/images/hbnb_screenshot_0.png"
       alt="HolbertonBnB logo">
</p>

---

<p align="center">
  <img src="https://github.com/anteneh2121/AirBnB_clone_v2/blob/main/web_flask/static/images/hbnb_screenshot_1.png"
       alt="HolbertonBnB logo">
</p>

---

<p align="center">
  <img src="https://github.com/anteneh2121/AirBnB_clone_v2/blob/main/web_flask/static/images/hbnb_screenshot_2.png"
       alt="HolbertonBnB logo">
</p>
