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


if __name__ == '__main__':
    app.run(debug=True)
