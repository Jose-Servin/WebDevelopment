from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('username_index.html')


@app.route('/report')
def report():
    username = request.args.get('username')

    # Pre-define the 3 boolean conditions
    lower = False
    upper = False
    final_num = False

    # must have an uppercase letter check
    upper = (any(i.isupper() for i in username))

    # must have a lower case letter check
    lower = any(i.islower() for i in username)

    # must have a number at the end check
    try:
        last_char = int(username[-1])
        final_num = isinstance(last_char, int)
    except ValueError:
        final_num = False

    all_good = lower and upper and final_num

    return render_template('username_report.html', username=username, lower=lower,
                           upper=upper, final_num=final_num, all_good=all_good)


if __name__ == "__main__":
    app.run(debug=True)
