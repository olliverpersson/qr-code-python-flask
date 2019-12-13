from flask import Flask
import os
import threading
import pathlib

app = Flask(__name__)

app.config['SECRET_KEY'] = 'you-will-never-guess'

from app import routes

#Clear qrcodes folder
def clear_qr_codes():
    
    pth = pathlib.Path('app/static/qrcodes')
    
    for sub in pth.iterdir():
        if sub.is_dir():
            delete_folder(sub)
        else:
            sub.unlink()
    
    try:
        seconds = int(os.environ['CLEAR_CACHE_SECONDS'])
    except:
        print('CLEAR_CACHE_SECONDS not defined, using 1800 seconds(30 minutes)')
        seconds = 1800
    
    threading.Timer(seconds, clear_qr_codes).start()
  
clear_qr_codes()