from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo,Email

class RegisterForm(Form):
    name = StringField('Username',validators=[DataRequired(), Length(min=2,max=20)])
    surname = StringField('Surname',validators=[DataRequired(), Length(min=2,max=20)])
    email = StringField('Email',validators=[DataRequired(), Length(min=6,max=40)])
    password = PasswordField('Password',validators=[DataRequired(), Length(min=6,max=40)])
    confirm = PasswordField('Password confirmation',validators=[DataRequired(), EqualTo('password')])
