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
    return json.dumps(brasileirao.to_dict())


# @app.route('/<fromx>/<to>')
# def getSentido(fromx, to):
#     sentido = to if(fromx == "central") else fromx
#     data = moovit.getJson(sentido)
#     if(sentido == "ceilandia"):
#         arraydata = data["syncedStops"][::-
#                                         1] if(fromx == "central") else data["syncedStops"]
#         i = 0 if(fromx == "central") else 1
#     else:
#         arraydata = data["syncedStops"] if(fromx == "central") else data["syncedStops"][:: -
#                                                                                         1]
#         i = 0 if(fromx == "central") else 0

#     partidasCeilandia = [{"epoch": departure, "formated": moovit.epochToDateTime(departure, "%H:%M")} for departure in data["lineTrips"]
#                          ["linesTrips"][i]['tripGroups'][0]['departures']]
#     intervalos = [{"epoch": interval, "formated": moovit.epochToDateTime(
#         interval, "%H:%M")} for interval in data["lineTrips"]["linesTrips"][i]['tripIntervals'][0]['intervals']]
#     estacoes = moovit.getEstacoes(arraydata, intervalos)
#     horarios = moovit.partidasDict(estacoes, partidasCeilandia)
#     return Response(response=json.dumps(moovit.proximoTrem(horarios)),
#                     status=200,
#                     mimetype="application/json")


# @app.route('/')
# def getOpcoes():
#     array = [{'Central->Ceilandia': 'http://metrodfapi.herokuapp.com/central/ceilandia'}, {'Ceilandia->Central': 'http://metrodfapi.herokuapp.com/ceilandia/central'},
#              {'Central->Samambaia': 'http://metrodfapi.herokuapp.com/central/samambaia'}, {'Samambaia->Central': 'http://metrodfapi.herokuapp.com/samambaia/central'}]
#     return jsonify(array)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
