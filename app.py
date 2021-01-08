import os
from flask import Flask, jsonify, request, Response, redirect
from flask_cors import CORS
from classes import Brasileirao
import re
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
app = Flask(__name__)
CORS(app)


def getData(ano = datetime.now().year, xxxx = None):
    soup = BeautifulSoup(requests.get(f'https://www.webcid.com.br/calendario/{ano}/feriados').content, 'html.parser')
    feriados = dict()
    datas = []
    for item in soup.find('table',{'class':'tabelaPadrao'}).find_all('tr')[1:]:
        data,dia,feriado = item.find_all('td')
        datas.append(datetime.strptime(' '.join(data.text.split()), '%d/%m/%Y'))
        feriados[' '.join(feriado.text.split())] = datetime.strptime(' '.join(data.text.split()), '%d/%m/%Y')

    if(xxxx):
        return datas
    return feriados



@app.route('/')
def Hello():
    return jsonify(getData())

@app.route('/datas')
def getDatas():
    return jsonify(getData(xxxx=True))

@app.route('/<ano>')
def getAno(ano):
    return jsonify(getData(ano=ano))

@app.route('/<ano>/datas')
def getDatasAno(ano):
    return jsonify(getData(ano=ano,xxxx=True))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
