from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')  # this renders at http://127.0.0.1:5000/
def home():
    return render_template('home.html')


@app.route('/signup')
def sign_up():
    return render_template('signup.html')


@app.route('/thankyou')
def thank_you():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template('thankyou.html', first=first, last=last)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
