# -*- coding: utf-8 -*- 
from flask import Flask

# puerto 7012 es usado para desarrollo en __main__
IA_SERVER = 'http://127.0.0.1:7012'

IA_URL = '/ejercicio3/app2-ia/summary'

app = Flask(__name__,
            static_url_path='/ejercicio3/app2-front/static')
