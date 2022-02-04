from flask import redirect, render_template, url_for
from flask_login import current_user
from . import main
from .. import db
from .forms import PitchForm
from ..models import Category, Pitch


@main.route('/')
def index():
    pitchForm = PitchForm()
    categories = Category.get_all_categories()

    pitches = Pitch.get_all_pitches()

    return render_template('index.html', pitchForm=pitchForm, categories=categories, pitches=pitches)


@main.route('/dashboard')
def dashboard():
    return 'dashboard'


@main.route('/profile')
def profile():
    return 'profile'


@main.route('/pitch/create', methods=['POST'])
def pitch_create():
    form = PitchForm()
    form.category.choices = [(cat.id, cat.name)
                             for cat in Category.get_all_categories()]
    if form.validate_on_submit():
        pitch = Pitch(title=form.title.data, description=form.description.data,
                      user=current_user, category_id=form.category.data)
        db.session.add(pitch)
        db.session.commit()

    return redirect(url_for('main.index'))
