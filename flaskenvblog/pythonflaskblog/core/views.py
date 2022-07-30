from flask import render_template, request, Blueprint

core = Blueprint('core', __name__)


@core.route('/')
def index():
    # TODO
    return render_template('index.html')


@core.route('/information')
def info():
    return render_template('info.html')
