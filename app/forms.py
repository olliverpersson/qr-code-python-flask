from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField, PasswordField
from wtforms.validators import DataRequired, Length

class CreateForm(FlaskForm):
    
    textToCreate = StringField('Text for QR Code', validators=[DataRequired()])
    submit = SubmitField('Create')
    
class CreateWifiForm(FlaskForm):
    
    wifiName = StringField('WIFI Name', validators=[DataRequired()])
    wifiType = SelectField('Wifi Type', choices = [('WEP', 'WEP'), ('WPA', 'WPA'), ('nopass', 'No password')], validators=[DataRequired()])
    wifiPass = PasswordField('Wifi Password')
    ssidHidden = BooleanField('Use SSID', validators=[DataRequired()])
    submit = SubmitField('Create')