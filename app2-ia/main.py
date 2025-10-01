# -*- coding: utf-8 -*- 
from app import app
from utils import resumir
from flask import Flask, jsonify, request

@app.route('/ejercicio3/app2-ia/summary', methods=['POST'])
def summary():
    json_texto = request.json
    print("se recibe: {}".format(json_texto))
    texto = json_texto['texto']
    resumen = resumir(texto)
    json_respuesta = {'resumen': resumen}
    print("responder: {}".format(json_respuesta))
    return jsonify(json_respuesta)

if __name__ == "__main__":
    app.run(port=7012)
