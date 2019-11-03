import os
from flask import Flask, jsonify, request, Response
from classes import Brasileirao
import re
import requests
from bs4 import BeautifulSoup
import json
app = Flask(__name__)


@app.route('/<serie>')
def getSerie(serie):
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
    brasileirao = Brasileirao.from_dict(data)
    return jsonify(brasileirao.to_dict())


@app.route('/<serie>/classificacao')
def getClassificacao(serie):
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
    brasileirao = Brasileirao.from_dict(data)
    return jsonify([classificacao.to_dict() for classificacao in brasileirao.classificacao])


@app.route('/<serie>/edicao')
def getEdicao(serie):
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
    brasileirao = Brasileirao.from_dict(data)
    return jsonify(brasileirao.edicao.to_dict())


@app.route('/<serie>/lista_jogos')
def getListaJogos(serie):
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
    brasileirao = Brasileirao.from_dict(data)
    return jsonify([lista_jogos.to_dict() for lista_jogos in brasileirao.lista_jogos])


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
