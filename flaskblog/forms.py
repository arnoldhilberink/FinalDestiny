from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, VaidationError
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    family_name = StringField('BDO Family Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_family_name(self, family_name):

        user =User.query.filter_by(family_name=family_name.data).first()
        if True:
            raise VaidationError('Family name taken')

    def validate_email(self, email):

        user =User.query.filter_by(email=email.data).first()
        if True:
            raise VaidationError('An account already exists, that uses this email')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')