import os
from flask import Flask, jsonify, request, Response, redirect
from flask_cors import CORS
from classes import Brasileirao
import re
import requests
from bs4 import BeautifulSoup
import json

app = Flask(__name__)
CORS(app)


def getData(serie):
    soup = BeautifulSoup(requests.get(
        "https://globoesporte.globo.com/futebol/brasileirao-serie-{}/".format(serie)).text, 'html.parser')
    data = json.loads(re.search(r"classificacao = (.*?);",
                                soup.find("script", {"id": "scriptReact"}).text).group(1))
    data_artilheiros = soup.find("section", {"class": "artilharia-wrapper"}
                                 ).find_all("div", {"class": "jogador"})
    data["artilheiros"] = [{"time": jogador.find("div", {"class": "jogador-escudo"}).find("img")['alt'],
                            "nome": jogador.find("div", {"class": "jogador-nome"}).text,
                            "gols": int(jogador.find("div", {"class": "jogador-gols"}).text)
                            } for jogador in data_artilheiros]
    return data


@app.route('/')
def Hello(serie):
    return redirect("https://github.com/renoviana/brasileiraoapi", code=302)


@app.route('/<serie>')
def getSerie(serie):
    print("oi")
    return jsonify(Brasileirao.from_dict(getData(serie)).to_dict())


@app.route('/<serie>/classificacao')
def getClassificacao(serie):
    return jsonify([classificacao.to_dict() for classificacao in Brasileirao.from_dict(getData(serie)).classificacao])


@app.route('/<serie>/edicao')
def getEdicao(serie):
    return jsonify(Brasileirao.from_dict(getData(serie)).to_dict)


@app.route('/<serie>/lista_jogos')
def getListaJogos(serie):
    return jsonify([lista_jogos.to_dict() for lista_jogos in Brasileirao.from_dict(getData(serie)).lista_jogos])


@app.route('/<serie>/artilheiros')
def getArtilheiros(serie):
    return jsonify([artilheiro.to_dict() for artilheiro in Brasileirao.from_dict(getData(serie)).artilheiros])


@app.route('/<serie>/faixas_classificacao')
def getFaixasClassificacao(serie):
    return jsonify([faixa.to_dict() for faixa in Brasileirao.from_dict(getData(serie)).faixas_classificacao])


@app.route('/<serie>/fase')
def getFase(serie):
    return jsonify(Brasileirao.from_dict(getData(serie)).fase.to_dict())


@app.route('/<serie>/fases_navegacao')
def getFasesNavegacao(serie):
    return jsonify([fases.to_dict() for fases in Brasileirao.from_dict(getData(serie)).fases_navegacao])


@app.route('/<serie>/rodada')
def getRodadaAtual(serie):
    return jsonify(Brasileirao.from_dict(getData(serie)).rodada.to_dict())


@app.route('/<serie>/rodada/<rodada>')
def getRodada(serie, rodada):
    url = url = "https://api.globoesporte.globo.com/tabela/d1a37fa4-e948-43a6-ba53-ab24ab3a45b1/fase/fase-unica-seriea-2019/rodada/{}/jogos/".format(
        rodada)
    if(serie == "b"):
        url = "https://api.globoesporte.globo.com/tabela/009b5a68-dd09-46b8-95b3-293a2d494366/fase/fase-unica-serieb-2019/rodada/{}/jogos/".format(
            rodada)

    return jsonify(requests.get(url).json())


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
