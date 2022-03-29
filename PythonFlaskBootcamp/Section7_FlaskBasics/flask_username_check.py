from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('username_index.html')


@app.route('/report')
def report():
    username = request.args.get('username')

    # must have an uppercase letter check
    condition_one = (any(i.isupper() for i in username))

    # must have a lower case letter check
    condition_two = any(i.islower() for i in username)

    # must have a number at the end check
    try:
        last_char = int(username[-1])
        condition_three = isinstance(last_char, int)
    except ValueError:
        condition_three = False

    return render_template('username_report.html', username=username, condition_one=condition_one,
                           condition_two=condition_two, condition_three=condition_three)


if __name__ == "__main__":
    app.run(debug=True)
