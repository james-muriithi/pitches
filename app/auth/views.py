from crypt import methods
from flask import render_template,redirect, url_for
from . import auth
from .forms import LoginForm

@auth.route('/login', methods = ['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('auth.index'))
    return render_template('login.html', form = form)

@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    return render_template('signup.html')    