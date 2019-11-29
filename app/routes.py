from flask import render_template, request, url_for, redirect
from app import app
import os
import pyqrcode
from app.forms import CreateForm, CreateWifiForm
from uuid import uuid4 as uuid

basedir = os.path.dirname(__file__)
# os.path.join(basedir, 'min-fil.txt') ger fullständig filväg till min-fil.txt

#from uuid import uuid4 as uuid
#id = str(uuid())
# genererar unika uuid strängar

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def creator():
    
    form = CreateForm()
    if form.validate_on_submit():
        
        qrcode = pyqrcode.create( form.textToCreate.data )
        
        qrid = uuid()
        
        qrcode.svg('app/static/qrcodes/{}.svg'.format(qrid), scale=8)
        
        return redirect(url_for('created', qrid=qrid))
        
    return render_template('creator.html', title='QR-CODE CREATOR', form=form)

@app.route('/wifi-qr-code', methods=['GET', 'POST'])
def wifiqr():
    
    form = CreateWifiForm()
    
    if form.validate_on_submit():
    
        qrtext = "WIFI:T:{};S:{};P:{};H:{};".format(form.wifiType.data, form.wifiName.data, form.wifiPass.data, str(form.ssidHidden.data))
    
        qrcode = pyqrcode.create( qrtext )
        
        qrid = uuid()
        
        qrcode.svg('app/static/qrcodes/{}.svg'.format(qrid), scale=8)
        
        return redirect(url_for('created', qrid=qrid))
    
    return render_template('wifiqr.html', form=form)


@app.route('/qrcode/<string:qrid>', methods=['GET'])
def created(qrid):
    
    return render_template('created.html', title='QR-CODE CREATED', qrid=qrid)

