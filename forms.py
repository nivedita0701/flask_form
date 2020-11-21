from wtforms import Form, StringField, validators
from wtforms.validators import DataRequired, Regexp

class myForm(Form):
    """Homepage form."""
    PlotlyURL = StringField('Provide a raw .ipynb URL from Github',
    validators=[
            DataRequired(),
            Regexp(".*\.ipynb$",
            message="Please provide a URL ending in ipynb"),
          ])