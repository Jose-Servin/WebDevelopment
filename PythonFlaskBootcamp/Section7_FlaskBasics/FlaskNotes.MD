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

We are able to use Python control/condition statements inside our HTMl template. For example, if we want to create a
list of each element in an iterable we can do the following:

### for loop

```html

<ul>
    {% for letter in name%}
    <li>{{letter}}</li>
    {%endfor%}
</ul>
```

Control flow syntax is inserted between `{%%}`.

### if statement

Let's first create a list of users to check if a certain user is in that list.

```python
@app.route('/')
def index():
    name = 'Servin'
    name_list = list(name)
    users = ['Bella', 'Camila', 'Servin']  # creating a list of users 
    return render_template('index.html', name=name, name_list=name_list, users=users)
```

Next we add the `for` control flow in our HTML template.

```html
Let's see if Baker is in the users:
{% if 'Baker' in users %}
<p> Found you Baker!</p>
{% else %}
<p>Baker is not a user....</p>
{% endif %}
```

### Real Case: Login message

First we create the variable user_logged_in and set it equal to True.

```python
@app.route('/')
def index():
    name = 'Servin'
    name_list = list(name)
    user_logged_in = True
    users = ['Bella', 'Camila', 'Servin']  # creating a list of users 
    return render_template('index.html', name=name, name_list=name_list, users=users, user_loggedin=user_logged_in)
```

Next we use that variable in our HTML template to format special messages to show when the condition is either True or
False.

```html

Special Message if you are logged in!
{% if user_logged_in%}
<h2>Welcome! Thank you for logging in! </h2>
{%else%}
<h2>Please log in to continue.</h2>
{% endif %}
```

Key things to remember:

* The syntax used for python in HTML templates is `{% <python goes here> %}`.
* `for` and `if` statements have to be ended with `{% endfor %}` and `{% endif %}`.

## Template Inheritance

Template inheritance is used to minimize the amount of code you re-type since by definition, template inheritance is the
re-use of page/template components that are set up in a `base.html` file. <br>

To re-use the code from this `base.html` template, we use the `{% extend "base.html" %` and `{% block %}`
statements. <br>

Visually, this looks like:
<img src="static/template_inheritance.png">

### Implementation

We start by defining various HTML templates. We have `base.html`, `home.html` and `user.html`. Next, we define the view
functions that will return the HTML templates along with any variables created.

```python
@app.route('/')  # this renders at http://127.0.0.1:5000/
def home():
    return render_template('home.html')


@app.route('/user/<name>')
def user_page(name):
    return render_template('user.html', name=name)
```

1. Set up `base.html` containing HTML elements that will be used in various templates. In other words, in `base.html`
   you place the HTML elements that will be re-used between templates.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>MyWebsite</title>
    <!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <!-- JavaScript Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p"
            crossorigin="anonymous"></script>
</head>
<body>

<!-- NavBar setup-->
<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
        <a class="navbar-brand" href="#">Navbar</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup"
                aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
            <div class="navbar-nav">
                <a class="nav-link active" aria-current="page" href="#">Home</a>
                <a class="nav-link active" href="#">Features</a>
                <a class="nav-link active" href="#">Pricing</a>
            </div>
        </div>
    </div>
</nav>

{% block content %}

{% endblock %}

</body>
</html>
```

Here we have our `base.html` page defined with a simple Nav Bar.

2. Build on `home.html` using components from `base.html` by defining block contents.

```html
{% extends "base.html" %}

{% block content %}
<h1> This is the home page</h1>

{% endblock %}
```

Here home.html will inherit the nav bar defined in base.html, along with having unique html elements.

## Filters

A great way to quickly change/edit a variable passed to a template.

* syntax used : `{{ variable | filter }}`

```html
<h1> Howdy {{name}}</h1>
```

This renders as `Howdy jose`. If we want to capitalize the name variable, we would use `{{ name | capitalize }}`.

```html
<h1> Howdy {{name | capitalize}}</h1>
```

## url_for() help function

The `url_for()` helper function allows us to easily connect other template pages or files within our templates.

1. Link to different views <br>
   To link to a different view function, you pass the view function name. So now when you click Home, it will run the
   home view function and return back whatever template it returns. For this example it's `home.html`.

```html
<a class="nav-link active" aria-current="page" href="{{url_for('home')}}">Home</a>


```

2. Link to static file content. <br>
   To link to a static file you pass the folder name `static` along with `filename`. Here when you click on `View Code`
   you will open the image.

```html
<a href="{{url_for('static',filename='post-img.jpg')}}">View code</a>

```

## Template Forms

Template forms allow you to gather user input information using a form structure. For this example, we will gather
the first and last name of the user and greet them. We will also build a custom 404 page for redirection if an
invalid URL is attempted. <br>

Our project structure is:

* basics.py for backend running
* A base.html page for template inheritance
* home.html
* signup.html
* thankyou.html

The backend is fairly simple, we define our `route` functions and for this case we added a 404 error handler in case
the user tries to access a page not found.

```python
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/signup-page')
def signup():
    return render_template('signup.html')


@app.route('/thankyou')
def thankyou():
    first_name = request.args.get('fname')
    last_name = request.args.get('lname')
    return render_template('thankyou.html', first_name=first_name, last_name=last_name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404_error.html'), 404


if __name__ == '__main__':
    app.run(debug=True)

```

Now, `base.html` contains our nav bar and footer which will be present in all pages. `home.html` is where we ask the
user is they would like to sign up. `signup.html` is where we gather the `first` and `last` name of the user,
followed by a simple thank-you message displayed via `thankyou.html`. <br>

Here is where we also introduced the `url_for()` function which we used to tied together views and functions. For
example:

```html

<form action="{{url_for('thankyou')}}">
    <label for="fname">First name:</label>
    <input type="text" id="fname" name="fname">
    <label for="lname">Last name:</label>
    <input type="text" id="lname" name="lname">
    <input type="submit" value="submit-form">
</form>
```

Here we are saying "once the user submits, run the view function in the backend called `thankyou`". This in turn,
will render a different view. <br>

A good place for this function is in our `base.html` page for home buttons or buttons that should always take a user
to a specific view. We defined this `url_for()` function in the base view and then inherit it to all views that
should have those common elements present as well. <br>

Another concept introduced was gathering user info submitted which is done using `request.args.get(<attribute name>)
`. This allowed us to use the user input in `thankyou.html` view by defining and referncing the gathered variables.

```html
{% extends "base.html" %}
{% block title %}Thank you Page{% endblock %}


{% block content %}

<h2> Thank you for signing-up! {{first_name | capitalize}} {{last_name | capitalize}} </h2>
<a href="{{url_for('index')}}"> Home</a>

{% endblock %}
```

## A simple username checker

Our html code looks like:

```html
{% extends "base.html" %}
{% block title %}Home{% endblock %}


{% block content %}

<h2> Welcome to our home page. </h2>
<h3> Fill out the form with a Username to check if it's valid: </h3>

<ul>
    <li>Must have an upper case letter somewhere.</li>
    <li>Must have a lower case letter somewhere.</li>
    <li>Must have a number at the end.</li>
</ul>

<form action={{url_for('report')}}>
    
    <label for="username">Username:</label>
    <input type="text" id="username" name="username">
    <input type="submit" value="Submit">

</form>
{% endblock %}
```

```html
{% extends "base.html" %}
{% block title %}Report{% endblock %}


{% block content %}

<h2> Results..... </h2>


{% if  valid_username %}
<h3> Congrats, you have a valid username! </h3>

{% else %}
<ul>
    {% if not has_uppercase %}
    <li> Username does not have an uppercase letter.</li>
    {% endif %}
    {% if not has_lowercase %}
    <li> Username does not have a lowercase letter.</li>
    {% endif %}
    {% if not has_number %}
    <li> Username does not end with a digit.</li>
    {% endif %}

</ul>
{% endif %}

<a href="{{url_for('index')}}">Go back home</a>

{% endblock %}
```

In the backend we do all the logic checking; we simply pass back boolean values for each condition check.

```python
from flask import Flask, render_template, request
import re

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/report')
def report():
    username = request.args.get('username')

    has_uppercase = False
    has_lowercase = False
    has_number = False

    has_uppercase = any(i.isupper() for i in username)
    has_lowercase = any(i.islower() for i in username)
    has_number = username[-1].isdigit()

    valid_username = has_number and has_uppercase and has_lowercase

    return render_template('signup.html', valid_username=valid_username, has_number=has_number,
                           has_lowercase=has_lowercase,
                           has_uppercase=has_uppercase)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404_error.html'), 404


if __name__ == '__main__':
    app.run(debug=True)

```

## Introduction to Flask Forms

Flask Forms are built using Flask WTF Form class. General steps to building out Forms on Flask are the following:

1. Configure a secret key
2. Create a WTForm class
    1. Define attributes for each part of the form
3. Set up view functions
    1. add methods = ['GET','POST]
    2. create instance of class
    3. handle form submission

## Flask Forms Example

```python
# Section 9: Forms with Flask
from flask import Flask, render_template
from flask_wtf import FlaskForm
# from wtforms you import certain fields and provide parameters in the class buildup
from wtforms import StringField, SubmitField

# Step 1: create application
app = Flask(__name__)

# Step 2: configure secret key to use with CSRF (cross-site request forgery)
# app.config is a configuration dictionary for our app
app.config['SECRET_KEY'] = 'mysecretkey123'


# Step 3: create WTF Form class
# inherit from FlaskForm
class InfoForm(FlaskForm):
    # define class attributes
    department = StringField("What department do you work in? ")
    submit = SubmitField("Submit")


# Step 4: create view function that creates instance of WTF form class and checks if it's a valid submission
@app.route('/', methods=['GET', 'POST'])
def index():
    # set department variable equal to False, different from the department attribute defined in our class
    department = False
    # create instance of our InfoForm class 
    form = InfoForm()

    if form.validate_on_submit():
        # grab department from form (grabs data submitted for this attribute)
        department = form.department.data
        # reset this attribute to an empty string so the StringField doesn't show previous entry
        form.department.data = ''

    return render_template('Flask_Forms_Index.html', form=form, department=department)


if __name__ == '__main__':
    app.run(debug=True)

```

After defining the simple backend using wtforms class we define our index.html page.

```html
<p>
    <!-- originally set to False so at start up else block runs but then grabs Form data entered -->
    {% if department %}
    The department you work at is: {{department}}. <br>
    Update it in the form below:
    
    {% else %}
    Please enter your department:
    
    {% endif %}
</p>


<form method="POST">
    <!-- This is for the CSRF security feature, accessible because we inherit from FlaskForm in our class setup.-->
    {{ form.hidden_tag() }}
    <!-- for fields defined such as StringField we can access label or execute which will create element -->
    <!-- form.department.label accesses the text inside the () for our defined StringField -->
    <!-- form.department() will run the function; create a fill-in box. -->
    {{ form.department.label }} {{ form.department() }}
    <!-- Here we are calling the submit method defined in out InfoForm class -->
    {{ form.submit() }}
</form>
```

## Form Fields

* Every possible HTML form field has a corresponding wtforms class you can import.
* wtforms also has validators you can easily insert.
* Validators can perform checks on the form data, such as requiring a field to be filled.

We begin with a new import statement:

```python
from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateTimeField, RadioField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
```

Next we define our app and secret key configuration:

```python
# Step 1: define app
app = Flask(__name__)

# Step 2: configure secret key
app.config['SECRET_KEY'] = 'mysecretkey123'
```

Then our class that inherits from FlaskForm: <br>
In this class, we use the wtforms fields that were imported to define the attributes.

```python
# Step 3: Define Form class with attributes; built with wtforms
class InfoForm(FlaskForm):
    # for validators we create an instance in the validators list
    department = StringField('What department are you in? ', validators=[DataRequired()])
    high_access = BooleanField('Do you have level 5 or above access? ')
    # choices in RadioField are a list of Tuple pairs consisting of (value, label)
    access_level = RadioField('Please select your access level: ',
                              choices=[
                                  ('access_5', '5'),
                                  ('access_6', '6'),
                                  ('access_7', '7')
                              ])
    information = SelectField('Please select the information you wish to see: ',
                              choices=[
                                  ('payroll', 'Payroll'),
                                  ('timecard', 'Timecard'),
                                  ('salary', 'Salary'),
                                  ('master_info', 'Master Info')
                              ])

    reason = TextAreaField()
    submit = SubmitField('Submit')
```

Next we define our view functions: <br>
Here we introduce the nested return statements.

1. `return redirect(url_for('thank_you'))` will redirect the user to the render_template the view function
   'thank_you' returns. <strong> ONLY IF </strong> the user correctly fills in the form; correctly means all validators
   are True.
2. The second return statement `return render_template('Flask_Forms_One_Index.html'), form=form)` is the return
   statement for the view function so, it's what the user will see.

```python
# Step 4: Define view functions
@app.route('/', methods=['GET', 'POST'])
def index():
    form = InfoForm()

    # Only upon submission of form will this be True and user will be redirected to html 'thank_you' renders
    # validate_on_submit will check validators from attribute's; if one is False, user will not be redirected.
    if form.validate_on_submit():
        '''
        In order to pass the data to another template automatically we will use the session object from Flask import.
        Unlike a cookie, session data is stored on the server and a session is just a time interval from when client 
        logs into server and then logs out of it. So the data is stored in a temporary directory on the server. 
        
        This is essentially a way to temporarily hold information about a session that lasted x amount of time for a
        specific user and report it back. 
        
        '''
        # grab session object and treat it as dictionary by building it using dict_value = value from tuple
        session['department'] = form.department.data  # this will report back the value from the tuple pairs
        session['high_access'] = form.high_access.data
        session['access_level'] = form.access_level.data
        session['information'] = form.information.data
        session['reason'] = form.reason.data

        # only upon correct form submission does the user get re-directed to the render_template of the view function
        return redirect(url_for('thankyou'))  # thankyou is the name of the view function
    # rendering the Flask_Forms_One_Index.html; this is the page rendered when view function runs
    return render_template('Flask_Forms_One_Index.html', form=form)


@app.route('/thankyou', methods=['GET', 'POST'])
def thankyou():
    return render_template('Flask_Forms_One_ThankYou.html')
```

Lastly, we include our run statement:

```python
if __name__ == "__main__":
    app.run(debug=True)
```

Next we move on to the front-end. <br>
Index template for this project is shown below.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Flask Forms</title>
</head>
<body>
<h1> Welcome to the info access bar: </h1>
<form method="POST">
    {{form.hidden_tag()}}
    {{form.department.label}} {{form.department()}}
    <br>
    {{form.high_access.label}} {{form.high_access()}}
    <br>
    {{form.access_level.label}} {{form.access_level()}}
    <br>
    {{form.information.label}} {{form.information()}}
    <br>
    Please state your reason?
    <br>
    {{form.reason()}}
    <br>
    {{form.submit.label}} {{form.submit()}}

</form>
</body>
</html>
```

Thank you page is as follows:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Flask Forms</title>
</head>
<body>
<h1> Thank you for providing your information. Processing the following....</h1>
<ul>
    <li>Department: {{session['department']}}</li>
    <li> High Access: {{session['high_access']}}</li>
    <li> Access Level: {{session['access_level']}}</li>
    <li> Information Requested: {{session['information']}}</li>
    <li> Reason: {{session['reason']}}</li>
</ul>

</body>
</html>
```

## How to flash a message to a user

* Often, we want to send a message to the user that we don't need to save or fix permanently to the template page.
* We can <strong> flash </strong> a message to the user that can then be closed.

To do this, you import a flash function from Flask and then connect to some Bootstrap code. <br>

Our backend looks like:

```python
from flask import Flask, render_template, flash, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

# Next we set up our application and security key:
app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey123'


# We move on to creating a simple form.
class SimpleForm(FlaskForm):
    submit = SubmitField('Click Me')


# here we define our index view function

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SimpleForm()

    if form.validate_on_submit():
        flash('You just clicked the button')

        return redirect(url_for('index'))

    return render_template('home.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)

```

Next we move on the front end `home.html` page building.

* the function `get_flashed_messages()` is what gets passed back when we use `flash` in Flask.
* In other words, when we use `flash` Flask will automatically call the function `get_flashed_messaged()`.
* We use a `for` loop in case we have multiple flashed messages.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
    <title> Home page </title>

</head>
<body>


{% for message in get_flashed_messages() %}

<div class="alert alert-warning alert-dismissible fade show" role="alert">
    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close">
    </button>
    {{message}}
</div>

{% endfor %}


<form method="POST">
    {{form.hidden_tag()}}
    {{form.submit()}}
</form>


<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2"
        crossorigin="anonymous"></script>
</body>
```

In this section, we combine bootstrap's alert with our defined flashed text.

```html

<div class="alert alert-warning alert-dismissible fade show" role="alert">
    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close">
    </button>
    {{message}}
</div>
```

So now, our message will appear inside the bootstrap alert. <br>

The last section of our HTML simply creates that `submit` button so that the user can see the flash message. Again
here, we use the `form` element.

```html

<form method="POST">
    {{form.hidden_tag()}}
    {{form.submit()}}
</form>

```

## Flashing session data to the user

In the backend we set up our form and flash message as well as the render files.

```python
from flask import Flask, render_template, flash, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

# Next we set up our application and security key:
app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey123'


# We move on to creating a simple form.
class SimpleForm(FlaskForm):
    department = StringField('What department are you in? ')
    submit = SubmitField('Submit')


# here we define our index view function

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SimpleForm()

    if form.validate_on_submit():
        session['department'] = form.department.data
        flash(f"You are in the {session['department']} department. ")

        return redirect(url_for('index'))

    return render_template('home.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)

```

For the front-end we use the `get_flashed_messages()'` and build out the form which will capture the user input data.
Note here that the actual "data grabbig" occurs in the back-end when we
define `flash(f"You are in the {session['department']} department. ")`. <br>

The front-end is simple two processes.

1. iterate through the flashed messages
2. build out the form

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
    <title> Home page </title>

</head>
<body>


{% for message in get_flashed_messages() %}

<div class="alert alert-warning alert-dismissible fade show" role="alert">
    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close">
    </button>
    {{message}}
</div>

{% endfor %}


<form method="POST">
    {{form.hidden_tag()}}
    {{form.department.label}} {{form.department()}}
    {{form.submit()}}
</form>


<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2"
        crossorigin="anonymous"></script>
</body>
```

## Flask and Databases High level Introduction

By default, Flask comes with SQLite which is a simple database engine that can handle simple web application needs.
Top handle boundary is close to the 100,000 hits per day. <br>

To connect Python, Flask and SQL we will need an `ORM (Object Relational Mapper)`. Which is just "something" that
allows us to convert python code to SQL commands. Most common ORM for python is `SQL Alchemy`. <br>

We can map out our abstraction levels as being:

1. SQL Database
2. SQL Alchemy
3. Flask SQL Alchemy

## How to introduce a database

1. Set up SQLite Database in Flask App
2. Create a Model in Flask App
3. Perform basic CRUD on our model

## How to set up a SQLite database

1. Create Flask App
2. Configure Flask App for SQLAlchemy
3. Pass our application into SQLAlchemy class call

These steps can be accomplished with (`basic.py`):

```python
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
# __file__ --> basics.py
# the os.path.dirname is flaskenv/basics.py
# the abspath is the "full path" which when printed is /Users/joseservin/WebDevelopment/flaskenv

# 1. Create Flask App
app = Flask(__name__)

# 2. Configure Flask App for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join((basedir, 'data.sqlite'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 3. Pass our application into SQLAlchemy class call

db = SQLAlchemy(app)

```

## Notes on Model in Flask

* Models directly link to a table in a SQL database.
* You do not need to create the table manually in SQL.
* We create a `Model` class in Python that generates the table for us.
* "Models" == Tables in our Database.
* By default, the `__tablename__` is the name of our Model class `class Department(db.Model):`.

## How to create a Model in Flask (similar to creating a Form)

1. Create a Model class
2. Inherit from `db.Model`
3. Optionally provide a table name
4. Add in table columns as attributes
5. Add in methods for `__init__` and `__repr__`.

Note `__repr__` is simply the text representation of that object. <br>

To build a column we define `column_name = db.Column(db.DataType, column_property)`.

We build a database with the following code (`basics.py`):

```python
# HOW TO CREATE A MODEL
class Departments(db.Model):
    # create columns for table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    security_level = db.Column(db.Integer)

    def __init__(self, name, security_level):
        self.name = name
        self.age = security_level

    def __repr__(self):
        rep = f"The {self.name} has a security level of {self.security_level}. "
        return rep

```

## How to save information to the Database

First we create a new python file called `setupdatabase.py` and import the `db` and `Departments` which is also our
Model name. In the code below we are transforming our Model into a database table and creating instances of that
Model which will be saved to the database using python commands.

```python
from basics import db, Departments

# CREATES ALL THE TABLES, ESSENTIALLY TRANSFORMING MODEL CLASS --> DB.TABLE
db.create_all()

# CREATE DEPARTMENT INSTANCES

Tech = Departments('PepsiCo Tech Team', 5)
AM = Departments('Account Managers', 3)
CM = Departments('Carrier Managers', 3)
Data_Analyst = Departments('Data Analyst', 8)
Customer_Service = Departments('Customer Service', 1)

# SAVING DEPARTMENT INSTANCES TO THE DATABASE 
db.session.add_all([Tech, AM, CM, Data_Analyst, Customer_Service])
db.session.commit()

print(Tech.id)
print(AM.id)
```

After running `setupdatabase.py` we can check if the instances were created correctly by running `print(Department.
query.all())` which should return in our terminal:

```commandline
[The PepsiCo Tech Team has a security level of 7. , 
The Account Managers has a security level of 3. , 
The Carrier Managers has a security level of 3. , 
The Data Analyst has a security level of 8. , 
The Customer Service has a security level of 1. ]
```

We should also see a `data.sqlite` file in our project folder present.

## Performing CRUD

To perform CRUD operations on our database, we must be cautious and not call upon instances that no longer exist in
the database. For our example we followed the code below in a file called `crud.py`:

```python
from basics import db, Departments

## CREATE ##

extra_dept = Departments('Extra Department', 10)
db.session.add(extra_dept)
db.session.commit()

## READ ###
all_departments = Departments.query.all()  # returns list of all department objects in the database table
print(all_departments)

# SELECT BY ID
department_id_1 = Departments.query.get(1)  # This returns the Object with ID 1
print(department_id_1.name)  # this prints out the specific attribute of that object returned

# FILTER (THIS PRODUCES SQL CODE FOR US)
AM_dept = Departments.query.filter_by(name='Account Managers')
print(AM_dept.all())

### UPDATE
first_dept = Departments.query.get(1)
first_dept.security_level = 7
db.session.add(first_dept)  # adding back in the edited Department object
db.session.commit()

#### DELETE
dept_to_del = Departments.query.get(6)
db.session.delete(dept_to_del)
db.session.commit()

## Check changes
all_departments = Departments.query.all()
print(all_departments)

```

If any issues arise we can simply delete the `data.sqlite` file/database and re-run `setupdatabase.py` and then
`crud.py` to avoid any errors. This is not best practices but simply a quick way to "restart" when first learning
about Flask and Flask Databases.

## Flask Migrate

"Migrating" refers to the transfer of any changes done to your "Model" (DB.TABLE). Most commonly this can be adding
a new column or other Model changes. <br>

This migration is done using `Flask-Migrate` which is a python package that is used to ensure any changes done to
our model take effect on our database.  <br>

The first step we must take is set the `FLASK_APP` environment variable. (`export FLASK_APP=myapp.py`). This let's
Flask Migrate know which file represents our Flask Application.

The 4 main commands are:

1. `export FLASK_APP=myapp.py`
2. `flask db init` : sets up the migration directory.
3. `flask db migrate -m "some message"` sets up the migration file
4. `flask db upgrade`: updates the database with the migration

`Migrate(app, db)` connects our application to our database in order to add on Migration capabilities to run terminal
commands. We do this because we've already run the `basics.py` file which holds our `Model` class. If we were to add
a column to this class our database would not be updated with these changes. We need to "migrate" that information
to the database. After running the 4 commands, our application.py file is now synced with our database.

After introducing a new column to our Model/Table our `basics.py` file contains the following:

```python
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
# __file__ --> basics.py
# the os.path.dirname is flaskenv/basics.py
# the abspath is the "full path" which when printed is /Users/joseservin/WebDevelopment/flaskenv

# CREATING FLASK APP
app = Flask(__name__)

# SQLALCHEMY CONFIGURATIONS
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# DEFINING DATABASE
db = SQLAlchemy(app)

# MIGRATING APP AND DB
Migrate(app, db)


# HOW TO CREATE A MODEL
class Departments(db.Model):
    # create columns for table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    security_level = db.Column(db.Integer)
    incentive = db.Column(db.BOOLEAN)

    def __init__(self, name, security_level, incentive):
        self.name = name
        self.security_level = security_level
        self.incentive = incentive

    def __repr__(self):
        rep = f"The {self.name} has a security level of {self.security_level}. Incentive? {self.incentive} "
        return rep

```

To introduce a migration we do:

1. `flask db migrate -m "message about migration change"`
2. `flask db upgrade`

## Flask Relationships

It is common for relationships to exists between Models "Tables" in our Application and in general. These relations
are formed by a common column. The simples example can be:

* Customer Table
    * Customer ID (Primary Key)
    * Customer Name
    * Customer Address
    * Order Number (Foreign Key)
* Order Table
    * Order ID (Primary Key)
    * Order Quantity
    * Order Amount
    * Order Number (Foreign Key)

These two tables are related via an "Order Number" column.

We are going to create many departments that have a one-to-many relationship with employees and a one-to-one
relationship between Department and Managers.

### One-to-many relationship

We can create a one-to-many relationship between Departments and Employees. In essence there can be many employees
working for a specific Department. To define a relationship between our Models/Tables we
use `employees = db.relationship('Employees', backref='department', lazy='dynamic')`. Where:

* first argument: `Model who the relationship is with`
* `backref='departments'` adds a reference to our Employee models to remember it is related to the Departments model.
* `lazy="dynamic"` defines how to data will get loaded.
* `uselist=False` this parameter defines what to return, by default this is True

Our final `basics.py` script contains the following:

```python
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
# __file__ --> basics.py
# the os.path.dirname is flaskenv/basics.py
# the abspath is the "full path" which when printed is /Users/joseservin/WebDevelopment/flaskenv

# CREATING FLASK APP
app = Flask(__name__)

# SQLALCHEMY CONFIGURATIONS
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# DEFINING DATABASE
db = SQLAlchemy(app)

# MIGRATING APP AND DB
Migrate(app, db)


# HOW TO CREATE A MODEL
class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    security_level = db.Column(db.Integer)
    # ONE-TO-MANY RELATIONSHIP (ONE DEPARTMENT CAN HAVE MANY EMPLOYEES)
    employees = db.relationship('Employee', backref='department', lazy='dynamic')

    # ONE-TO-ONE RELATIONSHIP (ONE DEPARTMENT HAS ONE MANAGER)
    manager = db.relationship('Manager', backref='department', uselist=False)

    def __init__(self, name, security_level):
        self.name = name
        self.security_level = security_level

    def __repr__(self):
        if self.manager:
            return f"Department name: {self.name} | Manager {self.manager.first_name} {self.manager.last_name}"
            # self.manager.name is an attribute from the Manager class
        else:
            return f"{self.name} department has no Manager assigned. "

    def report_employees(self):
        print(f"{self.name} department has these employees: ")
        for employee in self.employees:
            print(f"{employee.first_name} {employee.last_name}")  # this is an attribute from the Employees class


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)

    # CONNECTING EMPLOYEES WITH DEPARTMENTS
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))

    def __init__(self, first_name, last_name, department_id):
        self.first_name = first_name
        self.last_name = last_name
        self.department_id = department_id

    def __repr__(self):
        return f"Employee: {self.first_name} {self.last_name} works in Department ID {self.department_id}"


class Manager(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)

    # CONNECTING ONE DEPARTMENT WITH ONE MANAGER
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))

    def __init__(self, first_name, last_name, department_id):
        self.first_name = first_name
        self.last_name = last_name
        self.department_id = department_id

    def __repr__(self):
        return f"Manager: {self.first_name} {self.last_name} works in Department ID {self.department_id}"

```

This essentially has two main parts:

1. We defined our application, database path with SQLAlchemy authorization as well as defining our Migration.
2. In the `class` definition portion we created our 3 Models.
    1. Departments
    2. Employees
    3. Managers

Our main Model `Department` contains the column relationships. So far, we can tell is there is a one-to-one
relationship because we set `uselist=False`.

## Exploring Flask Model Relationships

Before exploring we:

* deleted the old Migrations and DB
* set up our Migration files
* migrated our initial Models creation and updated

Starting the DB exploration part, we create a file called `db_exploration.py` where we will create our Instances and
define our Models relationships. `db_exploration.py` contains the following:

```python
from basics import db, Department, Manager, Employee

# CREATING TWO DEPARTMENT OBJECTS
tech = Department('Tech', 5)
AM = Department('Account Manager', 3)

# Adding these two Department instances to the db
db.session.add_all([tech, AM])
db.session.commit()

# Check instances properly added to DB
print(Department.query.all())

# Grab specific instance (This returns a list)
tech = Department.query.filter_by(name='Tech').first()
print(tech)

# Creating Manager for Tech department
tech_manager = Manager('Jose', 'Servin', tech.id)

# Creating Employees for Tech department
emp_1 = Employee('Baker', 'Servin', tech.id)
emp_2 = Employee('Camila', 'Servin', tech.id)

# Commit Manger and new Employees to DB
db.session.add_all([tech_manager, emp_1, emp_2])
db.session.commit()

# Grab tech again after DB updates
tech = Department.query.filter_by(name='Tech').first()
print(tech)

# Show Tech employees
tech.report_employees()

```

Which prints:

```commandline
[Tech department has no Manager assigned. , Account Manager department has no Manager assigned. ]
Tech department has no Manager assigned. 
Department name: Tech | Manager Jose Servin
Tech department has these employees: 
Baker Servin
Camila Servin

```


