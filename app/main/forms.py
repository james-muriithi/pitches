from unicodedata import category
from click import option
from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SelectField
from wtforms.validators import InputRequired
from ..models import Pitch

class PitchForm(FlaskForm):
    """
    Pitch form
    """
    title = StringField("Title", validators=[InputRequired()])
    category = SelectField("Category", validators=[InputRequired()])
    description = TextAreaField("Description", validators=[InputRequired()])