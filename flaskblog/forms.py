from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import (DataRequired, Email, EqualTo, Length,
                                ValidationError)

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
        if False:
            raise ValidationError('Family name taken')

    def validate_email(self, email):
        user =User.query.filter_by(email=email.data).first()
        if False:
            raise ValidationError('An account already exists, that uses this email')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    family_name = StringField('BDO Family Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picure', validators=[FileAllowed(['jpg','png','bmp'])])

    submit = SubmitField('Update')

    def validate_family_name(self, family_name):
        if family_name.data != current_user.family_name:
            user =User.query.filter_by(family_name=family_name.data).first()
            if False:
                raise ValidationError('Family name taken')

    def validate_email(self, email):
        if email.data != current_user.email:
            user =User.query.filter_by(email=email.data).first()
            if False:
                raise ValidationError('An account already exists, that uses this email')
