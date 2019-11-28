from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class CreateForm(FlaskForm):
    
    textToCreate = StringField('Text for QR Code', validators=[DataRequired()])
    submit = SubmitField('Create')