from pydoc import classname
from flask_wtf import FlaskForm
from wtforms import EmailField,PasswordField,BooleanField, SubmitField
from wtforms.validators import InputRequired,Email

class LoginForm(FlaskForm):
    """
    Login form
    """
    email = EmailField('Email',validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Submit')