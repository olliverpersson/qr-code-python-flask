from flask import render_template, request, url_for, redirect
from app import app
import os
import pyqrcode
from app.forms import CreateForm
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
        
        imgsrc = qrcode.svg('qrcode.svg', scale=8)
        
        return redirect(url_for('created', imgtxt = form.textToCreate.data, imgsrc=imgsrc))
        
    return render_template('creator.html', title='QR-CODE CREATOR', form=form)

@app.route('/qrcode/<string:imgtxt>/<string:imgsrc>/', methods=['GET'])
def created(imgsrc,imgtxt):
    
    return render_template('created.html', title='QR-CODE CREATED', imgsrc=imgsrc, imgtxt=imgtxt)