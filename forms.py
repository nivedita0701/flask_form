from wtforms import Form
from wtforms import TextField, validators
from wtforms.validators import DataRequired, Regexp

class myForm(Form):
    message = TextField('write a message')