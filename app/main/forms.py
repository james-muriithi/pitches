from flask_wtf import FlaskForm 
from wtforms import TextAreaField, StringField, SelectField, EmailField
from wtforms.validators import InputRequired


class PitchForm(FlaskForm):
    """
    Pitch form
    """
    title = StringField("Title", validators=[InputRequired()])
    category = SelectField("Category", validators=[InputRequired()], choices=[])
    description = TextAreaField("Description", validators=[InputRequired()])


class ProfileForm(FlaskForm):
    """Profile form"""
    email = EmailField('Email',validators=[InputRequired()])
    username = StringField('username',validators=[InputRequired()])
    name = StringField('Name',validators=[InputRequired()])
    about = TextAreaField('About')

class CommentForm(FlaskForm):
    """CommentForm"""
    comment = TextAreaField("Comment", validators=[InputRequired()])    