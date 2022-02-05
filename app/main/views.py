from flask import redirect, render_template, url_for, flash
from flask_login import current_user, login_required
from wtforms.validators import ValidationError
from . import main
from .. import db
from .forms import PitchForm, ProfileForm
from ..models import Category, Pitch, User

@main.route('/')
def index():
    pitchForm = PitchForm()
    categories = Category.get_all_categories()

    pitches = Pitch.get_all_pitches()

    return render_template('index.html', pitchForm=pitchForm, categories=categories, pitches=pitches)


@main.route('/dashboard')
@login_required
def dashboard():
    return 'dashboard'


@main.route('/profile', methods=["GET","POST"])
@login_required
def profile():
    profile_form = ProfileForm()
    if profile_form.validate_on_submit():
        validate_email(profile_form.email.data)
        validate_username(profile_form.username.data)

        current_user.query.update({'email': profile_form.email.data, 'username':profile_form.username.data,
                    'name':profile_form.name.data, 'about': profile_form.about.data})
        db.session.commit()
        flash("Your details have been updated", "success")
        return redirect(url_for('main.profile'))
        
    return render_template('profile.html', form=profile_form)


@main.route('/pitch/create', methods=['POST'])
@login_required
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


def validate_email(email):
    user = User.query.filter_by(email = email).first()
    if user and user.id != current_user.id:
        raise ValidationError('Email already exists')

def validate_username(username):
    user = User.query.filter_by(username = username).first()
    if user and user.id != current_user.id:
        raise ValidationError('Username is already taken')