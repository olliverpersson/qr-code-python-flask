from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField, PasswordField
from wtforms.validators import DataRequired, Length

class CreateForm(FlaskForm):
    
    textToCreate = StringField('Text for QR Code', validators=[DataRequired()])
    errorCorrection = SelectField('Error Correction Level', choices=[('L', 'Low'), ('M', 'Mid'), ('Q', 'Mid-High'), ('H', 'High')])
    submit = SubmitField('Create')
    
class CreateWifiForm(FlaskForm):
    
    wifiName = StringField('Wifi Name', validators=[DataRequired()])
    wifiType = SelectField('Authentication Type', choices = [('WEP', 'WEP'), ('WPA', 'WPA'), ('nopass', 'No password')], validators=[DataRequired()])
    wifiPass = PasswordField('Wifi Password (optional)')
    ssidHidden = BooleanField('Hidden SSID')
    errorCorrection = SelectField('Error Correction Level', choices=[('L', 'Low'), ('M', 'Mid'), ('Q', 'Mid-High'), ('H', 'High')])
    submit = SubmitField('Create')