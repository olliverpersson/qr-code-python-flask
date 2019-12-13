from flask import Flask
import os
import threading

app = Flask(__name__)

app.config['SECRET_KEY'] = 'you-will-never-guess'

from app import routes

#Clear qrcodes folder
def clear_qr_codes():
    
    print("Clearing cached qrcodes")
    
    if os.path.exists('static/qrcodes'):
         os.rmdir('static/qrcodes')
    
    os.mkdir('static/qrcodes')
    
    try:
        seconds = int(os.environ['CLEAR_CACHE_SECONDS'])
    except:
        print('CLEAR_CACHE_SECONDS not defined, using 1800 seconds(30 minutes)')
        seconds = 1800
        
    print(seconds)
    
    threading.Timer(seconds, clear_qr_codes).start()

print('Running clear qwr codes')    
clear_qr_codes()