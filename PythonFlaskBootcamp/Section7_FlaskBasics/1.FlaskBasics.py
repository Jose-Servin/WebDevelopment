from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')  # this renders at http://127.0.0.1:5000/
def index():
    return '<h1> Hello World </h1> '


@app.route('/page_two')  # this will now render at 127.0.0.1:5000/page_two
def info():
    return "<h1> This is page two. </h1>"


# Creating a Dynamic Route
@app.route('/monitor/<name>')  # the name in the route is passed to the view function
def monitor(name):
    return f"<h1> This is a page for {name.upper()} </h1> "


# Debug Mode
@app.route('/debug/<name>')
def debug(name):
    return f"The 100th character of this name is {name[100]}."


# Flask Routing Exercise "Fake Latin"
@app.route('/fake_latin/<name>')
def fake_latin(name):
    if name[-1] == 'y':
        latin_name = name + 'iful'

    else:
        latin_name = name + "y"

    return f"<h1> Hi {name}, your fake latin name is {latin_name}.</h1>"


if __name__ == "__main__":
    app.run(debug=True)
