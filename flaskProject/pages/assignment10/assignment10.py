from flask import Blueprint, render_template

assignment10 = Blueprint('assignment10', __name__,
                         static_folder='static',
                         template_folder='templates')

@assignment10.route('/assignment10')
def assignment10_func():
    return render_template('assignment10.html')