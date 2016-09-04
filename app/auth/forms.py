from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo 
from wtforms import ValidationError
from ..models import User

from wtforms.validators import Required, Length, Email

class LoginForm(Form):
    email = StringField('Email', validators = [Required(), Length(1,64), \
                        Email()])
    password = PasswordField('Password', validators = [Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')


class RegisterForm(Form):
    email = StringField('Email', validators = [Required(), Length(1,64), Email()])

    username = StringField('Username', validators = [Required(),Length(1,64), \
                            Regexp('^[A-Za-z][A-Za-z0-9]*$', 0, 'Username must \
                            only contain letters, numbers, dots or underscore') ])
    password = PasswordField('Password', validators = [Required(), \
                            EqualTo('password2', message = 'password must be \
                            match') ] )

    password2 = PasswordField('Confirm Password', validators = [Required()])

    submit = SubmitField('Register')

    def validate_username(self, field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError('Username Aready In Use')

    def validate_email(self,field):
        if User.query.filter_by(email= field.data).first():
            raise ValidationError('Email Already In Use')
