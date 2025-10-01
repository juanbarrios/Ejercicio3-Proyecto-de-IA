# -*- coding: utf-8 -*-s
from app import app, IA_SERVER, IA_URL
import requests
import json
from flask import request, render_template


@app.route('/ejercicio3/app2-front/')
def index_form():
    return render_template('index.html')


@app.route('/ejercicio3/app2-front/upload', methods=['POST'])
def upload_texto():
    text = request.form
    if text == '':
        error = 'No se seleccionó ningún texto'
        return render_template('index.html', error=error)
    json_texto = {'texto': text['text']}
    print("llamando {} con {}".format(IA_SERVER + IA_URL, json_texto))
    try:
        apicall = requests.post(IA_SERVER + IA_URL, json=json_texto)
        if apicall.status_code != 200:
            error = 'Error contactando la aplicación IA'
            return render_template('index.html', error=error)
        api_json = json.loads(apicall.content.decode('utf-8'))
        print ("recibo: {}".format(api_json))
        return render_template('index.html', result=api_json['resumen'], error=None)
    except Exception as e:
        error = 'Error: {}'.format(e)
        print(error)
        return render_template('index.html', error=error)


if __name__ == "__main__":
    app.run(port=7011)
