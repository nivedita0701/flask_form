from wtforms import Form
from wtforms import StringField, validators
from wtforms.validators import DataRequired, Regexp

class myForm(Form):
    message = StringField('write a message', [validators.Required()])