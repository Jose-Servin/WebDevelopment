from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/user/<user_name>')
def template_inheritance_demo(user_name):
    user_name = user_name
    return render_template('user.html', user_name=user_name)


if __name__ == '__main__':
    app.run(debug=True)
