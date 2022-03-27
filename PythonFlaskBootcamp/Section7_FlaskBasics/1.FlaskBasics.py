from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')  # this renders at http://127.0.0.1:5000/
def home():
    return render_template('home.html')


@app.route('/user/<name>')
def user_page(name):
    return render_template('user.html', name=name)


if __name__ == "__main__":
    app.run(debug=True)
