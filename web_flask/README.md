# 0x04. AirBnB clone - Web framework

For this project, students are expected to look at this concept:

- [AirBnB clone](https://intranet.hbtn.io/concepts/74)

## Resources
#### Read or watch:

- [What is a Web Framework?](https://jeffknupp.com/blog/2014/03/03/what-is-a-web-framework/)
- [A Minimal Application](https://flask.palletsprojects.com/en/1.0.x/quickstart/#a-minimal-application)
- [Routing](https://flask.palletsprojects.com/en/1.0.x/quickstart/#routing) (except “HTTP Methods”)
- [Rendering Templates](https://flask.palletsprojects.com/en/1.0.x/quickstart/#rendering-templates)
- [Synopsis](https://jinja.palletsprojects.com/en/2.9.x/templates/#synopsis)
- [Variables](https://jinja.palletsprojects.com/en/2.9.x/templates/#variables)
- [Comments](https://jinja.palletsprojects.com/en/2.9.x/templates/#comments)
- [Whitespace Control](https://jinja.palletsprojects.com/en/2.9.x/templates/#whitespace-control)
- [List of Control Structures](https://jinja.palletsprojects.com/en/2.9.x/templates/#list-of-control-structures) (read up to “Call”)
- [Flask](https://palletsprojects.com/p/flask/)
- [Jinja](https://jinja.palletsprojects.com/en/2.9.x/templates/)

## Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/2012/04/feynman-technique/), **without the help of Google:**

### General
- What is a Web Framework
- How to build a web framework with Flask
- How to define routes in Flask
- What is a route
- How to handle variables in a route
- What is a template
- How to create a HTML response in Flask by using a template
- How to create a dynamic template (loops, conditions…)
- How to display in HTML data from a MySQL database

## Requirements
### **Python Scripts**
- Allowed editors: ```vi```, ```vim```, ```emacs```
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using ```python3``` (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly ```#!/usr/bin/python3```
- A ```README.md``` file, at the root of the folder of the project, is mandatory
- Your code should use the ```PEP 8``` style (version 1.7)
- All your files must be executable
- The length of your files will be tested using ```wc```
- All your modules should have documentation (```python3 -c 'print(__import__("my_module").__doc__)'```)
- All your classes should have documentation (```python3 -c 'print(__import__("my_module").MyClass.__doc__)'```)
- All your functions (inside and outside a class) should have documentation (```python3 -c 'print(__import__("my_module").my_function.__doc__)'``` and ```python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'```)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## HTML/CSS Files
- Allowed editors: ```vi```, ```vim```, ```emacs```
- All your files should end with a new line
- A ```README.md``` file at the root of the folder of the project is mandatory
Your code should be W3C compliant and validate with [W3C-Validator](https://github.com/holbertonschool/W3C-Validator) (except for jinja template)
- All your CSS files should be in the ```styles``` folder
- All your images should be in the ```images``` folder
- You are not allowed to use ```!important``` or ```id``` (```#...``` in the CSS file)
- All tags must be in uppercase
- Current screenshots have been done on ```Chrome 56.0.2924.87```.
- No cross browsers

## More Info
### **Install Flask**
```bash
$ pip3 install Flask
```
![image](https://github.com/Cristhian-Carbonell/AirBnB_clone_v2/blob/master/web_flask/images/hbnb_step3.png)

<div class="ytp-cued-thumbnail-overlay" data-layer="4" style=""><div class="ytp-cued-thumbnail-overlay-image" style="background-image: url(&quot;https://i.ytimg.com/vi_webp/lzs4nQOiZQY/sddefault.webp&quot;);"></div><button class="ytp-large-play-button ytp-button" aria-label="Reproducir"><svg height="100%" version="1.1" viewBox="0 0 68 48" width="100%"><path class="ytp-large-play-button-bg" d="M66.52,7.74c-0.78-2.93-2.49-5.41-5.42-6.19C55.79,.13,34,0,34,0S12.21,.13,6.9,1.55 C3.97,2.33,2.27,4.81,1.48,7.74C0.06,13.05,0,24,0,24s0.06,10.95,1.48,16.26c0.78,2.93,2.49,5.41,5.42,6.19 C12.21,47.87,34,48,34,48s21.79-0.13,27.1-1.55c2.93-0.78,4.64-3.26,5.42-6.19C67.94,34.95,68,24,68,24S67.94,13.05,66.52,7.74z" fill="#f00"></path><path d="M 45,24 27,14 27,34" fill="#fff"></path></svg></button></div>
</div>
