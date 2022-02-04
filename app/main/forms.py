from unicodedata import category
from click import option
from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SelectField
from wtforms.validators import InputRequired


class PitchForm(FlaskForm):
    """
    Pitch form
    """
    title = StringField("Title", validators=[InputRequired()])
    category = SelectField("Category", validators=[InputRequired()], choices=[])
    description = TextAreaField("Description", validators=[InputRequired()])
