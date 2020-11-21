from flask_wtf import FlaskForm
from wtforms StringField, validators
from wtforms.validators import DataRequired, Regexp

class myForm(FlaskForm):
    message = StringField('write a message')