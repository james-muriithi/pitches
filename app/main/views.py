from flask import redirect, render_template, url_for
from flask_login import current_user
from . import main
from .. import db
from .forms import PitchForm
from ..models import Pitch


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/dashboard')
def dashboard():
    return 'dashboard' 

@main.route('/profile')
def profile():
    return 'profile'       


@main.route('/pitch/create', methods=['POST'])
def pitch_create():
    form = PitchForm()
    if form.validate_on_submit():
        pitch = Pitch(title=form.title.data, description=form.description.data,
                      user=current_user, category_id=form.category.data)
        db.session.add(pitch)
        db.session.commit()

    return redirect(url_for('main.pitch_create'))
