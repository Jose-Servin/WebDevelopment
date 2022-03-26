<h1 align="center"> How to build a Flask Application </h1>

## The Flask "Hello World" site

A basic Flask app "Hello World" page can be built using the following code:

```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1> Hello World </h1> '


if __name__ == "__main__":
    app.run()
```

## Now, let's examine this code line by line.

1. First we import the Flask class from the flask package. <br>

```python
from flask import Flask
```

2. We create an application object as an instance of the Flask class. The `__name__` is a predefined name variable in
   Python. Which is set to the name of the module being used. This answers "are we running the script directly?"

```python
app = Flask(__name__)
```

3. Now we add pages to the application object we created from the Flask class. We do this by defining functions that
   return html.

```python
def index():
    return '<h1> Hello World </h1'
```

4. The function decorator directly links page to whatever route on your web application it should be at. For now, we
   route it to our home page/domain.

```python
@app.route('/')
```

5. At the button of the script we add `if __name__ == "__main__":`, which translates to "if you are running this script,
   run the application we created. "

```python
if __name__ == "__main":
    app.run()
```

## Basic Routes

How can we add multiple routes to our application (multiple pages)? The answer is in the `app.route()` function
decorator. The string parameter passed into the decorator determines the URL extension that will link to the function.
What this means is, this decorator parameter determines what "view"/"page" the user sees. <br>

Currently, our homepage/domain is locally represented at 'http://127.0.0.1:5000/'. The `/` represents our home page the
same way `/` represents our root directory.  <br>

Now, let's create another view called `page_two` which will be another html script that shows a simple html message.

1. We begin by decorating a view function with `app.route('/page_two')`.
2. We define the view function; the function decorated by the `app.route('page_two') and define the return value. What
   do you want the user to see when they visit this route/extension?
3. We run and test route by visiting 'http://127.0.0.1:5000/page_two' since that is the new route created.

### Creating a page_two route:

```python
from flask import Flask

app = Flask(__name__)


@app.route('/')  # this renders at http://127.0.0.1:5000/
def index():
    return '<h1> Hello World </h1> '


@app.route('/page_two')  # this will now render at 127.0.0.1:5000/page_two
def info():
    return "<h1> This is page two. </h1>"


if __name__ == "__main__":
    app.run()

```

## Flask Dynamic Routing

Dynamic Routing is when the URL route extension changes based on the situation. For example, we want the URL for user
Servin to be 'http://127.0.0.1:5000/Servin' and the URL for Baker to be 'http://127.0.0.1:5000/Baker'. That is, the URL
will change and update with the username of the person viewing the page. The standard URL for this
is 'www.site.com/user/unique_user_name'. <br>

Simple Dynamic Routing Example:

```python
@app.route('/monitor/<name>')  # the name in the route is passed to the view function as a parameter
def monitor(name):
    return f"<h1> This is a page for {name.upper()} </h1> "
```

## Flask Debug Mode

Debug mode allows you to see what type of error the Server and or application is encountering. This should be set to
False when application is ready for production. Let's create a route that returns back the 100th letter of the route
name.

1. Create route that returns 100th letter.

```python
@app.route('/debug/<name>')
def debug(name):
    return f"The 100th character of this name is {name[100]}."
```

Since there will be names with no 100th character this will return an error. But the error message will not be helpful.

```
Not Found
The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.
```

2. To be more helpful we set `app.run(debug=True)`. Now we get a more helpful error message.

```
IndexError
IndexError: string index out of range
```

The debug pin can be used to generate a console in the web application hosting to debug live. The pin is generated in
the terminal when the application runs and is needed to use the interactive/live debug functions.

## Template Basics

Realistically, we want to connect a view function to render HTML templates. Flask will automatically look for HTML
Templates in the <strong>templates</strong> directory.

1. We first create a templates' folder in the same directory level as our .py flask application.

```
/application.py
/templates
    /hello.html
```

2. We create the HTML page.
3. Using `from flask import render_templates` we define our view function and return the html template.

```python
@app.route('/')  # this renders at http://127.0.0.1:5000/
def index():
    return render_template('index.html')
```

## Updated Project Setup

To better organize our code, we will use the following directory setup.

* static folder for images
* templates for html pages
* application.py file for flask application.

```
/application.py
/templates
    /hello.html
/static
    /code_image.jpg
```

To reference the content inside the static folder we use `../static/file_name.jpg` which can read as "going back one
directory level, go into the static directory and use the file_name file."

## Template Variables

We want to be able to use Python code in our app, changing and updating variables and logic, and then send that
information to the template. To do this, we use the Jinja template engine. <br>

Jinja templating will let us directly insert variables from our Python code to the HTML file.

* Syntax: `{{some_variable}}`

1. We define a variable in our view function that we want to display in the HTML template.

```python
@app.route('/')  # this renders at http://127.0.0.1:5000/
def index():
    user_name = 'Servin'  # variable defined
    return render_template('index.html', user_name=user_name)
```

2. To insert this `user_name` into our HTML file we do the following:
    1. Define the variable in the render_template function as a parameter. Typically the variable and parameter are the
       same name.
    2. Use that parameter in the HTML template.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1> Howdy {{user_name}}</h1>

</body>
</html>
```

To summarize, we get to define whatever variables we want following standard python syntax. We then define a template
parameter and set it equal to the variable we defined. So template parameter == variable. Finally, in the HTML template,
we can use that variable using the syntax `{{parameter_name}}`.

## Template Control Flow
