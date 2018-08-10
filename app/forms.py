from wtforms.validators import DataRequired, Optional
from wtforms.fields.html5 import TimeField
from wtforms import StringField
from flask_wtf import FlaskForm

class StoryForm(FlaskForm):
    location = StringField('Location', validators=[Optional()])
    time = TimeField('Time', validators=[Optional()])
    event_name = StringField('Event Name', validators=[Optional()])
