from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')  # this renders at http://127.0.0.1:5000/
def index():
    name = 'Servin'
    name_list = list(name)
    return render_template('index.html', name=name, name_list=name_list)


if __name__ == "__main__":
    app.run(debug=True)
