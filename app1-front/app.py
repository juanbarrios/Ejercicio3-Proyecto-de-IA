# -*- coding: utf-8 -*- 
from flask import Flask

# puerto 7002 es usado para desarrollo en __main__
IA_SERVER = 'http://127.0.0.1:7002'

IA_URL = '/ejercicio3/app1-ia/predict'

UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__,
            static_url_path='/ejercicio3/app1-front/static')
            
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
