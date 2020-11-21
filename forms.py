from wtforms import Form, StringField, validators
from wtforms.validators import DataRequired, Regexp

class myForm(Form):
    message = StringField('write a message')