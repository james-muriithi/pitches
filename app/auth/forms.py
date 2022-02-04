from ast import Str
from flask_wtf import FlaskForm
from wtforms import EmailField,PasswordField,BooleanField, SubmitField, StringField
from wtforms.validators import InputRequired,Email

class LoginForm(FlaskForm):
    """
    Login form
    """
    email = EmailField('Email',validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    remember = BooleanField('Remember Me')


class SignupForm(FlaskForm):
    """
    Signup form
    """
    email = EmailField('Email',validators=[InputRequired()])
    username = StringField('username',validators=[InputRequired()])
    name = StringField('Name',validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])